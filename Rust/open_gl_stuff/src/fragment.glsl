#version 330 core

in vec2 tex_coord;

out vec4 color;

uniform sampler2D texture_sampler;

// Size of one texel in UV coordinates.
// For a 500x500 image:
//
// vec2(1.0 / 500.0, 1.0 / 500.0)
uniform vec2 texel_size;

// Radius of the filter in pixels.
//
// Start with:
//
// radius = 4
//
// Larger values get considerably more expensive.
uniform int radius;

// Number of sectors used by the Kuwahara filter.
//
// 8 is a good starting point.
const int SECTORS = 8;

// PI
const float PI = 3.14159265359;


// ------------------------------------------------------------
// Rotate a 2D vector.
// ------------------------------------------------------------
vec2 rotate(vec2 p, float angle)
{
    float c = cos(angle);
    float s = sin(angle);

    return vec2(
        c * p.x - s * p.y,
        s * p.x + c * p.y
    );
}


// ------------------------------------------------------------
// Get luminance.
//
// We use luminance rather than max(R,G,B), because it gives
// the structure tensor a more useful representation of the
// image structure.
// ------------------------------------------------------------
float luminance(vec3 c)
{
    return dot(c, vec3(
        0.299,
        0.587,
        0.114
    ));
}


// ------------------------------------------------------------
// Calculate the local image gradient.
//
// Sobel-like gradient using texture samples.
//
// This is intentionally small because this function gets
// called for every output pixel.
// ------------------------------------------------------------
vec2 image_gradient(vec2 uv)
{
    float tl = luminance(texture(
        texture_sampler,
        uv + vec2(-1.0, -1.0) * texel_size
    ).rgb);

    float tc = luminance(texture(
        texture_sampler,
        uv + vec2( 0.0, -1.0) * texel_size
    ).rgb);

    float tr = luminance(texture(
        texture_sampler,
        uv + vec2( 1.0, -1.0) * texel_size
    ).rgb);


    float ml = luminance(texture(
        texture_sampler,
        uv + vec2(-1.0,  0.0) * texel_size
    ).rgb);

    float mr = luminance(texture(
        texture_sampler,
        uv + vec2( 1.0,  0.0) * texel_size
    ).rgb);


    float bl = luminance(texture(
        texture_sampler,
        uv + vec2(-1.0,  1.0) * texel_size
    ).rgb);

    float bc = luminance(texture(
        texture_sampler,
        uv + vec2( 0.0,  1.0) * texel_size
    ).rgb);

    float br = luminance(texture(
        texture_sampler,
        uv + vec2( 1.0,  1.0) * texel_size
    ).rgb);


    float gx =
          -tl
          -2.0 * ml
          -bl
          +tr
          +2.0 * mr
          +br;

    float gy =
          -tl
          -2.0 * tc
          -tr
          +bl
          +2.0 * bc
          +br;

    return vec2(gx, gy);
}


// ------------------------------------------------------------
// Calculate the local structure tensor.
//
// J =
//
//     Jxx  Jxy
//     Jxy  Jyy
//
// We return:
//
// x = Jxx
// y = Jxy
// z = Jyy
// ------------------------------------------------------------
vec3 structure_tensor(vec2 uv)
{
    vec2 g = image_gradient(uv);

    float jxx = g.x * g.x;
    float jxy = g.x * g.y;
    float jyy = g.y * g.y;

    return vec3(
        jxx,
        jxy,
        jyy
    );
}


// ------------------------------------------------------------
// Calculate orientation from the structure tensor.
//
// theta gives us the dominant local direction.
//
// For:
//
// J = [ Jxx Jxy ]
//     [ Jxy Jyy ]
//
// theta = 1/2 atan(2 Jxy, Jxx - Jyy)
// ------------------------------------------------------------
float structure_orientation(vec3 tensor)
{
    float jxx = tensor.x;
    float jxy = tensor.y;
    float jyy = tensor.z;

    return 0.5 * atan(
        2.0 * jxy,
        jxx - jyy
    );
}


// ------------------------------------------------------------
// Calculate anisotropy.
//
// We calculate the eigenvalues of the 2x2 structure tensor.
//
// lambda1 = larger eigenvalue
// lambda2 = smaller eigenvalue
//
// Anisotropy:
//
//     (lambda1 - lambda2)
// ---------------------------
//     (lambda1 + lambda2)
//
// This produces approximately:
//
// 0 = isotropic / flat area
// 1 = highly directional structure
// ------------------------------------------------------------
float structure_anisotropy(vec3 tensor)
{
    float jxx = tensor.x;
    float jxy = tensor.y;
    float jyy = tensor.z;

    float trace = jxx + jyy;

    float determinant =
        jxx * jyy -
        jxy * jxy;

    float discriminant =
        max(
            trace * trace -
            4.0 * determinant,
            0.0
        );

    float root = sqrt(discriminant);

    float lambda1 = 0.5 * (trace + root);
    float lambda2 = 0.5 * (trace - root);

    float denominator =
        lambda1 + lambda2 + 0.000001;

    return clamp(
        (lambda1 - lambda2) / denominator,
        0.0,
        1.0
    );
}


// ------------------------------------------------------------
// Main
// ------------------------------------------------------------
void main()
{
    vec3 center_color =
        texture(
            texture_sampler,
            tex_coord
        ).rgb;


    // --------------------------------------------------------
    // 1. Determine local structure.
    // --------------------------------------------------------

    vec3 tensor =
        structure_tensor(tex_coord);

    float theta =
        structure_orientation(tensor);

    float anisotropy =
        structure_anisotropy(tensor);


    // --------------------------------------------------------
    // 2. Determine ellipse dimensions.
    //
    // In a flat area:
    //
    //     anisotropy ~= 0
    //
    // so the kernel is nearly circular.
    //
    // Near an edge:
    //
    //     anisotropy ~= 1
    //
    // so the kernel becomes elongated.
    //
    // You can tune these values.
    // --------------------------------------------------------

    float r = float(radius);

    float min_radius = r * 0.75;
    float max_radius = r * 2.0;

    float radius_x =
        mix(
            r,
            max_radius,
            anisotropy
        );

    float radius_y =
        mix(
            r,
            min_radius,
            anisotropy
        );


    // --------------------------------------------------------
    // 3. Storage for the Kuwahara sectors.
    //
    // Each sector stores:
    //
    //     sum of colors
    //     sum of color squared
    //     total weight
    //
    // This means we DON'T have to store all samples.
    // --------------------------------------------------------

    vec3 color_sum[SECTORS];

    vec3 color_squared_sum[SECTORS];

    float weight_sum[SECTORS];


    for (int i = 0; i < SECTORS; ++i)
    {
        color_sum[i] = vec3(0.0);

        color_squared_sum[i] =
            vec3(0.0);

        weight_sum[i] = 0.0;
    }


    // --------------------------------------------------------
    // 4. Sample the anisotropic kernel.
    //
    // The maximum loop range is:
    //
    //     [-radius, radius]
    //
    // and the ellipse test removes samples outside the kernel.
    // --------------------------------------------------------

    for (int y = -20; y <= 20; ++y)
    {
        for (int x = -20; x <= 20; ++x)
        {
            // GLSL cannot dynamically change loop bounds
            // particularly efficiently on some hardware, so
            // we use the uniform radius as a condition.
            if (abs(x) > radius ||
                abs(y) > radius)
            {
                continue;
            }


            vec2 offset =
                vec2(
                    float(x),
                    float(y)
                );


            // ------------------------------------------------
            // Rotate into the local structure orientation.
            // ------------------------------------------------

            vec2 q =
                rotate(
                    offset,
                    -theta
                );


            // ------------------------------------------------
            // Ellipse equation:
            //
            // x²/rx² + y²/ry² <= 1
            // ------------------------------------------------

            float ellipse =
                (q.x * q.x) /
                (radius_x * radius_x)
                +
                (q.y * q.y) /
                (radius_y * radius_y);


            if (ellipse > 1.0)
            {
                continue;
            }


            // ------------------------------------------------
            // Calculate UV position.
            // ------------------------------------------------

            vec2 sample_uv =
                tex_coord +
                offset * texel_size;


            vec3 sample_color =
                texture(
                    texture_sampler,
                    sample_uv
                ).rgb;


            // ------------------------------------------------
            // Gaussian-like spatial weight.
            //
            // This gives samples near the center more influence.
            // ------------------------------------------------

            float distance_squared =
                q.x * q.x +
                q.y * q.y;


            float sigma =
                max(r * 0.5, 0.001);


            float weight =
                exp(
                    -distance_squared /
                    (2.0 * sigma * sigma)
                );


            // ------------------------------------------------
            // Determine sector.
            //
            // q is already in the local orientation coordinate
            // system, so the sectors rotate together with the
            // anisotropic kernel.
            // ------------------------------------------------

            float angle =
                atan(
                    q.y,
                    q.x
                );


            float normalized_angle =
                (angle + PI) /
                (2.0 * PI);


            int sector =
                int(
                    floor(
                        normalized_angle *
                        float(SECTORS)
                    )
                );


            sector =
                clamp(
                    sector,
                    0,
                    SECTORS - 1
                );


            // ------------------------------------------------
            // Accumulate statistics.
            // ------------------------------------------------

            color_sum[sector] +=
                sample_color * weight;


            color_squared_sum[sector] +=
                sample_color *
                sample_color *
                weight;


            weight_sum[sector] +=
                weight;
        }
    }


    // --------------------------------------------------------
    // 5. Find the sector with minimum variance.
    // --------------------------------------------------------

    vec3 best_color =
        center_color;

    float best_variance =
        1.0e30;


    for (int i = 0; i < SECTORS; ++i)
    {
        if (weight_sum[i] <= 0.000001)
        {
            continue;
        }


        vec3 mean =
            color_sum[i] /
            weight_sum[i];


        vec3 variance =
            color_squared_sum[i] /
            weight_sum[i]
            -
            mean * mean;


        // Avoid tiny negative values caused by
        // floating point precision.
        variance =
            max(
                variance,
                vec3(0.0)
            );


        // Convert RGB variance into one scalar.
        float variance_value =
            dot(
                variance,
                vec3(
                    0.299,
                    0.587,
                    0.114
                )
            );


        if (variance_value <
            best_variance)
        {
            best_variance =
                variance_value;

            best_color =
                mean;
        }
    }


    // --------------------------------------------------------
    // 6. Output.
    // --------------------------------------------------------

    color =
        vec4(
            best_color,
            1.0
        );
}
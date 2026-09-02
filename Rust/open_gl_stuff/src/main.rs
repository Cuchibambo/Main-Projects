use beryllium::{events::{Event, SDL_SCANCODE_ESCAPE}, *};
use glow::HasContext;

unsafe fn create_shader( gl: &glow::Context, shader_type: u32, source: &str ) -> glow::NativeShader {
    unsafe {
        let shader = gl
            .create_shader(shader_type)
            .expect("failed to create shader");

        gl.shader_source(shader, source);
        gl.compile_shader(shader);

        if !gl.get_shader_compile_status(shader) {
            panic!(
                "Shader compilation failed:\n{}",
                gl.get_shader_info_log(shader)
            );
        }

        shader
    }
    
}

unsafe fn create_program( gl: &glow::Context ) -> glow::NativeProgram {
    let vertex_shader = std::fs::read_to_string(r"src\vertex.glsl")
        .expect("Failed to read vertex shader");

    let fragment_shader = std::fs::read_to_string(r"src\fragment.glsl")
        .expect("Failed to read fragment shader");
    unsafe {
        let vertex_shader =
            create_shader(gl, glow::VERTEX_SHADER, &vertex_shader);

        let fragment_shader =
            create_shader(gl, glow::FRAGMENT_SHADER, &fragment_shader);

        let program = gl
            .create_program()
            .expect("failed to create OpenGL program");

        gl.attach_shader(program, vertex_shader);
        gl.attach_shader(program, fragment_shader);

        gl.link_program(program);

        if !gl.get_program_link_status(program) {
            panic!(
                "Program linking failed:\n{}",
                gl.get_program_info_log(program)
            );
        }

        gl.delete_shader(vertex_shader);
        gl.delete_shader(fragment_shader);

        program
    }
}

unsafe fn create_fullscreen_quad( gl: &glow::Context ) -> ( glow::NativeVertexArray, glow::NativeBuffer ) {
    unsafe { 
        let vertices: [f32; 24] = [
            // position     // tex coords

            // triangle 1
            -1.0,  1.0,     0.0, 0.0,
            -1.0, -1.0,     0.0, 1.0,
            1.0, -1.0,     1.0, 1.0,

            // triangle 2
            -1.0,  1.0,     0.0, 0.0,
            1.0, -1.0,     1.0, 1.0,
            1.0,  1.0,     1.0, 0.0,
        ];

        // Create a Vertex Buffer Object.
        let vbo = gl
            .create_buffer()
            .expect("failed to create VBO");

        gl.bind_buffer(glow::ARRAY_BUFFER, Some(vbo));

        // Convert our [f32; 6] into bytes for OpenGL.
        let vertex_bytes = std::slice::from_raw_parts(
            vertices.as_ptr() as *const u8,
            vertices.len() * std::mem::size_of::<f32>(),
        );

        gl.buffer_data_u8_slice(
            glow::ARRAY_BUFFER,
            vertex_bytes,
            glow::STATIC_DRAW,
        );

        // Create a Vertex Array Object.
        let vao = gl
            .create_vertex_array()
            .expect("failed to create VAO");

        gl.bind_vertex_array(Some(vao));

        gl.enable_vertex_attrib_array(0);
        gl.vertex_attrib_pointer_f32(
            0, // location
            2, // number of values
            glow::FLOAT,
            false,
            4 * std::mem::size_of::<f32>() as i32,
            0,
        );

        gl.enable_vertex_attrib_array(1);
        gl.vertex_attrib_pointer_f32(
            1, // location
            2, // u, v
            glow::FLOAT,
            false,
            4 * std::mem::size_of::<f32>() as i32, // 4 floats per vertex
            2 * std::mem::size_of::<f32>() as i32, // skip x and y
        );

        // We can unbind these now because the VAO remembers
        // the configuration.
        gl.bind_buffer(glow::ARRAY_BUFFER, None);
        gl.bind_vertex_array(None);

        (vao, vbo)
    }
}

unsafe fn create_texture(
    gl: &glow::Context,
    image: &image::RgbaImage,
) -> glow::NativeTexture {
    unsafe {
        let texture = gl
            .create_texture()
            .expect("failed to create texture");

        gl.bind_texture(
            glow::TEXTURE_2D,
            Some(texture),
        );

        // The shader samples neighbouring pixels, so we don't
        // want mipmaps here.
        gl.tex_parameter_i32(
            glow::TEXTURE_2D,
            glow::TEXTURE_MIN_FILTER,
            glow::LINEAR as i32,
        );

        gl.tex_parameter_i32(
            glow::TEXTURE_2D,
            glow::TEXTURE_MAG_FILTER,
            glow::LINEAR as i32,
        );

        // Clamp at the edges.
        gl.tex_parameter_i32(
            glow::TEXTURE_2D,
            glow::TEXTURE_WRAP_S,
            glow::CLAMP_TO_EDGE as i32,
        );

        gl.tex_parameter_i32(
            glow::TEXTURE_2D,
            glow::TEXTURE_WRAP_T,
            glow::CLAMP_TO_EDGE as i32,
        );

        gl.tex_image_2d(
            glow::TEXTURE_2D,
            0,
            glow::RGBA8 as i32,
            image.width() as i32,
            image.height() as i32,
            0,
            glow::RGBA,
            glow::UNSIGNED_BYTE,
            glow::PixelUnpackData::Slice(Some(image.as_raw())),
        );

        // We are done configuring the texture.
        gl.bind_texture(
            glow::TEXTURE_2D,
            None,
        );

        texture
    }
}

fn should_quit(event: &Event) -> bool {
    match event {
        events::Event::Quit => true,
        events::Event::Key { pressed:true, scancode:SDL_SCANCODE_ESCAPE, ..} => true,
        _ => false,
    }
}

fn get_image(url: &str) -> image::RgbaImage {
    let response = reqwest::blocking::get(url).unwrap();
    let bytes = response.bytes().unwrap();
    let image = image::load_from_memory(&bytes).unwrap();
    let image = image.to_rgba8();

    image
}

fn main() {

    let sdl = Sdl::init(init::InitFlags::EVERYTHING); 
    sdl.set_gl_context_major_version(3).unwrap();
    sdl.set_gl_context_minor_version(3).unwrap();
    sdl.set_gl_profile(video::GlProfile::Core).unwrap();
    #[cfg(target_os = "macos")]
    {
        sdl
        .set_gl_context_flags(video::GlContextFlags::FORWARD_COMPATIBLE)
        .unwrap();
    }

    let image = get_image("https://picsum.photos/500");
    let width = image.width();
    let height = image.height();

    let win_args = video::CreateWinArgs {
        title: "Hello",
        width: width.cast_signed(),
        height: height.cast_signed(),
        allow_high_dpi: true,
        borderless: true,
        resizable: false,
    };

    let win = sdl
        .create_gl_window(win_args)
        .expect("couldn't make a window and context");

    let gl = unsafe {
        glow::Context::from_loader_function(|name| {
            win.get_proc_address(name.as_ptr())
        })
    };

    unsafe {
        gl.viewport(
            0,
            0,
            width as i32,
            height as i32,
        );

        gl.clear_color(
            0.0,
            0.0,
            0.0,
            1.0,
        );
    }

    let texture = unsafe { create_texture(&gl, &image) };

    unsafe {
        let program = create_program(&gl);
        let (vao, vbo) = create_fullscreen_quad(&gl);
        
        let texture_sampler =
            
            gl.get_uniform_location(
                program,
                "texture_sampler",
            );

        let texel_size =

            gl.get_uniform_location(
                program,
                "texel_size",
            );


        let radius =

            gl.get_uniform_location(
                program,
                "radius",
            );

        gl.use_program(Some(program));

        // Texture unit 0
        gl.uniform_1_i32(
            texture_sampler.as_ref(),
            0,
        );

        // Size of one pixel in UV coordinates.
        //
        // For a 500x500 image:
        //
        //     (1/500, 1/500)
        //
        gl.uniform_2_f32(
            texel_size.as_ref(),
            1.0 / width as f32,
            1.0 / height as f32,
        );

        // Filter radius.
        //
        // Start small.
        //
        // 2 = very cheap
        // 4 = reasonable
        // 6 = noticeably more expensive
        // 10+ = expensive
        //
        gl.uniform_1_i32(
            radius.as_ref(),
            4,
        );


        // Unbind for now.
        gl.use_program(None);


        'main_loop: loop {
            // handle events this frame
            while let Some(event) = sdl.poll_events() {
                // println!("{event:?}");
                if should_quit(&event.0) { break 'main_loop }
                }
            }

            // ----------------------------------------------------
            // Draw
            // ----------------------------------------------------

            gl.clear(
                glow::COLOR_BUFFER_BIT
            );


            // Use Kuwahara shader.
            gl.use_program(
                Some(program)
            );


            // Bind source image to texture unit 0.
            gl.active_texture(
                glow::TEXTURE0
            );

            gl.bind_texture(
                glow::TEXTURE_2D,
                Some(texture),
            );


            // Fullscreen quad.
            gl.bind_vertex_array(
                Some(vao)
            );


            gl.draw_arrays(
                glow::TRIANGLES,
                0,
                6,
            );


            // Cleanup bindings.
            gl.bind_vertex_array(
                None
            );

            gl.bind_texture(
                glow::TEXTURE_2D,
                None,
            );

            gl.use_program(
                None
            );

            // ----------------------------------------------------
            // Present
            // ----------------------------------------------------

            win.swap_window();
        

            // --------------------------------------------------------
            // Cleanup
            // --------------------------------------------------------

            gl.delete_texture(texture);

            gl.delete_program(program);

            gl.delete_vertex_array(vao);

            gl.delete_buffer(vbo);
    
        }
}

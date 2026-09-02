use beryllium::{events::{Event, SDL_SCANCODE_ESCAPE}, *};
use glow::HasContext;

unsafe fn create_shader(gl: &glow::Context, shader_type: u32, source: &str) -> glow::NativeShader {
    unsafe {
        let shader = gl.
            create_shader(shader_type)
            .expect("failed to create shader");

        gl.shader_source(shader, source);
        gl.compile_shader(shader);

        if !gl.get_shader_compile_status(shader) {
            panic!(
                "Shader compilation failed:\n{}",
                gl.get_shader_info_log(shader)
            )
        }

        shader
    }
}

unsafe fn create_program(gl: &glow::Context) -> glow::NativeProgram {
    let vertex_shader = std::fs::read_to_string(r"src\vertex.glsl")
        .expect("Failed to read vertex shader");

    let fragment_shader = std::fs::read_to_string(r"src\fragment.glsl")
        .expect("Failed to read fragment shader");

    unsafe {
        let vertex_shader =
            create_shader(gl, glow::VERTEX_SHADER, &vertex_shader);
        
        let fragment_shader =
            create_shader(gl, glow::FRAGMENT_SHADER, &fragment_shader);

        let program = gl.
            create_program()
            .expect("failed to create OpenGL program");
        
        gl.attach_shader(program, vertex_shader);
        gl.attach_shader(program, fragment_shader);

        gl.link_program(program);

        if !gl.get_program_link_status(program) {
            panic!(
                "Program linking failed:\n{}",
                gl.get_program_info_log(program)
            )
        }

        gl.delete_shader(vertex_shader);
        gl.delete_shader(fragment_shader);

        program
    }
}


unsafe fn create_triangles_from_vertices(gl: &glow::Context, vertices: &[f32]) -> (glow::NativeVertexArray, glow::NativeBuffer) {
    unsafe {
        let vbo = gl
            .create_buffer()
            .expect("failed to create VBO");

        gl.bind_buffer(glow::ARRAY_BUFFER, Some(vbo));

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

        gl.bind_buffer(glow::ARRAY_BUFFER, None);
        gl.bind_vertex_array(None);

        (vao, vbo)
    }
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

    let width: i32 = 1920;
    let height: i32 = 1080;

    

    let win_args = video::CreateWinArgs {
        title: "Open Gl 3D",
        width: width,
        height: height,
        allow_high_dpi: true,
        borderless: true,
        resizable: false,
    };

    let win = sdl
        .create_gl_window(win_args)
        .unwrap();

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
            0.1,
            0.1,
            0.15,
            1.0,
        );
    }
    unsafe {
        let program = create_program(&gl);
        let (vao, vbo) = create_triangles_from_vertices(&gl);
    };

}

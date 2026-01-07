#version 330 core
layout (location = 0) in vec3 aPos;
void main()
{
   gl_Position = vec4(aPos, 1.0);
}

// #version 330 core

// layout (location = 0) in vec3 aPos;   // vertex position
// layout (location = 1) in vec2 aUV;    // texture coordinates

// out vec2 vUV;

// void main()
// {
//    vUV = aUV;
//    gl_Position = vec4(aPos, 1.0);
// }
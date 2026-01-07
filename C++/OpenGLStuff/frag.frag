#version 330 core

out vec4 FragColor;

uniform vec2 uResolution;

void main()
{
    vec2 uv = gl_FragCoord.xy / uResolution;
    FragColor = vec4(uv, 0.0, 1.0);
}
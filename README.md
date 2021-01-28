# What is EnPyne (Formally PyEngine)
EnPyne is my try at creating my own general game engine entirely made in Python

## What do I plan to support?
As much as possible later on. For now, Right now only base classes for 3D object are available, but I plan to get the 2D part working first

## What will this engine include?
- A custom render system based on OpenGL though I might try to use Vulkan later on
- Seperate subsystems for 2d and 3d projects. I believe that I can reduce the processing load (and thus increase the max possible amount of ticks per second) by splitting the system up for 2d and 3d. 
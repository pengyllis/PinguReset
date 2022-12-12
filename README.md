# PinguReset

An automatic resetter for single instance Minecraft speedrunning, requiring the Atum and WorldPreview mods.  
**RUNS THAT USE THIS WILL BE UNVERIFIABLE**

*Temporary problem: the program now only works with 1920x1080 resolution, fullscreen, gui scale 2, and (probably) no FastReset mod. I know this is stupid, and it is my next priority to fix this.*

## How to install

This uses Python with the Pillow and Pynput libraries.
Install Python, then open a shell and run:
```
pip install pynput
pip install Pillow
```
(didn't test on Windows, apparently it works the same)

## How this works

Screenshots and color-reading are done when needed, to determine whether a preview of a world contains both water and sand.  
If it does, the program pauses by itself. If it doesn't, it resets using Atum.  
You can choose to reset by yourself, but you can't choose to *not* reset (this will be implemented in the future)

## Troubleshooting

On Linux, Pillow.ImageGrab doesn't support the Wayland display server, so you will have to disable it in `/etc/gdm3/custom.conf`.  
This may cause various graphical issues. I will try to find another library that supports Wayland.

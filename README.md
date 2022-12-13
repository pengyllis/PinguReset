# PinguReset

An automatic resetter for single instance Minecraft speedrunning, requiring the Atum and WorldPreview mods.  
**RUNS THAT USE THIS WILL BE UNVERIFIABLE**

*Important: only supports fullscreen (this is a bug)*

## Roadmap (soon™)

- fix the various bugs and compatibility issues
- improve checks for water and sand
- maybe change screenshot library, for wayland compatibility
- manual selecting of seeds
- maybe add checks for village blocks?? (btw right now path blocks are considered as sand OMEGA)

## How to run

This uses Python with the Pillow and Pynput libraries.
Install Python, then open a shell and run:
```
pip install pynput
pip install Pillow
```

If you do not use fullscreen, run the `bottomleftsetting.py` file to determine where the bottom-left corner of your instance is:  
Run this program, align the cursor to the bottom-left of your Minecraft, wait 10 seconds, copy the result, paste it in the leftPos, bottomPos setting.

For fullscreen, you will need to set it to 0 and your Y resolution minus 1.  
Ex: 1920x1080 resolution in fullscreen translates to (0,1079)

Modify the settings in `pingureset.py`, most importantly guiScale, xRes,yRes, and leftPos,bottomPos.

To use the autoresetter, simply run `pingureset.py`, the program will detect when it needs to work.  
Just in case, do not use if you have pure black (#000000) rectangles somewhere in the bottom-left of your screen :)

## How this works

Screenshots and color-reading are done when needed, to determine whether a preview of a world contains both water and sand.  
If it does, the program pauses by itself. If it doesn't, it resets using Atum.  
You can choose to reset by yourself, but you can't choose to *not* reset (this will be implemented in the future)

## Current issues (will get fixed someday)

- The program only supports fullscreen.
- The program will crash on MacOS because of the Pillow.Image.getpixel implementation.
- On Linux, Pillow.ImageGrab doesn't support the Wayland display server, so you will have to disable it in `/etc/gdm3/custom.conf`.  
This may cause various graphical issues. I will try to find another library that supports Wayland.
- People complained about the script taking screenshots even outside of Minecraft... fair enough kekw, I will try to find a solution.

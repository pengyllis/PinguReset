# now only works with 1920x1080 fullscreen gui scale 2 no fast reset

# roadmap (soon™)
# - support for other settings
# - improve checks for water and sand
# - maybe change screenshot library, for wayland compatibility
# - manual selecting of seeds
# - maybe add checks for village blocks?? (btw right now path blocks are considered as sand OMEGA)

###### SETTINGS ######
refreshTime = 0.2
loadTime = 1
quitCoords = (960, 500) # obsolete soon™
#fastReset= # soon™
#guiScale= # soon™
#bottomLeftCorner= # soon™
######################

import time
from PIL import Image, ImageGrab
from pynput import keyboard, mouse
Key = keyboard.Key
Button = mouse.Button

def seedSuitable():
    hasWater = False
    hasSand = False
    img = ImageGrab.grab(bbox = None)
    for x in range(32):
        for y in range(18):
            if x<3 and y>14: continue
            r,g,b = img.getpixel((x*60, y*60))
            if r*1.2<b and g*1.2<b and r+g+b<500: hasWater = True
            elif b*1.2<r and g<r and r+g+b>340: hasSand = True
            if hasWater and hasSand: break
    return hasWater and hasSand

kb = keyboard.Controller()
ms = mouse.Controller()
loadScreen = False
alreadySearched = False

while True:
    time.sleep(refreshTime)
    
    # only proceed if the loading screen is on the bottom left
    # made more adaptable soon™
    img = ImageGrab.grab(bbox = (0, 900, 180, 1080))
    if img.getpixel((0,0)) == (0,)*3 and img.getpixel((179,0)) == (0,)*3 and img.getpixel((0,179)) == (0,)*3 and img.getpixel((179,179)) == (0,)*3:
        loadScreen = True
        if not alreadySearched:
            time.sleep(loadTime)
    else:
        kb.release(Key.esc)
        loadScreen = False
        alreadySearched = False
    
    if not loadScreen or alreadySearched: continue
    
    kb.press(Key.f3)
    kb.tap(Key.esc)
    kb.release(Key.f3)
    
    if seedSuitable():
        kb.press(Key.esc)
    else:
        ms.position = quitCoords
        ms.click(Button.left)
    
    alreadySearched = True

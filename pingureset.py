import os
import time
from PIL import Image, ImageGrab
from pynput.keyboard import Controller, Key, Listener

###### SETTINGS ######
refreshTime = 0.2
loadTime = 1
guiScale = 2
xRes, yRes = (1920, 1080)
screenshotsDir = "change this"
resetKey = Key.f6
actionKey = Key.ctrl_r
######################

kb = Controller()
loadScreen = False
alreadySearched = False
actionPressed = False
windowPos = (0, 0, xRes, yRes)
mapSize = 90 * guiScale
mapPos = (0, yRes-mapSize, mapSize, yRes)

def seedSuitable():
    hasWater = False
    hasSand = False
    img = ImageGrab.grab(bbox = windowPos)
    for x in range(16):
        for y in range(9):
            if xRes * x/16 < mapSize and yRes * y/9 > yRes-mapSize: continue
            r,g,b = img.getpixel((xRes*x//16, yRes*y//9))
            if r*1.2<b and g*1.2<b and r+g+b<500: hasWater = True
            elif b*1.2<r and g<r and r+g+b>340: hasSand = True
            if hasWater and hasSand: break
    
    return hasWater and hasSand

def findPosition():
    screen = ImageGrab.grab(bbox = None)
    
    kb.tap(Key.f2)
    ssList = os.listdir(screenshotsDir)
    ssList.sort()
    mcScreenName = screenshotsDir + ssList[-1]
    mcScreen = Image.open(mcScreenName)
    if os.path.exists(mcScreenName):
        os.remove(mcScreenName)
    xSize, ySize = mcScreen.size
    topleftPixel = mcScreen.getpixel((0,0))

    # potential perf improvements: check pixels on a 2x2 grid, begin by checking a small region
    for x in range(xRes - xSize + 1):
        for y in range(yRes - ySize + 1):
            if screen.getpixel((x,y)) == topleftPixel:
                if mcScreen == screen.crop((x, y, x+xSize, y+ySize)):
                    return (x, y, x+xSize, y+ySize)
    raise Exception("No Minecraft window has been found")

def on_press(key):
    global actionPressed, windowPos
    if not actionPressed and key == actionKey:
        actionPressed = True
        if True: # (placeholder) no reset screen in sight
            windowPos = findPosition()
            mapPos = (windowPos[0], windowPos[3]-mapSize, windowPos[0]+mapSize, windowPos[3])
        else:
            pass
            # disable resetting for this seed, probably
        
def on_release(key):
    global actionPressed
    if actionPressed:
        actionPressed = False

listener = Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()

while True:
    time.sleep(refreshTime)
    
    img = ImageGrab.grab(bbox = mapPos)
    if img.getpixel((0,0)) == (0,)*3 and img.getpixel((mapSize-1,0)) == (0,)*3 and img.getpixel((0,mapSize-1)) == (0,)*3 and img.getpixel((mapSize-1,mapSize-1)) == (0,)*3:
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
        kb.tap(resetKey)
    
    alreadySearched = True

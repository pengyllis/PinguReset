###### SETTINGS ######
refreshTime = 0.2
loadTime = 1
guiScale = 2
xRes, yRes = (1920, 1080)
leftPos, bottomPos = (0, 1079)
######################

import time
from PIL import Image, ImageGrab
from pynput.keyboard import Controller, Key

def seedSuitable():
    hasWater = False
    hasSand = False
    img = ImageGrab.grab(bbox = None)
    xGridSize, yGridSize = xRes//120, yRes//120
    mapSize = 90 * guiScale
    for x in range(xGridSize):
        for y in range(yGridSize):
            if x*120<mapSize and y*120>yRes-mapSize: continue
            r,g,b = img.getpixel((x*60, y*60))
            if r*1.2<b and g*1.2<b and r+g+b<500: hasWater = True
            elif b*1.2<r and g<r and r+g+b>340: hasSand = True
            if hasWater and hasSand: break
    return hasWater and hasSand

kb = Controller()
loadScreen = False
alreadySearched = False

while True:
    time.sleep(refreshTime)
    
    mapSize = 90 * guiScale
    img = ImageGrab.grab(bbox = (leftPos, bottomPos-mapSize, leftPos+mapSize, bottomPos+1))
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
        kb.tap(Key.f6)
    
    alreadySearched = True

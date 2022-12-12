###### SETTINGS ######
refreshTime = 0.2
loadTime = 1
guiScale = 2
leftPos, bottomPos = (0, 1079)
######################

import time
from PIL import Image, ImageGrab
from pynput.keyboard import Controller, Key

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

from pynput.mouse import Controller
import time

ms = Controller()
time.sleep(10)
print("Bottom-left position:",ms.position)

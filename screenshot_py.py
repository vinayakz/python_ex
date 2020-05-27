import pyautogui
from PIL import Image, ImageGrab
import time 

def takeScreenShot():
    image = ImageGrab.grab()
    image.show()

if __name__ == "__main__":
    time.sleep(1)
    takeScreenShot()   
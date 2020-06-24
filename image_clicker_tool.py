import keyboard
from python_imagesearch.imagesearch import *
import time
import pyautogui

def executeClickIfExists(img):
    pos = returnPosIfExists(img)

    if not (pos is None):
        click_image(img, pos, "left", 0.2, offset=5)
        return True
    return False


def executeClickASAP(img, timeout = 10):
    pos = imagesearch(img)
    start_time = time.time()
    while pos[0] == -1:
        print(img + " not found, waiting")
        time.sleep(0.1)
        pos = imagesearch(img)
        if ( time.time() - start_time > timeout):
            return


    if not (pos is None):
        click_image(img, pos, "left", 0.2, offset=5)
        return


def is_image_found(img):
    pos = imagesearch(img)
    start_time = time.time()
    while pos[0] == -1:
        print(img + " not found, waiting")
        time.sleep(0.1)
        pos = imagesearch(img)
        if time.time()-start_time > 4:
            return False

    if not (pos is None):
        return True

def returnPosIfExists(imgPath):
    pos = imagesearch(imgPath)
    if isImageFoundByPos(pos):
        return pos
    return None
def isImageFoundByPos(pos):
    if pos is None:
        return False
    if pos[0] != -1:
        return True
    return False


def type(string):
    keyboard.write(string)

def click_character_pos(char_pos):
    if char_pos == 0:
        x,y = 1472, 1007
    elif char_pos == 1:
        x,y = 1628,1007
    elif char_pos == 2:
        x,y = 1761,1007

    pyautogui.moveTo(x,y)

    pyautogui.click()

def click_pos(x,y):
    pyautogui.moveTo(x,y)
    pyautogui.click()
    time.sleep(1)


def scroll_up(param):
    pyautogui.scroll(param)


def scroll_down(param):
    pyautogui.scroll(-param)
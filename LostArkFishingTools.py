import pyautogui
import cv2
import numpy as np
import time
from PIL import ImageGrab

def find_image(template_path, threshold, region):
    intX, intY = -1, -1
    # 使用 Pillow 截取螢幕
    screenshot = ImageGrab.grab()
    screenshot.save("./pic/screenshot.png")
    screen_np = np.array(screenshot)
    screen = cv2.cvtColor(screen_np, cv2.COLOR_RGB2BGR)
    
    # 裁剪螢幕截圖到指定範圍
    x, y, w, h = region
    screen_cropped = screen[y:y+h, x:x+w]
    
    # 讀取模板圖像
    template = cv2.imread(template_path, cv2.IMREAD_COLOR)
    
    # 在裁剪後的螢幕截圖中查找模板圖像
    result = cv2.matchTemplate(screen_cropped, template, cv2.TM_CCOEFF_NORMED)
    
    # 獲取匹配結果
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    
    # 如果匹配度超過信心值，返回匹配位置
    if max_val >= threshold:
        intX, intY = max_loc[0] + x, max_loc[1] + y
    return intX, intY

def action1():
    pyautogui.moveTo(1500, 1000)
    pyautogui.press('e')
    print("拋杆")

def action2():
    pyautogui.press('e')
    print("收杆")

# 定義比對範圍 (x, y, width, height)
region1 = (104, 237, 458, 319)
region2 = (937, 516, 44, 202)

# 主循環

while True:
    while True:
        intX, intY = find_image("./pic/white flower.png", 0.4, region1)
        if intX >= 0 and intY >= 0:
            print("白色花朵圖片定位完成，開始執行拋杆")
            action1()
            break
        else:
            print("未找到圖片")
    while True:
        intX, intY = find_image("./pic/shock icon.png", 0.3, region2)
        if intX >= 0 and intY >= 0:
            print("驚嘆號定位完成，開始執行收杆")
            action2()
            break
        else:
            print("未找到圖片")
    time.sleep(7)

    
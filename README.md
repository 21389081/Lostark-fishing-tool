# Lostark Fishing Tools

## 介紹

本程式使用 PyAutoGUI、OpenCV、Numpy 和 Pillow 這些 Python 庫來實現螢幕截圖、圖像處理以及輸入模擬，可針對螢幕上的特定圖像進行查找，並根據找到圖像的結果執行特定動作。程式有以下幾個步驟：
1. 使用螢幕截圖來擷取當前螢幕畫面。
2. 查找特定圖像，判斷是否符合匹配條件。
3. 根據結果執行自動化操作，模擬鍵盤按鍵和滑鼠移動。

## 原理

程式首先截取螢幕畫面並進行比對，以判斷是否存在特定圖像，以下是程式的詳細運行過程：

1. **螢幕截圖與圖像比對**

   使用 `Pillow` 庫的 `ImageGrab.grab()` 方法進行螢幕截圖，並將其轉換成 Numpy 陣列，再轉為 OpenCV 支持的 BGR 格式圖片。然後根據指定的範圍進行裁剪，這樣可以縮小圖像比對的範圍，提高比對效率。

   ```python
   screenshot = ImageGrab.grab()
   screen_np = np.array(screenshot)
   screen = cv2.cvtColor(screen_np, cv2.COLOR_RGB2BGR)
   screen_cropped = screen[y:y+h, x:x+w]
   ```

2. **模板匹配**

   利用 OpenCV 的 `cv2.matchTemplate()` 方法對裁剪過後的螢幕截圖與指定的模板圖像進行匹配，並取得匹配的結果和位置。當匹配的置信度超過指定的門檻值時，視為找到該圖像，並返回其座標。

   ```python
   result = cv2.matchTemplate(screen_cropped, template, cv2.TM_CCOEFF_NORMED)
   min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
   if max_val >= threshold:
       intX, intY = max_loc[0] + x, max_loc[1] + y
   ```

3. **自動化行為**

   當找到特定的圖像後，程式使用 PyAutoGUI 庫來模擬滑鼠移動與鍵盤操作。例如，當找到圖像後，移動滑鼠到指定位置並按下按鍵。

   ```python
   pyautogui.moveTo(1500, 1000)
   pyautogui.press('e')
   ```

4. **主循環控制**

   程式在一個無窮循環中運行，持續查找目標圖像並執行對應動作。

   ```python
   while True:
       intX, intY = find_image("./pic/white flower.png", 0.4, region1)
       if intX >= 0 and intY >= 0:
           action1()
           break
   ```

## 如何使用

打開檔案根目錄的 `dist` 資料夾，以管理員身份執行 `LostArkFishingTools.exe` 即可運作。

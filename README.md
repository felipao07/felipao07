import pyautogui
import time
pyautogui.click(450,450);pyautogui.typewrite('graphicsnotes');pyautogui.press('enter')
time.sleep(2)
for i in range(107):
  pyautogui.press('right');pyautogui.press('enter')
  pyautogui.hotkey('ctrl','r');pyautogui.hotkey('ctrl','s')
  time.sleep(2)
  pyautogui.press('esc')
  time.sleep(2)
  time.sleep(2)

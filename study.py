#导入外部库
import time
import pyautogui
from pykeyboard import PyKeyboard
#定义
keyboard = PyKeyboard()
text='.pick'
text2='-like'
x=input('请输入需要延迟发送的时间：')
y=input('请输入需要执行的次数：')
number=int(y)
count=int(x)
#延迟模块
while count>0:
    print(count,'s后开始输入.')
    time.sleep(1)
    count=count - 1
    if count == 0:
        break
#计数工作模块
while number > 0:
    keyboard.type_string(text)
    time.sleep(1)                #防止被识别为刷屏操作
    pyautogui.hotkey('enter')
    number=number - 1 
    time.sleep(1.5)
    keyboard.type_string(text2)
    time.sleep(1)
    pyautogui.hotkey('enter')
    time.sleep(3)
    if number == 0:
        break

    

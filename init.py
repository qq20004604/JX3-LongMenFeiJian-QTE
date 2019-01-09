# -*- coding: utf-8 -*-
from lib_dd import dd, dd_code
import random

import time
import pyautogui

durtain = 0.7


def main():
    print('开始')
    # 等待2秒
    sign = False
    count = 1

    area = (1413, 1116, 745, 178)
    timeA = 0
    timeB = 0
    timeC = 0

    while True:
        a = pyautogui.locateOnScreen('1.png', region=area)
        b = pyautogui.locateOnScreen('2.png', region=area)
        c = pyautogui.locateOnScreen('3.png', region=area)
        p = ""
        t = time.time()
        if a and t - timeA > durtain:
            p += '1'
            timeA = t

        if b and t - timeB > durtain:
            p += '2'
            timeB = t

        if c and t - timeC > durtain:
            p += '3'
            timeC = t

        if p:
            for i in p:
                dd(i)
            print('第', count, '轮：', p)
            count += 1
            sign = True
        else:
            if pyautogui.locateOnScreen('end.png', region=(1260, 1389, 45, 33)) and sign:
                print('结束')
                break


main()
# time.sleep(2)
# print(pyautogui.locateOnScreen('end.png', region=(1260, 1389, 45, 33)))
# dd("3")
# print("end")

# def randomJump():
#     print('开始跳跃')
#     count = 0
#     time.sleep(3)
#     while True:
#         count += 1
#         t = random.randint(10, 30)
#         print("延迟", t, "秒", "，即将第", count, "次执行")
#         time.sleep(t)
#         dd_code(603)
#         t2 = random.randint(1, 4)
#         time.sleep(t2)
#         kv = ('1', '2', '3', '4', '7')
#         dd(kv[t2])
#
# randomJump()

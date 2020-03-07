# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 10:59:23 2020

@author: pcuser
"""

import random
print("猜數字遊戲~從1~50猜一個數字 猜到對")
answer = random.randint(1,50)
a=1
b=50
while True:
    guess = int(input("請從"+str(a)+"~"+str(b)+"猜一個數字"))
    if guess>answer:
        b=guess
        print("呵呵呵好大喔 太大了啦!")
    elif guess<answer:
        a=guess
        print("哈哈哈太小了啦 太小了!")
    else:
        print("這樣都被你猜到 哇賽")
        break
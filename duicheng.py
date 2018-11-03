# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 08:09:47 2017

@author: Arock
"""
import turtle
def hua_xin(x,y,D_cir,jiaodu):#画星星，参数有坐标x,y，星星的外接圆直径，偏角
    leng=D_cir*4/5#大致计算
    turtle.penup()#抬起笔
    turtle.pencolor('red')#规定画笔的颜色
    turtle.goto(x,y)#跳到特定的坐标位置
    turtle.pendown()#放下画笔
    turtle.left(jiaodu)#修正偏角
    turtle.fill(True)#填充颜色
    for i in range(5):#for循环画星
        turtle.forward(leng)
        turtle.right(144)#修正偏角
    turtle.fillcolor('red')#填充颜色
    turtle.fill(False)

turtle.goto(0,0)#跳到指定位置
turtle.fill(True)#填充颜色
turtle.fillcolor('yellow')#填充红色
for i in range(2):#开始画矩形
    turtle.forward(300)
    turtle.right(270)
    turtle.forward(200)
    turtle.right(270)
turtle.fill(False)
hua_xin(125,100,60,0)
hua_xin(50,50,60,30)
hua_xin(200,50,60,0)
hua_xin(50,150,60,30)
hua_xin(200,150,60,0)

#นี่คือตัวอย่างโปรแกรมเต่า
import turtle
tao = turtle.Pen() #สร้างตัวเต่าขึ้นมา
tao.shape('turtle') #แปลงร่างลูกศรให้กลายเป็นเต่า
import random

# ctrl + { คือแท็บถอยหลัง (ctrl + บ)

def Rect(x,y,size=30,clr='black'):
    tao.penup() #ยกปากกาขึ้น
    tao.goto(x,y) #เดินไปตามตำแหน่ง
    tao.color(clr) #เปลี่ยนสี
    tao.pendown() #เอาปากกาลง
    #--------วาดสี่เหลี่ยม---------
    for i in range(4):
        tao.forward(size)
        tao.left(90)
    #--------------------------
    tao.penup()#ยกปากกาขึ้น

#########รันโปรแกรมด้านล่างนี้#########
for i in range(10):
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    print(x,y)
    Rect(x,y,40,'green')

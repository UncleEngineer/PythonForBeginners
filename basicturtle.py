#นี่คือตัวอย่างโปรแกรมเต่า
import turtle
import random
tao = turtle.Pen() #สร้างตัวเต่าขึ้นมา
tao.shape('turtle') #แปลงร่างลูกศรให้กลายเป็นเต่า

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
allcolor = ['red','green','blue','orange']

count = int(input('อยากได้สี่เหลี่ยมเท่าไร?: '))
#รับจำนวนจาก user ว่าต้องการจำนวนเท่าไร

for i in range(count):
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    print(x,y)
    select_color = random.choice(allcolor)
    Rect(x,y,40,select_color)





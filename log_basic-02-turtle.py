Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> tao = turtle.Pen()
>>> tao.shape('turtle')
>>> tao.forward(50)
>>> tao.left(90)
>>> tao.right(45)
>>> tao.left(45)
>>> tao.forward(50)
>>> tao.left(90)
>>> tao.forward(50)
>>> tao.left(90)
>>> tao.forward(50)
>>> tao.left(90)
>>> tao.left(180)
>>> tao.reset()
>>> for i in range(5):
	print(i)

	
0
1
2
3
4
>>> for i in range(4):
	print(i)

	
0
1
2
3
>>> range(5)
range(0, 5)
>>> list(range(5))
[0, 1, 2, 3, 4]
>>> for i in [50,60,70]:
	print(i)

	
50
60
70
>>> print(i)
70
>>> for i in range(4):
	print('เดินครั้งที่',i)
	tao.forward(50)
	tao.left(90)

	
เดินครั้งที่ 0
เดินครั้งที่ 1
เดินครั้งที่ 2
เดินครั้งที่ 3
>>> tao.goto(-100,100)
>>> tao.reset()
>>> tao.penup()
>>> tao.goto(-100,100)
>>> for i in range(4):
	print('เดินครั้งที่',i)
	tao.forward(50)
	tao.left(90)

	
เดินครั้งที่ 0
เดินครั้งที่ 1
เดินครั้งที่ 2
เดินครั้งที่ 3
>>> tao.pendown()
>>> for i in range(4):
	print('เดินครั้งที่',i)
	tao.forward(50)
	tao.left(90)

	
เดินครั้งที่ 0
เดินครั้งที่ 1
เดินครั้งที่ 2
เดินครั้งที่ 3
>>> for i in range(4):
	print('เดินครั้งที่',i)
	tao.forward(50)
	tao.left(90)

	
เดินครั้งที่ 0
เดินครั้งที่ 1
เดินครั้งที่ 2
เดินครั้งที่ 3
>>> tao.clear()
>>> for i in range(4):
	print('เดินครั้งที่',i)
	tao.forward(50)
	tao.left(90)

	
เดินครั้งที่ 0
เดินครั้งที่ 1
เดินครั้งที่ 2
เดินครั้งที่ 3
>>> tao.reset()
>>> def Rect():
	for i in range(4):
		tao.forward(50)
		tao.left(90)

		
>>> Rect()
>>> clear()
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    clear()
NameError: name 'clear' is not defined
>>> tao.clear()
>>> tao.goto(100,100)
>>> Rect()
>>> tao.reset()
>>> def Rect():
	tao.pendown()
	for i in range(4):
		tao.forward(50)
		tao.left(90)
	tao.penup()

	
>>> Rect()
>>> tao.reset()
>>> tao.goto(100,100)
>>> tao.reset()
>>> tao.penup()
>>> tao.goto(100,100)
>>> Rect()
>>> tao.goto(-100,-100)
>>> Rect()
>>> tao.goto(50,-100)
>>> Rect()
>>> print('วาดสี่เหลี่ยมโดยใส่ขนาดสี่เหลี่ยมได้')
วาดสี่เหลี่ยมโดยใส่ขนาดสี่เหลี่ยมได้
>>> print('กำหนดตำแหน่งที่ต้องการวิ่งไปได้')
กำหนดตำแหน่งที่ต้องการวิ่งไปได้
>>> print('เลือกสีได้')
เลือกสีได้
>>> tao.reset()
>>> Rect()
>>> tao.reset()
>>> rect()
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    rect()
NameError: name 'rect' is not defined
>>> def Rect(size):
	tao.pendown()
	for i in range(4):
		tao.forward(size)
		tao.left(90)
	tao.penup()

	
>>> Rect(30)
>>> tao.goto(-100,-100)
>>> Rect(200)
>>> Rect()
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    Rect()
TypeError: Rect() missing 1 required positional argument: 'size'
>>> def Rect(size=30):
	tao.pendown()
	for i in range(4):
		tao.forward(size)
		tao.left(90)
	tao.penup()

	
>>> Rect()
>>> Rect(100)
>>> Rect(120)
>>> tao.reset()
>>> for sz in [30,50,80]:
	Rect(sz)

	
>>> tao.reset()
>>> for sz in [30,50,80,40,100,200]:
	Rect(sz)

	
>>> def Rect(x,y,size=30):
	tao.penup()
	tao.goto(x,y)
	tao.pendown()
	for i in range(4):
		tao.forward(size)
		tao.left(90)
	tao.penup()

	
>>> tao.reset()
>>> Rect(100,100)
>>> for i in range(5):
	print(i)

	
0
1
2
3
4
>>> def Rect(x,y,size=30,clr='black'):
	tao.penup()
	tao.goto(x,y)
	tao.color(clr)
	tao.pendown()
	for i in range(4):
		tao.forward(size)
		tao.left(90)
	tao.penup()

	
>>> Rect(150,150,40,'green')
>>> 
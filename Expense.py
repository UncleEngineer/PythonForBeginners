# Expense.py

from tkinter import *
from tkinter import ttk # theme of tk
# tkinter คือ library ที่ใช้สร้าง GUI

GUI = Tk() #หน้าต่างหลักของโปรแกรม
GUI.geometry('800x500') #ปรับขนาดหน้าจอโปรแกรม
GUI.title('โปรแกรมบันทึกค่าใช้จ่าย')

FONT1 = (None,15)
FONT2 = ('Angsana New',20,'bold')

###############################




F1 = Frame(GUI)
F1.place(x=50,y=50)

# Label (ข้อความแสดงผล)
L1 = ttk.Label(F1,text='รายการค่าใช้จ่าย',font=FONT2)
L1.pack(pady=5)

# ช่องกรอกช่องที่ 1
v_namelist = StringVar() # StringVar คือ ตัวแปรพิเศษใช้กับ GUI เท่านั้น 
E1 = ttk.Entry(F1,textvariable=v_namelist,font=FONT1)
E1.pack(pady=5)

###############################
# Label (ข้อความแสดงผล)
L2 = ttk.Label(F1,text='ค่าใช้จ่าย (บาท)',font=FONT2)
L2.pack(pady=5)

# ช่องกรอกช่องที่ 2
v_price = StringVar() # StringVar คือ ตัวแปรพิเศษใช้กับ GUI เท่านั้น 
E2 = ttk.Entry(F1,textvariable=v_price,font=FONT1)
E2.pack(pady=5)

###############################

def SaveData():
	namelist = v_namelist.get() # .get() ดึงข้อมูลจากช่องกรอกที่ชื่อว่า v_namelist
	price = v_price.get()
	textshow = 'ค่าใช้จ่าย: {} ราคา: {} บาท'.format(namelist,price)
	v_result.set(textshow)


B1 = ttk.Button(F1,text='Save',command=SaveData)
B1.pack(ipadx=20,ipady=10,pady=5)

###############################
v_result = StringVar()
v_result.set('---------RESULT---------')
R1 = ttk.Label(F1,textvariable=v_result,font=FONT2,foreground='green')
R1.pack()


GUI.mainloop()
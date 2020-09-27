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
# Label (ข้อความแสดงผล)
L1 = ttk.Label(GUI,text='รายการค่าใช้จ่าย',font=FONT2)
L1.pack(pady=5)

# ช่องกรอกช่องที่ 1
v_namelist = StringVar() # StringVar คือ ตัวแปรพิเศษใช้กับ GUI เท่านั้น 
E1 = ttk.Entry(GUI,textvariable=v_namelist,font=FONT1)
E1.pack(pady=5)

###############################
# Label (ข้อความแสดงผล)
L2 = ttk.Label(GUI,text='ค่าใช้จ่าย (บาท)',font=FONT2)
L2.pack(pady=5)

# ช่องกรอกช่องที่ 1
v_price = StringVar() # StringVar คือ ตัวแปรพิเศษใช้กับ GUI เท่านั้น 
E2 = ttk.Entry(GUI,textvariable=v_price,font=FONT1)
E2.pack(pady=5)

###############################
B1 = ttk.Button(GUI,text='Save')
B1.pack(ipadx=20,ipady=10,pady=5)

GUI.mainloop()
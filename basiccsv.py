# basiccsv.py

import csv
from datetime import datetime

def WriteCSV(data):
	# 'a' is append , 'w' is replace
	dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S') #strftime.org
	data.insert(0,dt) #ใส่วันที่ลงไปหน้าข้อความทุกครั้งที่บันทึก
	with open('data.csv','a',newline='',encoding='utf-8') as file:
		fw = csv.writer(file) # fw is file writer
		fw.writerow(data)
	print('Done!')


def ReadCSV():
	with open('data.csv',newline='',encoding='utf-8') as file:
		fr = csv.reader(file) # file reader
		data = list(fr)

	return data

alldata = ReadCSV()
#print(alldata)

for dt in alldata:
	print(dt)


# product = ['แอปเปิ้ล',20]
# WriteCSV(product)
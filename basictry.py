# basictry.py
try:
    money = int(input('กรุณากรอกเงินเดือน:'))
    print('คุณมีเงินเดือน: {:,d} บาท'.format(money))
except Exception as e:
    print('ERROR:',e)
else:
    # จุด else จะทำงานก็ต่อเมื่อ ใน try: ไม่มี error
    print('คุณได้โบนัส 10 เท่า: {} บาท'.format(money * 10))

print('Finish')

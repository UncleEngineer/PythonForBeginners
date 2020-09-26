money = 3000
expense = [100,200,2000]

money = money - sum(expense)
print(f'ตอนนี้ฉันเหลือเงิน {money} บาท')
if money >= 200:
    print('ไปกินอาหารญี่ปุ่นกัน')
elif money >= 100:
    print('ไปกิน KFC')
else:
    print('ไปกินข้าวราดแกง')

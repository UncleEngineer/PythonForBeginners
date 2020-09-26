money = 99
print(f'จำนวนเงินของคุณ: {money:,.2f} บาท' )
transfer = float(input('กรุณากรอกเงินที่ต้องการโอน: '))
#print('check ',money < transfer)
running = True

while money < transfer:
    print('จำนวนเงินของคุณไม่พอ')
    print(f'จำนวนเงินของคุณ: {money:,.2f} บาท' )
    print('-------------')
    print('กด [1] ฝากเงินเข้า')
    print('กด [2] กรอกยอดโอนใหม่')
    print('กด [3] ออกจากระบบ')
    menu = input('กรุณาเลือกเมนูที่ต้องการ: ')
    if menu == '1':
        get = float(input('ฝากเงินกี่บาท: '))
        money = money + get # money += get
    elif menu == '2':
        transfer = float(input('กรอกยอดโอนใหม่: '))
    else:
        running = False
        break       
    print('-------------')

if running == True:
    print(f'โอนเงิน: {transfer:,.2f} บาทเรียบร้อยแล้ว')
    money = money - transfer
    print(f'ยอดเงินคงเหลือ: {money:,.2f} บาท' )
else:
    print('คุณได้ยกเลิกการโอน')

    

# bot-songline.py

# การใช้งานโปรแกรมส่งไลน์
# 1-ออก token เว็บไซต์ https://notify-bot.line.me/my/
# 2-กด generate token > ตั้งชื่อบ็อท > เลือกกลุ่ม > generate token
# 3-เปิด cmd/terminal > pip install songline
# 4-พิมพ์ตามโค้ดด้านล่างนี้


from songline import Sendline

token = 'WHnwgNxrI29Od6jCMfjGYsZGXyD8YMNj4xmEFOl55qK'

messenger = Sendline(token)

#messenger.sendtext('สวัสดีจ้าาาาา')
#messenger.sticker(100,1)
messenger.sendimage('https://s359.kapook.com/pagebuilder/04761904-54c7-46ed-aba3-72ae8eebcd9e.png')

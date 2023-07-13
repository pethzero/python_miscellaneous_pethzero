import os

# เปลี่ยนเส้นทางไปยังไดเรกทอรีที่มีไฟล์ "old.txt" และ "new.txt"
os.chdir('D:\\DATA\\CTG\\STOCK\\')
# อ่านไฟล์เดิม
number = 41  # ตัวเริ่มต้นของตัวเลข
data = [
    'ม.',
    'หลอด',
    'กรง',
    'ตร.ฟ.',
    'รู',
    'วง',
    'm.',
    'ea.',
    'pc.',
    'เหมา',
    'กอ',
    'กระถาง',
    'หน่อ',
    'กระสอบ',
    'ไม้',
    'ไลน์ท่อ',
    'เที่ยว'
]
output_filename = 'unitnew.txt'  # ชื่อไฟล์ที่ต้องการสร้างและเขียนข้อมูล

with open(output_filename, 'w') as output_file:
    for item in data:
        output_file.write(f'INSERT INTO invent (RECNO, UNITNAME) VALUES (NEXT VALUE FOR GEN_LISTUNIT, [] )\n')  # เขียนข้อมูลลงในไฟล์ใหม่
        number += 1  # เพิ่มตัวเลขขึ้นไปทีละหนึ่งเพื่อใช้ในการเขียนบรรทัดถัดไป



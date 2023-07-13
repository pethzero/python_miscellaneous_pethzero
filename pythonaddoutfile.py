import os

# เปลี่ยนเส้นทางไปยังไดเรกทอรีที่มีไฟล์ "old.txt" และ "new.txt"
os.chdir('D:\\DATA\\CTG\\STOCK\\')
# อ่านไฟล์เดิม
number = 238  # ตัวเริ่มต้นของตัวเลข
filename = 'unitold.txt'  # ชื่อไฟล์ที่มีข้อมูลตัวอักษร
output_filename = 'unitnew.txt'  # ชื่อไฟล์ที่ต้องการสร้างและเขียนข้อมูล

with open(filename, 'r', encoding='utf-8') as input_file, open(output_filename, 'w', encoding='utf-8') as output_file:
    for line in input_file:
        line = line.strip()  # ลบช่องว่างหรือตัวขึ้นบรรทัดในท้ายสตริง
        output_file.write(f"{number} '{line}' \n")  # เขียนข้อมูลลงในไฟล์ใหม่
        number += 1  # เพิ่มตัวเลขขึ้นไปทีละหนึ่งเพื่อใช้ในการเขียนบรรทัดถัดไป
import os
from io import open

# ข้อความที่ต้องการเขียน
text = "You Got New Weapon"

# ระบุชื่อไฟล์และที่อยู่ของไฟล์ที่ต้องการสร้างหรือแก้ไข
file_path = "output.txt"

# เปิดไฟล์เพื่อเขียนข้อมูล
with open(file_path, "w", encoding="utf-8") as file:
    file.write(text)

print("เขียนข้อมูลลงในไฟล์เรียบร้อยแล้ว:", file_path)
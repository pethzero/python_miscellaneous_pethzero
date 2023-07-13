import pandas as pd
import os

# อ่านไฟล์ Excel
df = pd.read_excel('DATA.xlsx')
# print(df)

# ดึงข้อมูล RECNO และ BarCode
# recno_barcode_df = df[['RECNO', 'BARCODE']]
# # แสดงผลลัพธ์
# print(recno_barcode_df)


# ใช้ลูป for เพื่อสร้างข้อความ
# for index, row in df.iterrows():
#     recno = int(row['RECNO'])
#     barcode =  str(int(row['RECNO'])).zfill(8)
#     print(f"RECNO {recno} BARCODE {barcode}")

with open('output.txt', 'w') as file:
    # ใช้ลูป for เพื่อสร้างข้อความ
    for index, row in df.iterrows():
        recno = int(row['RECNO'])
        barcode =  str(int(row['RECNO'])).zfill(8)
        line = f"UPDATE invent SET BARCODE = '{barcode}' WHERE RECNO = {recno};\n"
        file.write(line)
# อ่านไฟล์ CSV
# df = pd.read_csv('DATA.csv')
# print(df.to_string())
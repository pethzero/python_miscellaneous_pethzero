import os

# เปลี่ยนเส้นทางไปยังไดเรกทอรีที่มีไฟล์ "old.txt" และ "new.txt"
os.chdir('D:\\DATA\\CTG\\STOCK\\')

# number = 3223  # จำนวนบรรทัดที่ต้องการ
# number_count = 1811 Part2

# number = 52
# number_count = 5034


number = 53
number_count = 1758 #1810
# message = "INSERT INTO invent (RECNO, INVTYPE, CODE, PRODNAME ,LISTUNIT , WAGEAMT) VALUES (NEXT VALUE FOR GEN_INVENT, 0, '', '', 0,0);"  # ข้อความที่ต้องการใส่ในแต่ละบรรทัด
output_filename = "callupdate_part1.txt"  # ชื่อไฟล์ที่ต้องการสร้างและเขียนข้อมูล

with open(output_filename, "w", encoding='utf-8') as output_file:
    for i in range(number):
        # output_file.write(f"UPDATE invent SET PRODNAME='' ,  QUAN=0,SALEAMT=0 WHERE RECNO = '{number_count+i}';\n")
          # output_file.write(f"UPDATE invent SET QUAN=0,SALEAMT=0 WHERE RECNO = '{number_count+i}';\n")
        # output_file.write(f"UPDATE invent SET CALLNAME=PRODNAME WHERE RECNO = '{number_count+i}';\n")
        # output_file.write(f"{number_count+i}\n")
        output_file.write(f"UPDATE invent SET SALEAMT=0 ,WAGEAMT=0 ,COSTAMT=0 WHERE RECNO = '{number_count+i}';\n")
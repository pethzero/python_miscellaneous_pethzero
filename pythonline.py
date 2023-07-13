import os
# อ่านไฟล์เดิม
# os.chdir('กรณีไฟลเลือกไฟล์')
num_lines = 238
  # ระบุจำนวนบรรทัดที่ต้องการในไฟล์

# insert_statement = "INSERT INTO invent (RECNO, INVTYPE, CODE ,LISTUNIT) VALUES (NEXT VALUE FOR GEN_INVENT, 32, '', 9);\n"
insert_statement ='get \n"'
with open("output.txt", 'w') as file:
    file.writelines([insert_statement] * num_lines)
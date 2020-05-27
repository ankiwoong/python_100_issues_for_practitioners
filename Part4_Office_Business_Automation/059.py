import openpyxl
import os

# 예제 024에서 저장한 Excel 파일 경로 지정
cwd = os.getcwd()
filename = "df.xlsx"
filepath = os.path.join(cwd, "output", filename)

wb = openpyxl.load_workbook(filepath)
ws = wb['Sheet1']

# 열(columns), 행(rows) 객체
cols = tuple(ws.columns)
rows = tuple(ws.rows)

print(cols[0])
print(rows[0])

for col_idx, col in enumerate(cols):
    for each_cell in col:
        print("%s번째 열: %s" % (col_idx, each_cell))

a3 = cols[0][2]
print(a3.value)
a3.value = 'row1'
print(a3.value)

# 워크북의 변경내용을 새로운 파일에 저장
wb.save(os.path.join(cwd, "output", "df3.xlsx"))

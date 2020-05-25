import pandas as pd

# 예제 015에서 저장한 CSV 파일명을 경로와 함께 지정
csv_file = './data/bok_statistics_CD.csv'

# read_csv() 함수로 데이터프레임 변환
df1 = pd.read_csv(csv_file)
print(df1)
print('\n')

df2 = pd.read_csv(csv_file, header=None)  # header=None 옵션
print(df2)
print('\n')

df3 = pd.read_csv(csv_file, index_col=0)  # index_col=0 옵션
print(df3)
print('\n')

# header=None, index_col=0 옵션
df4 = pd.read_csv(csv_file, index_col=0, header=None)
print(df4)
print('\n')

# 예제 014에서 다운로드 폴더에 저장한 Excel 파일을 data 폴더에 이동하여 저장
excel_file = './data/report_Key100Stat.xls'

# read_excel() 함수로 데이터프레임 변환
df5 = pd.read_excel(excel_file)
print(df5)

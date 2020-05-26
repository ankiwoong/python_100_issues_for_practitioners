import pandas as pd

# dictionary를 데이터프레임으로 변환
dict_data = {'c0': [1, 2, 3], 'c1': [4, 5, 6]}
df = pd.DataFrame(dict_data, index=['r0', 'r1', 'r2'])
print(df, '\n')

# 데이터프레임을 CSV 파일로 저장
df.to_csv('./output/df.csv')

# 데이터프레임을 Excel 파일로 저장
df.to_excel('./output/df.xlsx')

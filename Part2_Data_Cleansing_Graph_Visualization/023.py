import pandas as pd

# dictionary를 데이터프레임으로 변환
dict_data = {'c0': [1, 2, 3], 'c1': [4, 5, 6]}
df = pd.DataFrame(dict_data, index=['r0', 'r1', 'r2'])
print(df, "\n")

# 원소 선택
el_01 = df.iloc[0, 1]
print(el_01, "\n")

el_11 = df.iloc[1, 1]
print(el_11, "\n")

el_21 = df.loc['r2', 'c1']
print(el_21, "\n")

el_12_01 = df.loc['r1':'r2', 'c0':'c1']
print(el_12_01, "\n")

el_12_01_iloc = df.iloc[1:3, 0:2]
print(el_12_01, "\n")

# 원소값 변경
df.iloc[0, 1] = 40
print(df, "\n")

df.iloc[1:3, 0:2] = 0
print(df)

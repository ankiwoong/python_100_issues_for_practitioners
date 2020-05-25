import pandas as pd

# dictionary를 데이터프레임으로 변환
dict_data = {'c0': [1, 2, 3], 'c1': [4, 5, 6]}
df = pd.DataFrame(dict_data, index=['r0', 'r1', 'r2'])
print(df, "\n")

# 열 선택
col0 = df['c0']
col1 = df.c1

print(col0, "\n")
print(col1, "\n")

# 열 추가
df['c2'] = 7, 8, 9
print(df, "\n")

df['c3'] = 0
print(df, "\n")

df['c4'] = df['c3']
print(df, "\n")

# 열 변경
df['c3'] = 10, 11, 12
print(df, "\n")

df['c3'] = 0
print(df, "\n")

# 열 삭제
df.drop('c4', axis=1, inplace=True)
print(df, "\n")

df.drop(['c1', 'c3'], axis=1, inplace=True)
print(df)

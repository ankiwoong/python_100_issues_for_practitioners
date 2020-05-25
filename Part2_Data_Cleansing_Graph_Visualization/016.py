import pandas as pd

# dictionary를 데이터프레임으로 변환
dict_data = {'c0': [1, 2, 3, 4, 5], 'c1': [6, 7, 8, 9, 10]}
df1 = pd.DataFrame(dict_data)
print(type(df1), "\n")
print(df1, "\n")

# 행 이름 지정
df2 = pd.DataFrame(dict_data, index=['r0', 'r1', 'r2', 'r3', 'r4'])
print(df2, "\n")

# list of list를 데이터프레임으로 변환
list_of_list_data = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
df3 = pd.DataFrame(list_of_list_data)
print(df3, "\n")

# 행 이름, 열 이름 지정
df4 = pd.DataFrame(list_of_list_data,
                   index=['r0', 'r1'],
                   columns=['c0', 'c1', 'c2', 'c3', 'c4'])
print(df4, "\n")

# 데이터프레임의 형태 확인
print(df2.shape)
print(df4.shape)

import pandas as pd

# 예제 17의 CSV 파일을 다시 활용하여, 데이터프레임으로 변환
df = pd.read_csv('./data/bok_statistics_CD.csv',
                 header=None)       # heeader=None 옵션

print(df.head())
print('\n')
print(df.head(3))
print('\n')
print(df.tail())
print('\n')
print(df.tail(3))

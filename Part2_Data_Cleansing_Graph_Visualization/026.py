import pandas as pd
from matplotlib import pyplot as plt                    # 추가

# 예제 025에서 저장한 CSV 파일을 불러와서 데이터프레임으로 변환
df = pd.read_csv('./data/bok_statistics_CD_2.csv', header=0, index_col=0)
print(df.head())
print('\n')

# 막대 그래프 그리기
df.plot(kind='bar')
plt.savefig('./output/9번 라인.png', dpi=300)          # 파일 저장 / 추가

df['CD_rate'].plot(kind='bar')
plt.savefig('./output/11번 라인.png', dpi=300)          # 파일 저장 / 추가

df['change'].plot(kind='bar')
plt.savefig('./output/12번 라인.png', dpi=300)          # 파일 저장 / 추가

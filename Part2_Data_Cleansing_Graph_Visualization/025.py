import pandas as pd
from matplotlib import pyplot as plt                    # 추가

# 예제 017의 CSV 파일을 다시 활용하여, 데이터프레임으로 변환
df = pd.read_csv('./data/bok_statistics_CD.csv', header=None)
print(df.head())
print('\n')

df.columns = ['year', 'CD_rate', 'change']  # 열 이름 변경
df.set_index('year', inplace=True)   # year 열을 행 인덱스로 설정
print(df.head())
df.to_csv('./data/bok_statistics_CD_2.csv')
print('\n')

# 선 그래프 그리기
df.plot()
plt.savefig('./output/15번 라인.png', dpi=300)          # 파일 저장 / 추가

df['CD_rate'].plot()
plt.savefig('./output/17번 라인.png', dpi=300)          # 파일 저장 / 추가

df['change'].plot()
plt.savefig('./output/18번 라인.png', dpi=300)          # 파일 저장 / 추가

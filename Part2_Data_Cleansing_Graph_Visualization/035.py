import matplotlib.pyplot as plt
import seaborn as sns

# Seaborn 제공 데이터셋 가져오기
df = sns.load_dataset('iris')
print(df.head())
print("\n")
print(df.columns.values)

# 상관계수를 구해서 히트맵으로 그리기
plt.figure(figsize=(10, 10))
corr = df.loc[:, 'sepal_length':'petal_width'].corr()

# 히트맵 그리기
sns.set(font_scale=1.5)
sns.heatmap(corr,
            annot=True,
            cmap='PuBuGn',
            fmt='.1f',
            square=True,
            linewidth=0.5,
            cbar=False)

# plt.show()
plt.savefig('./output/히트맵.png')

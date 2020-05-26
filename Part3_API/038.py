from pytrends.request import TrendReq
import matplotlib.pyplot as plt
import os

# 검색 keyword, 검색 기간 입력
keyword = "WTO"
period = "now 7-d"  # 검색기간: 최근 7일

# Google Trend 접속
trend_obj = TrendReq()
trend_obj.build_payload(kw_list=[keyword], timeframe=period)

# 지역별 검색 Trend 비교
trend_df = trend_obj.interest_by_region().sort_values(by='WTO', ascending=False)
print(trend_df.head())

# 그래프 출력
plt.style.use("ggplot")
plt.figure(figsize=(14, 10))
trend_df.iloc[:50, :][keyword].plot(kind='bar')
plt.title("Google Trends by Region", size=15)
plt.legend(labels=[keyword], loc="upper right")

# 그래프 파일 저장
cwd = os.getcwd()
output_filepath = os.path.join(
    cwd, "output", "google_trend_by_region_%s.png" % keyword)
plt.savefig(output_filepath, dpi=300)
plt.show()

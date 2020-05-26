from pytrends.request import TrendReq
import matplotlib.pyplot as plt
import os

# 검색 keyword, 검색 기간 입력
keyword = "Galaxy Fold"
period = "today 3-m"  # 검색기간: 최근 3개월

# Google Trend 접속
trend_obj = TrendReq()
trend_obj.build_payload(kw_list=[keyword], timeframe=period)

# 시간에 따른 Trend 변화
trend_df = trend_obj.interest_over_time()
print(trend_df.head())

# 그래프 출력
plt.style.use("ggplot")
plt.figure(figsize=(14, 5))
trend_df[keyword].plot()
plt.title("Google Trends over time", size=15)
plt.legend(labels=[keyword], loc="upper right")

# 그래프 파일 저장
cwd = os.getcwd()
output_filepath = os.path.join(
    cwd, "output", "google_trend_over_time_%s.png" % keyword)
plt.savefig(output_filepath, dpi=300)
plt.show()

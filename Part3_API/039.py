from pytrends.request import TrendReq
import matplotlib.pyplot as plt
import os

# 검색 keyword, 검색 기간 입력
keyword1 = "apple iphone"
keyword2 = "samsung galaxy"
period = "today 5-y"  # 검색기간: 최근 5년

# Google Trend 접속 및 데이터 탑재
trend_obj = TrendReq()
trend_obj.build_payload(
    kw_list=[keyword1, keyword2], timeframe=period)  # kw_list: 최대 5개
trend_df = trend_obj.interest_over_time()

# 그래프 출력
plt.style.use("ggplot")
plt.figure(figsize=(14, 5))
trend_df[keyword1].plot()
trend_df[keyword2].plot()
plt.title("Google Trends: %s vs. %s" % (keyword1, keyword2), size=15)
plt.legend(loc="best")

# 그래프 파일 저장
cwd = os.getcwd()
output_filepath = os.path.join(
    cwd, "output", 'google_trend_%s_vs_%s.png' % (keyword1, keyword2))
plt.savefig(output_filepath, dpi=300)
plt.show()

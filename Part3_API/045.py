import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime as dt

# DART 전자공시 사이트 APT 인증키 입력
crtfc_key = "d691b6402660bb64db89e7e06ef636ccdf879e01"

# 검색기간 설정하기
now = dt.datetime.now()
search_period = dt.timedelta(days=30)
now_date = now.strftime('%Y%m%d')
bgn_de = (now-search_period).strftime('%Y%m%d')
page_count = 10

# DART 상세점보 접속 URL
corp_code = "00126380"
url = "https://opendart.fss.or.kr/api/list.xml?crtfc_key=" + crtfc_key + "&corp_code=" + corp_code\
      + "&page_count=" + str(page_count) + "&bgn_de=" + bgn_de


# BeautifulSoup으로 API가 반환하는 XML 해석하여 dataframe으로 정리
xml = requests.get(url)
soup = BeautifulSoup(xml.text, 'html.parser')
print(str(soup)[:500])

search_result = pd.DataFrame()
items = soup.find_all('list')
print(len(items))

for item in items:
    temp_dataframe = pd.DataFrame(([[item.corp_code.text, item.corp_name.text, item.stock_code.text,
                                     item.report_nm.text, item.rcept_no.text, item.flr_nm.text,
                                     item.rcept_dt.text, item.rm.text]]),
                                  columns=["corp_code", "corp_name", "stock_code", "report_nm", "rcept_no", "flr_nm", "rcept_dt", "rm"])
    search_result = pd.concat([search_result, temp_dataframe])

print(search_result)

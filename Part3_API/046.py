import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime as dt

# DART 전자공시 사이트 APT 인증키 입력
crtfc_key = "d691b6402660bb64db89e7e06ef636ccdf879e01"

# 검색기간 설정하기
now = dt.datetime.now()
search_period = dt.timedelta(days=5)
now_date = now.strftime('%Y%m%d')
start_date = (now-search_period).strftime('%Y%m%d')
page_set = 10

# DART 상세점보 접속 URL
pdt_list = [
    "D001",  # 주식등의대량보유상황보고서
    "D002",  # 임원ㆍ주요주주특정증권등소유상황보고서
    "D003",  # 의결권대리행사권유
    "D004",  # 공개매수
]

pdt_urls = []

for pdt in pdt_list:
    url = "https://opendart.fss.or.kr/api/list.xml?crtfc_key="+crtfc_key +\
        "&page_count="+str(page_set)+"&bgn_de=" + \
        start_date+"&pblntf_detail_ty="+pdt
    pdt_urls.append(url)

# BeautifulSoup으로 API가 반환하는 XML 해석하여 dataframe으로 정리

sum_items = []

for url in pdt_urls:
    xml = requests.get(pdt_urls[1])
    soup = BeautifulSoup(xml.text, 'html.parser')
    items = soup.find_all('list')
    sum_items += items

print(len(sum_items))

search_result = pd.DataFrame()

for item in sum_items:
    temp_dataframe = pd.DataFrame(([[item.corp_cls.text, item.corp_name.text, item.stock_code.text,
                                     item.report_nm.text, item.rcept_no.text, item.flr_nm.text,
                                     item.rcept_dt.text, item.rm.text]]),
                                  columns=["corp_cls", "corp_name", "stock_code", "report_nm", "rcept_no", "flr_nm", "rcept_dt", "rm"])
    search_result = pd.concat([search_result, temp_dataframe])

print(search_result.head())

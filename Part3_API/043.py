import requests
from bs4 import BeautifulSoup

# DART 전자공시 사이트 APT 인증키 입력
<<<<<<< HEAD
crtfc_key = ""
=======
crtfc_key = "d691b6402660bb64db89e7e06ef636ccdf879e01"
>>>>>>> 8bacb8a556b39618228a86c7731d553fde9536c6

# 기업개황 정보 접속 URL
corp_code = "00126380"
url = 'https://opendart.fss.or.kr/api/company.xml?crtfc_key=' + \
    crtfc_key + '&corp_code=' + corp_code
# BeautifulSoup으로 API가 반환하는 XML 확인
xml = requests.get(url)
soup = BeautifulSoup(xml.text, 'html.parser')
print(soup)

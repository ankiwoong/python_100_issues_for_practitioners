import requests
from bs4 import BeautifulSoup

# DART 전자공시 사이트 APT 인증키 입력
crtfc_key = "d691b6402660bb64db89e7e06ef636ccdf879e01"

# 기업개황 정보 접속 URL
corp_code = "00126380"
url = "https://opendart.fss.or.kr/api/company.xml?crtfc_key=" + \
    crtfc_key + "&corp_code=" + corp_code

# BeautifulSoup으로 API가 반환하는 XML 해석하여 dataframe으로 정리
xml = requests.get(url)
soup = BeautifulSoup(xml.text, 'html.parser')

corp_name = soup.find('corp_name').text
corp_name_eng = soup.find('corp_name_eng').text
stock_name = soup.find('stock_name').text
stock_code = soup.find('stock_code').text
ceo_nm = soup.find('ceo_nm').text
corp_cls = soup.find('corp_cls').text
jurir_no = soup.find('jurir_no').text
bizr_no = soup.find('bizr_no').text
adres = soup.find('adres').text
hm_url = soup.find('hm_url').text
ir_url = soup.find('ir_url').text
phn_no = soup.find('phn_no').text
fax_no = soup.find('fax_no').text
induty_code = soup.find('induty_code').text
est_dt = soup.find('est_dt').text
acc_mt = soup.find('acc_mt').text

company_info = {'corp_name': corp_name,
                'corp_name_eng': corp_name_eng,
                'stock_name': stock_name,
                'stock_code': stock_code,
                'ceo_nm': ceo_nm,
                'corp_cls': corp_cls,
                'jurir_no': jurir_no,
                'bizr_no': bizr_no,
                'adres': adres,
                'hm_url': hm_url,
                'ir_url': ir_url,
                'phn_no': phn_no,
                'fax_no': fax_no,
                'induty_code': induty_code,
                'est_dt': est_dt,
                'acc_mt': acc_mt,
                }

print(company_info)

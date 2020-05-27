from mailmerge import MailMerge
import os
from datetime import datetime as dt
import pandas as pd

# MS Word 템플릿 파일 불러오기
cwd = os.getcwd()
template_filename = "fax_cover_template.docx"
template_filepath = os.path.join(cwd, "data", template_filename)

# 템플릿 파일로 메일머지(mail-merge) 객체 만들기
document = MailMerge(template_filepath)

# 수신자 정보 불러오기 - MS Excel 파일
respondents_filename = "fax_respondents_list.xlsx"
respondents_filepath = os.path.join(cwd, "data", respondents_filename)

respondents = pd.read_excel(respondents_filepath)   # 판다스 dataframe 변환

respondents_list = []
today = '%s년 %s월 %s일' % (dt.now().year, dt.now().month, dt.now().day)

for index in respondents.index:
    new_respondent = {}
    new_respondent['name'] = respondents.loc[index, 'name']
    new_respondent['fax'] = respondents.loc[index, 'fax']
    new_respondent['phone'] = respondents.loc[index, 'phone']
    new_respondent['date'] = today
    new_respondent['title'] = respondents.loc[index, 'title']
    new_respondent['memo'] = respondents.loc[index, 'memo']
    respondents_list.append(new_respondent)

# 수신자 리스트를 메일머지 객체에 전달
document.merge_pages(respondents_list)

# 메일머지 객체를 MS Word 문서로 저장하기
output_filepath = os.path.join(
    cwd, "output", "fax_cover_output_multi_pages_excel_data.docx")
document.write(output_filepath)

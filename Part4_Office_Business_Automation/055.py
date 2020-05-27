from mailmerge import MailMerge
import os
from datetime import datetime as dt

# MS Word 템플릿 파일 불러오기
cwd = os.getcwd()
template_filename = "fax_cover_template.docx"
template_filepath = os.path.join(cwd, "data", template_filename)

# 템플릿 파일로 메일머지(mail-merge) 객체 만들기
document = MailMerge(template_filepath)

# 수신자 정보 입력 - 딕셔너리 형태
respondent1 = {
    'name': '이수민',
    'fax': '031-777-7777',
    'phone': '031-777-7700',
    'date': '%s년 %s월 %s일' % (dt.now().year, dt.now().month, dt.now().day),
    'title': '세금계산서 재발행 요청의 건',
    'memo': '2019년 8월분',
}

respondent2 = {
    'name': '박솔',
    'fax': '032-333-0007',
    'phone': '032-333-0800',
    'date': '%s년 %s월 %s일' % (dt.now().year, dt.now().month, dt.now().day),
    'title': '견적 문의',
    'memo': '공급 예정일 포함',
}

# 수신자 리스트를 메일머지 객체에 전달
respondents_list = [respondent1, respondent2]
document.merge_pages(respondents_list)

# 메일머지 객체를 MS Word 문서로 저장하기
output_filepath = os.path.join(
    cwd, "output", "fax_cover_output_multi_pages.docx")
document.write(output_filepath)

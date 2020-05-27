from mailmerge import MailMerge
import os
from datetime import datetime as dt

# MS Word 템플릿 파일 불러오기
cwd = os.getcwd()
template_filename = "fax_cover_template.docx"
template_filepath = os.path.join(cwd, "data", template_filename)

# 템플릿 파일로 메일머지(mail-merge) 객체 만들기
document = MailMerge(template_filepath)

# 수신자 정보 입력하고, 메일머지 객체에 전달하기
document.merge(
    name='박수민',
    fax='031-777-7777',
    phone='031-777-7700',
    date='%s년 %s월 %s일' % (dt.now().year, dt.now().month, dt.now().day),
    title='세금계산서 재발행 요청의 건',
    memo='2019년 8월분',
)

# 메일머지 객체를 MS Word 문서로 저장하기
output_filepath = os.path.join(cwd, "output", "fax_cover_output.docx")
document.write(output_filepath)

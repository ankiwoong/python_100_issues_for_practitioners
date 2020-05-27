import PyPDF2
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import os

# PyPDF2로 페이지 수 계산하기
filename = "north_korea_economic_growth.pdf"
filepath = os.path.join(os.getcwd(), "data", filename)
fp = open(filepath, 'rb')
total_pages = PyPDF2.PdfFileReader(fp).numPages
print(total_pages)

# pdfminer로 페이지별 텍스트 가져오기
page_text = {}
for page_no in range(total_pages):

    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(filepath, 'rb')
    password = None
    maxpages = 0
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    caching = True
    pagenos = [page_no]

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,
                                  caching=caching, check_extractable=True):
        interpreter.process_page(page)

    page_text[page_no] = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()

# 첫 페이지 내용 출력하기
print(page_text[0][:-1])

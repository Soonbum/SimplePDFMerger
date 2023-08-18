# 이 프로그램은 여러 개의 PDF를 합치는 프로그램입니다.

# 실행하기 전에 설치해야 함
# 1. Python 패키지
# 2. pip install pypdf[full]

from tkinter import filedialog
from tkinter import messagebox
from pypdf import PdfReader, PdfWriter

pdf_password = ''   # 여기에 pdf 암호를 입력하십시오!

pdfs = filedialog.askopenfilenames(initialdir="/", title = "파일을 선택하십시오", filetypes = (("*.pdf","*pdf"),("*.pdf","*pdf")))

if pdfs == '':
    messagebox.showwarning("경고", "파일을 추가하십시오")

writer = PdfWriter()

for pdf in pdfs:
    reader = PdfReader(pdf)
    if reader.is_encrypted:
        reader.decrypt(pdf_password)
    for page in reader.pages:
        writer.add_page(page)

with open("result.pdf", "wb") as f:
    writer.write(f)

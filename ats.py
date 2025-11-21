import  PyPDF2
import docx2txt
import re
def extrctfrmpdf(filepath):
    read=PyPDF2.PdfReader(filepath)
    text=""
    for page in read.pages:
        text+=page.extract_text()
    return text
def extrctfrmdocx(filepath):
    return docx2txt.process(filepath)
def clntxt(text):
    text=text.lower()
    text=re.sub(r'[^a-zA-Z\s]', '', text)
    return text
def calscr(rtxt,jdtxt):
    jdkey=set(jdtxt.split())
    rkey=set(rtxt.split())
    match=jdkey.intersection(rkey)
    score=(len(match)/len(jdkey)) * 100
    return round(score,2),match
resume=clntxt(extrctfrmpdf(r"C:\Users\VICTUS\project\sample\sample1.pdf"))
jd=clntxt(open(r"C:\Users\VICTUS\project\sample\jd.txt").read())
score,match=calscr(resume,jd)
print("Match score:",score,"%")
print("Matched Keywords:",match)
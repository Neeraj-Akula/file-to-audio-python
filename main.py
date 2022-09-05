import pyttsx3
import PyPDF2
book=open('oops.pdf','rb')
pdfread=PyPDF2.PdfReader(book)
pages=pdfread.numPages
speak=pyttsx3.init()
page=pdfread.getPage(8)
text=page.extractText()

speak.say(text)
speak.runAndWait()
import pyttsx3
from pypdf import PdfReader
fetch_pdf=input("please enter the location of the PDF you want to listen: ")
fetch_pageNo = int(input("Enter the page No. of the PDF you want to listen: "))
reader = PdfReader(fetch_pdf)
page= reader.pages[fetch_pageNo]
text = page.extract_text()

speak = pyttsx3.init()

rate = speak.getProperty("rate")
print(f"Default rate: {rate}")

speak.setProperty("rate", rate -40)
speak.say(text)
speak.runAndWait()
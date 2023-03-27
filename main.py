
import speech_recognition as sr
from fpdf import FPDF

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        query = query.lower()
        print(f'words recognised : {query}')
    except Exception as e:
        print(e)
        print("Unable to recognize")
        return "none"

    return query

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

while True:
    
    data = listen().lower()
    with open("notes.txt", "a") as f:
        f.write(f"{data}\n")
        pdf.multi_cell(0, 10, data)

    if 'class over' in data:
        break
    # Convert the text file to PDF after writing
    
with open("notes.txt", "r") as file:
    text = file.read()
pdf.output("notes.pdf")

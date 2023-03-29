
import speech_recognition as sr
from fpdf import FPDF
import time
import os



def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source,phrase_time_limit=10)
    try:
        query = r.recognize_google(audio, language='en-in')
        query = query.lower()
        print(f'words recognised : {query}')
        time.sleep(1)
    except Exception as e:
        print(e)
        print("Unable to recognize")
        return "none"

    return query

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

try:
    with open("notes.txt", "r") as file:
        text = file.read()
except FileNotFoundError:
    text = ""

# Add the existing text to the PDF
pdf.multi_cell(0, 10, text)

while True:
    
    data = listen().lower()
    with open("notes.txt", "a") as f:
        f.write(f"{data}\n")
        pdf.multi_cell(0,10,data)
        
    if 'class over' in data:
        break
    
    
    # Convert the text file to PDF after writing
with open("notes.txt", "r") as file:
    text = file.read()

with open("notes.pdf", "w") as file:
    pdf.output("notes.pdf",'F')
    

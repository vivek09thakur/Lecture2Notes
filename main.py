from voice_recognition import listen_to_teacher
from fpdf import FPDF
import speech_recognition as sr

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

try:
    with open("notes.txt", "r") as file:
        text = file.read()
except FileNotFoundError:
    text = ""


pdf.multi_cell(0, 10, text)

if __name__=='__main__':
    
    while True:
        recognizer = sr.Recognizer()
        data = listen_to_teacher(recognizer)
        if data is not None:
            with open("notes.txt", "a") as f:
                f.write(f"{data}\n")
                pdf.multi_cell(0, 10, data)
            if 'over' in data:
                break 
    with open("notes.txt", "r") as file:
        text = file.read()
    with open("notes.pdf", "w") as file:
        pdf.output("notes.pdf",'F')
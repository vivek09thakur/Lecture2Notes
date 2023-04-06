from voice_recognition import listen
from fpdf import FPDF
import os

def  clear_console():
    return os.system('cls')


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


if __name__=='__main__':
    
    clear_console()
    while True:
        
        data = listen()
        if data is not None:
            with open("notes.txt", "a") as f:
                f.write(f"{data}\n")
                pdf.multi_cell(0, 10, data)

            if 'class over' in data:
                break

            
        # Convert the text file to PDF after writing
    with open("notes.txt", "r") as file:
        text = file.read()

    with open("notes.pdf", "w") as file:
        pdf.output("notes.pdf",'F')


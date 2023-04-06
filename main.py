from vosk import Model,KaldiRecognizer
import pyaudio
from fpdf import FPDF
import time
import os
import json


# Speech Recognition Using Vosk
model = Model('./vosk/vosk-model-small-en-in-0.4')
mic = pyaudio.PyAudio()
recognizer = KaldiRecognizer(model, 16000)
stream = mic.open(rate=16000, channels=1, format=pyaudio.paInt16, input=True, frames_per_buffer=8192)
stream.start_stream()

    
def listen():
    
    frames = []
    for i in range(0, int(16000 / 8192 * 3)):
        data = stream.read(8192)
        frames.append(data)
    data = b''.join(frames)

    try:
        if recognizer.AcceptWaveform(data):
            results = recognizer.Result()
            user_input = json.loads(results)['text']
            return user_input
        else:
            return None
    except Exception as e:
        print("Unable to recognize waveform")
        print(e)


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
        print('User Said : '+str(data))
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


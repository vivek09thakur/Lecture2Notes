import speech_recognition as sr
import pyaudio
import wave
import pyautogui
from fpdf import FPDF

class NOTEMAKER:
    
    def __init__(self):
        self.r = sr.Recognizer()
        self.pdf = FPDF()
        self.pdf.add_page()
        self.pdf.set_font("Arial", size=12)
        self.pyaudio = pyaudio.PyAudio()
        
    def record_wave(self, filename):
        print('RECORDING STARTED (PRESS Q TO STOP)')
        stream = self.pyaudio.open(format=pyaudio.paInt16, 
                            channels=1, rate=44100, 
                            input=True, 
                            frames_per_buffer=1024)
        frames = []
        while True:
            data = stream.read(1024)
            frames.append(data)
            if pyautogui.keyDown('n'):
                break
        stream.stop_stream()
        stream.close()
        wf = wave.open(filename, 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(self.pyaudio.get_sample_size(pyaudio.paInt16))
        wf.setframerate(44100)
        wf.writeframes(b''.join(frames))
    
    def transcribe(self, filename):
        with sr.AudioFile(filename) as source:
            audio_data = self.r.record(source)
            text = self.r.recognize_google(audio_data)
            return text
        
    def make_notes(self,transcribe_data,text_file_path,pdf_notes_path):
        # Write to text file
        with open(text_file_path, "a") as f:
            f.write(f"{transcribe_data}\n")
            
        # Write to pdf file
        with open(text_file_path, "r") as file:
            text = file.read()
        self.pdf.multi_cell(0, 10, text)
        self.pdf.output(pdf_notes_path,'F')
        
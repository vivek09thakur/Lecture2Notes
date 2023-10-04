import speech_recognition as sr
import wave
from fpdf import FPDF

class NOTEMAKER:
    
    def __init__(self):
        self.r = sr.Recognizer()
        self.pdf = FPDF()
        self.pdf.add_page()
        self.pdf.set_font("Arial", size=12)
    
        
    def record_wave(self, filename,class_duration):
        print('RECORDING STARTED [PRESS CTRL+C TO STOP RECORDING]')
        try:
            try:
                with sr.Microphone() as source:
                    audio_data = self.r.adjust_for_ambient_noise(source)
                    audio_data = self.r.listen(source,
                                               timeout=class_duration,
                                    phrase_time_limit=class_duration)
                    
                    with open(filename, "wb") as file:
                        file.write(audio_data.get_wav_data())
                    print("RECORDING STOPPED\nFILE SAVED AS "+filename)
                    
            except sr.RequestError:
                print("API was unreachable or unresponsive")
                pass
            except sr.UnknownValueError:
                print("Unable to recognize speech")
                pass
            except sr.WaitTimeoutError:
                print("No speech detected within the given timeout")
                pass
            except Exception as e:
                print(f'EXCEPTION OCCURED => {e}')
        except KeyboardInterrupt:
            print('RECORDING STOPPED')
            pass
    
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
        
from NoteMaker.notemaker import NOTEMAKER

notemaker = NOTEMAKER()

if __name__ == '__main__':
    
    notemaker.record_wave('/data_collected/recorded.wav')
    transcript = notemaker.transcribe('/data_collected/recorded.wav')
    notemaker.make_notes(transcript,'/data_collected/notes.txt','/data_collected/notes.pdf')
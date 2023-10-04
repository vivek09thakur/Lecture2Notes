from NoteMaker.notemaker import NOTEMAKER

notemaker = NOTEMAKER()

audio_file_path = 'CollectedData/audio.wav'
text_file_path = 'CollectedData/text.txt'
pdf_notes_path = 'CollectedData/notes.pdf'

notemaker.record_wave(audio_file_path, 10)
transcribe_data = notemaker.transcribe(audio_file_path)
notemaker.make_notes(transcribe_data, text_file_path, pdf_notes_path)

## LECTURE2NOTES 
> It is a simple command-line python app that can record the notes or speaked lessons of teacher and convert them into **Pdf Notes**

### Installation

To install this app in your local machine you have to install some requirements first. Run the following command in your terminal to install the requirements.

```sh
    pip install -r requirements.txt
```

### Usage
After installing the requirements you can modify the code according to your needs. 

> [!IMPORTANT]
> You have to change the paths of your files in the code.

- [ ] **audio_file_path** : Create a folder i.e. `CollectedData` and create a file `audio.wav` in it. Then change the path of `audio_file_path` variable in the code.

- [ ] **text_file_path** : Change the path of `text_file_path` variable in the code. i.e. if you want to save the text file in `CollectedData` folder then change the path to `CollectedData/text.txt`.

- [ ] **pdf_notes_path** : Change the path of `pdf_notes_path` variable in the code. i.e. if you want to save the pdf file in `CollectedData` folder then change the path to `CollectedData/notes.pdf`.

> **Or After following the first check box just copy the following code and paste it in your python file.**

```python
    from NoteMaker.notemaker import NOTEMAKER

    notemaker = NOTEMAKER()

    audio_file_path = 'CollectedData/audio.wav' 
    text_file_path = 'CollectedData/text.txt'
    pdf_notes_path = 'CollectedData/notes.pdf'

    notemaker.record_wave(audio_file_path, 10)
    transcribe_data = notemaker.transcribe(audio_file_path)
    notemaker.make_notes(transcribe_data, text_file_path, pdf_notes_path)

```

And then run the python file using the following command.

```sh
    python main.py
```

### Best Practices

> [!NOTE]
> It is recommended to use a **noise cancellation microphone** for better results.
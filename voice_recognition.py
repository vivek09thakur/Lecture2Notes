import speech_recognition as sr

def listen_to_teacher(recognizer):
    voice_input = ''
    try:
        with sr.Microphone() as source:
            print('Listening for lecture...')
            audio = recognizer.listen(source=source, timeout=5, phrase_time_limit=5)
        voice_input = recognizer.recognize_google(audio)
        print('\nInput : {}'.format(voice_input))
    except sr.UnknownValueError:
        pass
    except sr.RequestError:
        print('Network error.')
    except sr.WaitTimeoutError:
        pass
    except TimeoutError:
        pass
    return voice_input.lower()
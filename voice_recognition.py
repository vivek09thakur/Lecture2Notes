import speech_recognition as sr

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source) # remove noise
        audio = r.listen(source, phrase_time_limit=5) # listen for up to 5 seconds

    try:
        user_input = r.recognize_google(audio)
        print(f"User said: {user_input}")
        return user_input
    except sr.UnknownValueError:
        print("Unable to recognize speech")
        return None
    except sr.RequestError as e:
        print(f"Error: {e}")
        return None

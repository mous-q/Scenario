import speech_recognition as sr

def get_speech() -> None:

    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)
        print("say anything : ")
        audio= r.listen(source)
        try:
            text = r.recognize_google(audio, language='ru-RU')
            return text.lower()
        except:
            pass


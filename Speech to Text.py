import speech_recognition as sr
import os


def SpeechToText():
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    print('Recognizing...')
    query = r.recognize_google(audio, language='en-in')
    print(f'User said: {query}\n')

    if os.path.exists('data.txt'):
        with open('data.txt', 'a') as file:
            file.write(query)
    else:
        with open('data.txt', 'w') as file:
            file.write(query+'\n\n')
    return query


SpeechToText()

import os
import speech_recognition as sr
from databaseQuery import connect, databaseExecute
from dialogflow import detect_intent_with_texttospeech_response
from tasks import take_query

def viviResponse(audio):
    print(audio)
    for line in audio.splitlines():
        os.system("say " + audio)

def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=2)
        viviResponse('Anything that I can help?')
        audio = r.listen(source)
        print('here...')
    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')
    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('....')
        command = myCommand()
    return command

def assistant(command):
    action, parameter = detect_intent_with_texttospeech_response("vivi-ysjylu", 123456789, [command], "en-US")
    take_query(action,parameter)

#cur = connect()
#databaseExecute(cur, 'SELECT 2+2');
#cur.close()

# can create a loop in order to constantly get prepared for tasks
assistant(myCommand())

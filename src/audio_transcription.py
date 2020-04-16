import os
from os import listdir
from os.path import isdir
from os.path import isfile, join
import speech_recognition as sr


class AudioTranscription:

    def transcribeAudio(fileName, directory):
        r = sr.Recognizer()

        with sr.AudioFile(directory + "/" + fileName) as source:
            audio = r.record(source)
        try:
            s = r.recognize_google(audio)
            temp = directory + '/' + os.path.splitext(fileName)[0] + '.txt'
            file = open(temp, "w+")
            file.write(s)
            file.close()
        except Exception as e:
            print("Exception: "+str(e))

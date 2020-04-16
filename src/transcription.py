import speech_recognition as sr
import pytesseract as pt 
from moviepy.editor import *
import os
from pydub import AudioSegment
from PIL import Image
import re
from datetime import datetime, timedelta
import datefinder 

class convert():
    def __init__(self):
        self.speechRecognize = sr.Recognizer()

    def audioTranscription(self, audio):
        if audio:
            convertedFile = audio.split('.')[0] + '.txt'
            if '.mp3' in audio:
                source = audio
                destination = audio.split('.')[0] + '.wav'
                sound = AudioSegment.from_mp3(source)
                sound.export(destination, format= "wav")
                audio = destination
            with sr.AudioFile(audio) as source:
                audio = self.speechRecognize.record(source)
                text = self.speechRecognize.recognize_sphinx(audio)
                with open(convertedFile, 'w') as output:
                    output.writelines(text)
                lines = open(audio.split('.')[0] + '.txt').readlines()
                with open(audio.split('.')[0] + '.txt', 'w') as f:
                    f.writelines(datetime.utcfromtimestamp(os.path.getmtime(audio)).strftime('%m/%d/%y %H:%M:%s') + ' ' + line for line in lines if line.strip())
                    f.truncate()
            print(convertedFile)
            return convertedFile

    def videoTranscription(self, video):
        if video:
            videos = VideoFileClip(video)
            audio = videos.audio
            file = video.split('.')[0] + '.wav'
            audio.write_audiofile(file)
            return self.audioTranscription(file)

    def imageTranscription(self, image):
        if image: 
            convertedFile = image.split('.')[0] + '.txt'
        pt.pytesseract.tesseract_cmd = '/usr/local/lib/python3.7/site-packages/pytesserect'
        images = Image.open(image)
        text = pt.image_to_string(images, lang='eng')
        file = image.split('.')[0] + '.txt'
        with open(file, 'w') as output:
            output.write(text)
        lines = open(convertedFile).readlines()
        with open(image.split('.')[0] + '.txt', 'w') as f:
            f.writelines(datetime.utcfromtimestamp(os.path.getmtime(image)).strftime('%m/%d/%y %H:%M:%s') + ' ' + line for line in lines if line.strip())
            f.truncate()
        return convertedFile

    def csv(self, csv):
        pass
    def default(self, file):
        return file

        




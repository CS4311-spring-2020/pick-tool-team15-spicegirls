import speech_recognition as sr

r = sr.Recognizer()
with sr.AudioFile('/Users/dima/Desktop/pick-tool-team15-spicegirls/Resources/Listen To This and Change Yourself  Kobe Bryant (Eye Opening Speech).wav') as source:
    audio = r.record(source)
    
try:
    s = r.recognize_google(audio)
    print("Text: " +s)
except Exception as e:
    print("Exception: "+str(e))

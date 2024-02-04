### import a given python module's :
            ### 1) Install a python pip module
            ### 2) pip install SpeechRecognition
            ### 3) pip install Pyaudio - some times all module's are not perfectly install so check and install all module's
            ### 4) pip install googletrans==3.1.0a0
            ### 5) pip install gTTS
            ### 6) pip install playsound

        ### its working perfectly ###
### 1st - try-except block of code is convert a audio-to-video
### 2nd - try-except block of code is convert a text-to-text
### 3rd - try-except block of code is convert a text-to-audio


import speech_recognition as sr ###speech recognition use to convert a audio to  text
from googletrans import Translator ### googletrans use to convert a original text to target text
from gtts import gTTS  ### gttp use to convert a text to audio
from playsound import playsound ### playsound use to play a converted audio
import os ### os use to rewrite a audio file

r = sr.Recognizer()
translator = Translator()

while True:
    with sr.Microphone() as source:
        print("Speak: ")
        audio = r.listen(source) ### convert a original audio to text format
        try:
            speechText = r.recognize_google(audio)
            if speechText == "exit": ### if you want to stop the loop opertion then say exit.
                break
            print("Original Text:", speechText)
        except sr.UnknownValueError:
            print("Could not understand")

        try:
            print("Text Translation")
            translatedText = translator.translate(speechText, dest="ml") ### convert a given input into malayalam text format 
            print("Translated Text:", translatedText.text)
        except Exception as e:
            print("Translation not working:", str(e))

        try:
            voice = gTTS(text=translatedText.text, lang="ml") ### convert a malayalam text format to audio format
            voice.save("voice.mp3")
            playsound("voice.mp3")
            os.remove("voice.mp3")
        except Exception as e:
            print("Error generating or playing the voice:", str(e))

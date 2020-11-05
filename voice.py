import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS 

def speak(text):
    myspeech = gTTS(text=text, lang='en')
    filename = 'myspeech.mp3'
    myspeech.save(filename)
    playsound.playsound(filename)

def my_word():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        word = ''
        ################### google #######################
        try:
            print('sent for recognition. Please wait...')
            word = r.recognize_google(audio)
            print('I heard : ',word)
            if word == 'stop':
                return 'stop'
            return word
        except Exception as e:
            print('Exception recognizing : '+str(e))
            return None
        
        
        # ################ google cloud speech api ################
        # #GOOGLE_CLOUD_SPEECH_CREDENTIALS = 'F:\my study\miscelleneous\google cloud key\My First Project-fb9ca964cbea.json'
        # try:
        #     print("Google Cloud Speech thinks you said " + r.recognize_google_cloud(audio, credentials_json=os.environ('GOOGLE_CLOUD_SPEECH_CREDENTIALS')))
        # except sr.UnknownValueError:
        #     print("Google Cloud Speech could not understand audio")
        # except sr.RequestError as e:
        #     print("Could not request results from Google Cloud Speech service; {0}".format(e))

if __name__ == "__main__":

    i=0
    while i<10:
        print('say something...')
        word = my_word()
        i+=1


'''
problem list : 
g2 : jeetu
a3 : 83
b3 : b tree
b4 : before
e3 : tree, T3
e4 : MI 4
e5 : MI 5
e8 : 88, cant process
'''
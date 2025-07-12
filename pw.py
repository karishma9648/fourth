#import required module
import speech_recognition as sr
import pyttsx3
#explicit function to take input commands
# and recognise them
def takeCommandHindi():
    engine = pyttsx3.init('dummy')
    engine.runAndWait()
    r=sr.Recognizer()
    with sr.Microphone()as source:
        #
        print('Listening')
        r.pause_threshold=0.7
        audio = r.listen(source)
        try:
            print("Recognize")
            Query= r.recognize_google(audio,language='hi-ln')
            print("The query is printed=",Query,"")
        except Exception as e:
                  print(e)
                  print("Say that again sir")
                  return"None"
        return Query
 #Drive Code
#call the function
takeCommandHindi()
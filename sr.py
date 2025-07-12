import speech_recognition as sr
import pyttsx3

# initialize the recognizer
r = sr.Recognizer()
# function to convert text to speech
def SpeakText(command):
    # initializes the engine
    engine=pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
# loop infinitely for user to speak
while(1):
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2=r.listen(source2)
            MyText=r.recognize_google(audio2)
            MyText = MyText.lower()
            print("Did you say:",MyText)
    except sr.RequestError as e:
        print("Could not request result;{0}".format(e))
    except sr.UnknownValueError:
        print("Unknown error occured")
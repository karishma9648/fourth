
from moviepy import VideoFileClip 
import speech_recognition as sr

video = VideoFileClip("v2.mp4")

audio_file = video.audio
audio_file.write_audiofile("11.wav")

r = sr.Recognizer()

with sr.AudioFile(filename_or_fileobject="11.wav") as source:
    data = r.record(source)

text = r.recognize_google(data)
print("Result")
print(text)
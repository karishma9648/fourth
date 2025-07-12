from moviepy import VideoFileClip
import speech_recognition as sr 
video = mp.VideoFileClip("")
audio_file = video.audio
audio_file.write_audiofile("")
r= sr.Recognizer()
with sr.AudioFile("")as source:
             data = r.record(source)  
text = r.recognize_google(data)
print("\nThe resultant text from video is:\n")
print(text)

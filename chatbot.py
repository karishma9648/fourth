import google.generativeai as genai
import speech_recognition as sr
import pyttsx3

# Set up Gemini API key
GEMINI_API_KEY = "AIzaSyDzeuI2BKIqrY5fQir_bUMviNc9a4_8C-w"  # Replace with your API key
genai.configure(api_key=GEMINI_API_KEY)

# Initialize text-to-speech engine
engine = pyttsx3.init()

def text_to_speech(text):
    """Converts text to speech and plays the audio directly."""
    engine.say(text)
    engine.runAndWait()

def speech_to_text():
    """Converts user's speech input into text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand the audio.")
        return None
    except sr.RequestError:
        print("Could not request results, please check your internet connection.")
        return None

def generate_response(user_input):
    """Generates a response using Gemini API."""
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(user_input)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

def chatbot():
    """Main chatbot function."""
    print("Welcome to the Chatbot! Type or speak your query (say 'exit' to quit).")
    
    while True:
        mode = input("Type 'text' for text input or 'voice' for voice input: ").strip().lower()
        
        if mode == "text":
            user_query = input("You: ")
        elif mode == "voice":
            user_query = speech_to_text()
            if not user_query:
                continue
        else:
            print("Invalid input. Please type 'text' or 'voice'.")
            continue

        if user_query.lower() == "exit":
            print("Goodbye!")
            break

        # Get response from Gemini
        response = generate_response(user_query)
        print("Chatbot:", response)

        # Convert response to speech and play it
        text_to_speech(response)

if __name__ == "__main__":
  chatbot()
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
# import pyaudio

# Initialize the speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio)
            print(f"User said: {query}")
            return query.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that. Can you please repeat?")
            return 
        except sr.RequestError:
            print("Sorry, I'm unable to access the Google API. Please check your internet connection.")
            return 

# Function to perform tasks based on user commands
def process_command(query):
    if "hello" in query:
        speak("Hello! How can I assist you today?")
    elif "time" in query:
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current time is {current_time}")
        print(f"{current_time}")
    elif "date" in query:
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        speak(f"Today's date is {current_date}")
   
    if "search" in query:
        speak("What would you like me to search for?")
        search_query = listen()
        if search_query:
            google_url = f"https://www.google.com/search?q={search_query}"
            webbrowser.open(google_url)
            speak(f"Here are the search results for {search_query}")

    elif "open youtube" in query:
        speak("What would you like me to search for on YouTube?")
        search_query = listen()
        if search_query:
            youtube_url = f"https://www.youtube.com/results?search_query={search_query}"
            webbrowser.open(youtube_url)
            speak(f"Here are the search results for {search_query}")

    elif "exit" in query or "quit" in query:
        speak("Goodbye Akash!")
        exit()
    else:
        speak("I'm sorry, I didn't understand that command.")

# Main function to run the voice assistant
def main():
    speak("Hello Akash! I'm your basic voice assistant. How can I assist you today?")
    while True:
        query = listen()
        if query:
            process_command(query)
        if "exit" in query or "quit" in query:
                speak("Goodbye!")
                break

if __name__ == "__main__":
    main()

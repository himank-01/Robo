import speech_recognition as sr
import webbrowser
import pyttsx3
import music_library

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    """Process the recognized command."""
    if "open google" in c.lower():
        webbrowser.open("https://www.google.co.in")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
    elif "open jio cinema" in c.lower():
        webbrowser.open("https://www.jiocinema.com")
    elif "open prime video" in c.lower():
        webbrowser.open("https://www.primevideo.com")
    elif "open netflix" in c.lower():
        webbrowser.open("https://www.netflix.com")

    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=music_library.music[song]
        webbrowser.open(link)

if __name__ == "__main__":
    speak("Initializing Jarvis")
    
    while True:
        r = sr.Recognizer()
        print("Recognizing...")
        try:
            # Recognizing speech
            with sr.Microphone() as source:
                print("Listening...")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source, timeout=4, phrase_time_limit=2)

            # Convert audio to text
                word = r.recognize_google(audio)
            if "jarvis" in word.lower():
                speak("Yeah")
                print("Jarvis active")
                


                # Start another microphone session for the command
            with sr.Microphone() as source:
                
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source, timeout=4, phrase_time_limit=2)

                # Recognize the command
                command = r.recognize_google(audio)
                processCommand(command)

        except sr.UnknownValueError:
            print("Sorry, I didn't understand that.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

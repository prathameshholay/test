import speech_recognition as sr
import pyttsx3 
import wikipedia

engine = pyttsx3.init()
engine.runAndWait()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def greet():
    speak("system is live. you can ask me anything ")

try:
    print("checking requirements.")
    speak("checking requirements.")
    speak("Connected to internet sir.")
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("microphone is ready")
except:
    print("i won't be ablr to take commands sir if your microphone is not connected. Please connect a microphone and try again :)")
    speak("i won't be able to take commands sir if your microphone is not connected. Please connect a microphone and try again.")
    quit()

def takeCommand():
    #start listening the command from the user
    with sr.Microphone() as source:
        print("Please wait.. ")
        print("listening....")
        r.energy_threshold = 3500
        r.dynamic_enery_threshold = True
        audio = r.listen(source)

    try:
        print("recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"you said: {query}\n")
        file = open('said.txt', 'a+')
        file.write("\n"+query)
        file.close()
    

    except Exception as e:
        print("Say that again ,please")
        speak("say that again please")
        return "None"
    return query


if __name__ == "__main__":

    greet()
    while True:
        query = takeCommand().lower()
        #GREETING QUERY
        if 'hello 'in query:
            speak("hello sir how are you doing these days")
        #JARVIS ORTHODOX QUIT QUERY
        if 'quit' in query:
            speak("thanks for having me ")
            quit()
        #JARVIS QUIT FUNCTION
        if 'jarvisquit' in query:
            speak("thanks for having me ")
            quit()
        #CLEARING DATA FROM FILES CODE

        #WIKIPEDIA CODE 
        if 'wikipedia' in query:
            speak("what should i search on wikipedia sir.")
            takeCommand()
            query = query.replace("wikipedia","") and query.replace("what is","")
            result = wikipedia.summary(query, sentences = 2)
            print("according to wikipedia")
            print(result)
            speak("according to wikipedia.")
            speak(result)
            
      
import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voices',voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    
    elif hour>=12 and hour<18:
        speak("good afternoon")
    
    else:
        speak("good evening")
    
    speak("i am jarvis may i help you")

def takecomand():
    #it takes input from microphone give output through strings 

    r= sr.Recognizer()
    with sr.Microphone() as source:
        print('listing.....')
        r.pause_threshold=1
        audio=r.listen(source)
    
    try:
       print("recoginizing....")
       query=r.recognize_google(audio,language="en-in")
       r.recognizer_google(audio,language="en-in")
       print("user said",query)
       
    except Exception as e :
        print("say that again....")
        return "None"
    return query    

              
              
              
            
            
            
            
if __name__=='__main__':
    wishme()
    while(True):
        query=takecomand().lower()


        #logic for executing task based on query
        if "wikipedia" in query:
            speak("Searching....")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open gmail" in query:
            webbrowser.open("gmail.com")

        elif "open instagram" in  query:
            webbrowser.open("instagram.com")

        elif "open facebook" in query:
            webbrowser.open("facebook.com")          



        
        


    
    
    
    
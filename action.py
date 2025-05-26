import text_to_speech
import speech_to_text
import datetime
import webbrowser

def Action(data):
    user_data = data.lower()

    if "what is your name" in user_data:
        text_to_speech.text_to_speech("my name is sree. your desktop assistant")
        return "my name is virtual assisstant"

    elif "hello" in user_data or "hii" in user_data :

        text_to_speech.text_to_speech("hey, mam how can i help you")
        return "hello mam. how can i help you"

    elif "good morning" in user_data :
        text_to_speech.text_to_speech("good morning mam")  
        return "good morning mam"
    
    elif "good morning" in user_data :
        text_to_speech.text_to_speech("good morning mam")  
        return "good morning mam"
    
    elif "what is time now" in user_data :
        current_time = datetime.datetime.now()  
        Time = (str)(current_time) + "Hour:", (str)(current_time.minute) + "Minute"
        text_to_speech.text_to_speech(Time)   
        return Time

    elif "shutdown" in user_data :
        text_to_speech.text_to_speech("ok mam")
        return "ok mam"

    elif "open google" in user_data :
        webbrowser.open("https://google.com/")
        text_to_speech.text_to_speech("google.com is ready for you")
        return "google.com is ready for you"

    elif "open linkedin" in user_data :
        webbrowser.open("https://linkedin.com/")
        text_to_speech.text_to_speech("linkedin is ready for you")
        return "linkedin is ready for you"

    elif "open youtube" in user_data :
        webbrowser.open("https://youtube.com/")
        text_to_speech.text_to_speech("youtube.com is ready for you")  
        return "youtube.com is ready for you"  

    elif "open spotify" in user_data :
        webbrowser.open("https://spotify.com/")
        text_to_speech.text_to_speech("spotify.com is ready for you")
        return "spotify.com is ready for you"

    elif "open instagram" in user_data :
        webbrowser.open("https://instagram.com/")
        text_to_speech.text_to_speech("instagram is ready for you")
        return "instagram is ready for you"


    else:
        text_to_speech.text_to_speech("I'm not able to understand")
        return "I'm not able to understand"
    

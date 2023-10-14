import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser

engine = pyttsx3.init('dummy')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print('Good Morning')
        speak('Good Morning')
    elif hour > 12 and hour < 18:
        print('Good Afternoon')
        speak('Good Afternoon')
    else:
        print('Good Evening')
        speak('Good Evening')

    speak('Hello Sir, I am Friday, your Artificial intelligence assistant. Please tell me how may I help you')

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
        return query
    except Exception as e:
        print(e)
        return None

if __name__ == '__main__':
    wishme()
    while True:
        command = takecommand()
        print(command)
        if command is not None:
            query = command.lower()
            print(f'query is {query}')
            if 'open youtube' in query:
                url = "https://www.youtube.com"
                webbrowser.get("safari").open(url)
            elif 'open google' in query:
                url = "https://www.google.com"
                webbrowser.get("safari").open(url)
            elif 'time' in query:
                strtime = datetime.datetime.now().strftime('%H:%M:%S')
                print(f'Sir the time is {strtime}')
            elif 'open stack overflow' in query:
                url = "https://www.stackoverflow.com"
                webbrowser.get("safari").open(url)
            elif 'exit' in query:
                speak('okay boss, please call me when you need me')
                quit()
        else:
            print("Could not recognize speech.")
            speak('Sorry, tell me something')

# import pyttsx3
# import datetime
# import speech_recognition as sr
# import webbrowser
# import mac_say

# # engine = pyttsx3.init('nsss')
# # voices = engine.getProperty('voices')
# # engine.setProperty('voice',voices[1].id)    

# def speak(audio):
#     mac_say.say(audio)
#     # engine.say(audio)
#     # engine.runAndWait()

# def wishme():
#     hour = int(datetime.datetime.now().hour)
#     if hour >= 0 and hour < 12:
#         print('Good Morning')
#         speak('Good Morning')
#     elif hour > 12 and hour < 18:
#         print('Good Afternoon')
#         speak('Good Afternoon')
#     else:
#         print('Good Evening')
#         speak('Good Evening')

#     speak('Hello Sir, I am Friday, your Artificial intelligence assistant. Please tell me how may I help you')

# def takecommand():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         r.pause_threshold = 1
#         audio = r.listen(source)
#     try:
#         print("Recognizing...")
#         query = r.recognize_google(audio, language='en-in')
#         print(f"You said: {query}")
#         return query
#     except Exception as e:
#         print(e)
#         return None

# if __name__ == '__main__':
#     wishme()
#     while True:
#         command = takecommand()
#         print(command)
#         if command is not None:
#             query = command.lower()
#             print(f'query is {query}')
#             if 'open youtube' in query:
#                 url = "https://www.youtube.com"
#                 webbrowser.get("safari").open(url)
#             elif 'open google' in query:
#                 url = "https://www.google.com"
#                 webbrowser.get("safari").open(url)
#             elif 'time' in query:
#                 strtime = datetime.datetime.now().strftime('%H:%M:%S')
#                 speak(f'Sir the time is {strtime}')
#                 print(f'Sir the time is {strtime}')
#             elif 'open stack overflow' in query:
#                 url = "https://www.stackoverflow.com"
#                 webbrowser.get("safari").open(url)
#             elif 'exit' in query:
#                 speak('okay boss, please call me when you need me')
#                 quit()
#         else:
#             print("Could not recognize speech.")
#             speak('Sorry, tell me something')


# # import pyttsx3                                    
# # import datetime                                   
# # import speech_recognition as sr                  
# # import webbrowser                                 

# # # engine = pyttsx3.init('nsss')                    # sapi5 is an API and the technology for voice recognition and synthesis provided by Microsoft
# # engine = pyttsx3.init('dummy')                    # sapi5 is an API and the technology for voice recognition and synthesis provided by Microsoft
# # voices = engine.getProperty('voices')             # gets you the details of the current voices
# # # engine.setProperty('voice',voices[1].id)          # 0-male voice , 1-female voice



# # def speak(audio):                                # function for assistant to speak
# #     engine.say(audio)
# #     engine.runAndWait()                          # without this command, the assistant won't be audible to us



# # def wishme():                                    # function to wish the user according to the daytime
# #     hour = int(datetime.datetime.now().hour)
# #     if hour>=0 and hour<12:
# #         print('Good Morning')
# #         speak('Good Morning')

# #     elif hour>12 and hour<18:
# #         print('Good Afternoon')
# #         speak('Good Afternoon')

# #     else:
# #         print('Good Evening')
# #         speak('Good Evening')

# #     speak('Hello Sir, I am Friday, your Artificial intelligence assistant. Please tell me how may I help you')


# # # def takecommand():                               # function to take an audio input from the user
# # #     r = sr.Recognizer()
# # #     with sr.Microphone() as source:
# # #         print('Listening...')
# # #         r.pause_threshold = 1
# # #         audio = r.listen(source)


# # #     try:                                            # error handling
# # #         print('Recognizing...')
# # #         query = r.recognize_google(audio,language = 'en-in')  # using google for voice recognition
# # #         print(f'User said: {query}\n')

# # #     except Exception as e :
# # #         print('Say that again please...')        # 'say that again' will be printed in case of improper voice
# # #         return 'None'  
# # #     return query
# # def takecommand():
# #     r = sr.Recognizer()
# #     with sr.Microphone() as source:
# #         print("Listening...")
# #         r.pause_threshold = 1
# #         audio = r.listen(source)

# #     try:
# #         print("Recognizing...")
# #         query = r.recognize_google(audio, language='en-in')
# #         print(f"You said: {query}")
# #         return query
# #     except Exception as e:
# #         print(e)
# #         return None

# # # def sendemail(to,content):                       # function to send email
# # #     server = smtplib.SMTP('smtp.gmail.com',587)
# # #     server.ehlo()
# # #     server.starttls()
# # #     server.login('senders_eamil@gmail.com','senders_password')
# # #     server.sendmail('senders_email@gmail.com',to,content)
# # #     server.close()


# # if __name__ == '__main__' :                      # execution control
# #     wishme()
# #     while True:
# #         command = takecommand()
# #         print(command)
# #         if command is not None:
# #             query = command.lower()
# #             print(f'query is {query}')

# #             # query = takecommand().lower()  # converts user asked query into lower case
# #             # The whole logic for execution of tasks based on user asked query
# #             if 'open youtube' in query :
# #                 # webbrowser.open('youtube.com')
# #                 url = "https://www.youtube.com"  # Замените этот URL на тот, который вы хотите открыть
# #                 webbrowser.get("safari").open(url)

# #             elif 'open google' in query :
# #                 # webbrowser.open('google.com')
# #                 url = "https://www.google.com"  # Замените этот URL на тот, который вы хотите открыть
# #                 webbrowser.get("safari").open(url)

# #             elif 'time' in query :
# #                 strtime = datetime.datetime.now().strftime('%H:%M:%S')
# #                 # speak(f'Sir the time is {strtime}')
# #                 print(f'Sir the time is {strtime}')

# #             elif 'open stack overflow' in query :
# #                 # webbrowser.open('stackoverflow.com')
# #                 url = "https://www.stackoverflow.com"  # Замените этот URL на тот, который вы хотите открыть
# #                 webbrowser.get("safari").open(url)

# #             # elif 'pycharm' in query :
# #             #     codepath = 'pycharm_directory_of_your_computer'
# #             #     os.startfile(codepath)

# #             # elif 'email' in query :
# #             #     try:
# #             #         speak('what should i write in the email?')
# #             #         content = takecommand()
# #             #         to = 'reciever_email@gmail.com'
# #             #         sendemail(to, content)
# #             #         speak('email has been sent')
# #             #     except Exception as e:
# #             #         print(e)
# #             #         speak('Sorry, I am not able to send this email')

# #             elif 'exit' in query:
# #                 speak('okay boss, please call me when you need me')
# #                 quit()
# #         else:
# #             print("Could not recognize speech.")
# #             speak('Sorry, tell me something')

            # https://pythonist.ru/golosovoj-pomoshhnik-na-python/
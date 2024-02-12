import speech_recognition as sr

'''
index=1
for name in sr.Microphone.list_microphone_names():
    print(index," : ",name)
    index=index+1
'''
recognizer = sr.Recognizer()

def mic1():
    with sr.Microphone(device_index=0) as source:
        print("say something: ")
        recognizer.adjust_for_ambient_noise(source)
        audio=recognizer.listen(source)
        print("listening.....")
        text=recognizer.recognize_google(audio)
        print("you said: ",text)
        return text
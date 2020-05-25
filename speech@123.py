import speech_recognition as sr
r=sr.Recognizer()
print("Speak Now")
with sr.Microphone() as source:
    data=r.record(source,duration=5)
    print("recognizing.....")
    output=r.recognize_google(data)
    print(output)

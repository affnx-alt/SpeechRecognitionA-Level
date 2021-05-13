#importing the SpeechRecognition module
import speech_recognition as sr  


print("enter a file name")
name = input()


#get audio from the microphone
#or
#reading the audio file as a source file
#listening to the source and store as a text variable
r = sr.Recognizer()                                                                                   
with sr.AudioFile('bible.wav') as source:
    r.adjust_for_ambient_noise(source)
    audio = r.record(source)   
try:
    #using google's speech recognition API
    print(r.recognize_google(audio))
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))
    
    
f = open(name+".txt" , "x")
f.write(r.recognize_google(audio))
f.close()
    
    

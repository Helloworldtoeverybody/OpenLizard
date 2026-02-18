from speech_recognition.recognition import recognition
import ollama
from ollama_model.ollama_model import model


model = model()


rec = recognition()
rec.find_microphone() # Lists all devices and microphones and their indexes


while True:
    rec.run() # Run voice recognition!


    if rec.activate_flag:
   

        model.generate(rec.get_text())
        rec.activate_flag = 0



from speech_recognition.recognition import recognition
import ollama
from ollama_model.ollama_model import model


model = model()


model.generate("Hello")


rec = recognition()


rec.find_microphone() # Lists all devices and microphones and their indexes









while True:
    rec.run() # Run voice recognition!




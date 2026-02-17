'''

from speech_recognition.recognition import recognition

rec = recognition()


rec.find_microphone()

while True:
    rec.run()


'''



from vosk import Model,KaldiRecognizer

import pyaudio

model = Model("/root/Open_Lizard/vosk-model-small-ru-0.22")
recognizer = KaldiRecognizer(model, 16000)

mic = pyaudio.PyAudio()

stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192, input_device_index=2)
stream.start_stream()


    
for i in range(mic.get_device_count()):
    info = mic.get_device_info_by_index(i)
    print(i, info["name"], "input channels:", info["maxInputChannels"])

while True:
    data = stream.read(4096)


    if recognizer.AcceptWaveform(data):
        text = recognizer.Result()
        print(text)
        

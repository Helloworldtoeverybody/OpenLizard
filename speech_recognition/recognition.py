from vosk import Model,KaldiRecognizer

import pyaudio








class recognition:

    def __init__(self):


        self.mic = pyaudio.PyAudio()

        self.stream = self.mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
        self.stream.start_stream()

        self.model = Model("/root/Open_Lizard/vosk-model-small-ru-0.22")
        self.recognizer = KaldiRecognizer(self.model, 16000)



    def run(self):
        data = self.stream.read(4096)


        if self.recognizer.AcceptWaveform(data):
            text = self.recognizer.Result()
            print(text)

    def find_microphone(self):
        
        for i in range(self.mic.get_device_count()):
            info = self.mic.get_device_info_by_index(i)
            print(i, info["name"], "input channels:", info["maxInputChannels"])
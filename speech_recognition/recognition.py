from vosk import Model,KaldiRecognizer

import pyaudio







class recognition:

    def __init__(self):


        self.mic = pyaudio.PyAudio()
        self.output = None
        self.activate_flag = 0
   
        self.stream = self.mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192, input_device_index=2)
        self.stream.start_stream()

        # self.model = Model("/root/Open_Lizard/vosk-model-small-ru-0.22")
        self.model = Model("vosk-model-small-en-us-0.15")
        self.recognizer = KaldiRecognizer(self.model, 16000)




    key_words = ["alice", "jarvis", "lizard"]



    def key_word(self, text):
        text = text.lower()

        if any(word in text for word in self.key_words):
            return True
        

    def get_text(self):
        return self.output








    def run(self):
        self.data = self.stream.read(4096, exception_on_overflow=False)


        if self.recognizer.AcceptWaveform(self.data):
            self.text = self.recognizer.Result()
            self.output = self.text.lower()
            print(self.output)


            if self.key_word(self.text):
                print("Activated!")
                self.activate_flag = 1
                

        

    def find_microphone(self):
        
        for i in range(self.mic.get_device_count()):
            info = self.mic.get_device_info_by_index(i)
            print(i, info["name"], "input channels:", info["maxInputChannels"])
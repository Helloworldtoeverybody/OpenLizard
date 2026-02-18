import ollama

class model:
    def __init__(self):
        self.model = 'qwen2.5:0.5b' # Just type "ollama list" in terminal and choose a model you want from that list


    def generate(self, prompt):

        self.result = ollama.generate(model= self.model, prompt=prompt) # Generating answer
        print(self.result['response']) # "response" means print only answer, without any uneccesary information






       

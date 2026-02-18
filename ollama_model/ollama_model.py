import ollama
from system_prompt import SYSTEM_PROMPT  # import the string

class model:
    def __init__(self):
        self.model_name = "qwen2.5:0.5b"
        self.system_prompt = SYSTEM_PROMPT  # THIS IS NOW A STRING

    def generate(self, user_prompt):
        response = ollama.chat(
            model=self.model_name,
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": user_prompt}
            ]
        )
        answer = response["message"]["content"]
        print(answer)
        return answer

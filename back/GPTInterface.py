import openai
from back.APIKeys import APIKeys

class GPTInterface:
    def __init__(self):
        APIKeys.set_var('OPENAI_API_KEY')
        self.__gpt = openai.OpenAI()
        
    def get_summary(self, article_body):
        completion = self.__gpt.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Provide a concise summary of this article."},
                {"role": "user", "content": article_body}
            ]
        )
        
        return completion.choices[0].message.content
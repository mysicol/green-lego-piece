import openai
from APIKeys import APIKeys

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
    
    # def get_relevance(self, prompt, results):
    #     prompt = ""
    #     for r in results:
    #         prompt += (r + "$")
    #     prompt = prompt[:-1]
    #     completion = self.__gpt.chat.completions.create(
    #         model="gpt-3.5-turbo",
    #         messages=[
    #             {"role": "system", "content": "The search query is: " + prompt + ". I will now provide a short blurb from a few articles separated by dollar signs. For each article blurb, return a rating from 0 (least relevant) to 10 (most relevant) based on how relevant you think the article is to the search query. Delimeter your responses with dollar signs."},
    #             {"role": "user", "content": prompt}
    #         ]
    #     )
        
    #     return completion.choices
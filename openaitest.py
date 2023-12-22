import openai
from config import apikey


openai.api_key=apikey
# print(apikey)




response = openai.Completion.create(

  model="gpt-3.5-turbo-instruct",
  prompt="Write an essay on ChristmasWrite an essay on Christmas",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)


print(response["choices"][0]["text"]) #prints the essay
from openai import OpenAI
from dotenv import load_dotenv
import os

import json

load_dotenv()

client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)
out = completion.choices[0].message.content
print(out)

# print(dir(out))



# with open("out.txt", 'w') as f:
#     f.write(out)
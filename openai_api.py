import os
import openai

openai.api_key = "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"

prompt = input('질문을 입력하세요 : ')

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=prompt,
  temperature=1,
  max_tokens=4000,
)

print("="*30)
print(response['choices'][0]['text'].strip())
print("="*30)
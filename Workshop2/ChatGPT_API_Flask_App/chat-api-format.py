import os
import openai
openai.api_key = 'YOUR_API_KEY'
openai.Completion.create(
  model="gpt-3.5-turbo-instruct",
  prompt="Say this is a test",
  max_tokens=7,
  temperature=0
)


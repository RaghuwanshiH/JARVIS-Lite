import ollama

res = ollama.chat(model='tinyllama', messages=[
  {'role': 'user', 'content': 'write a code two multiply two numbers in python'}
])

print(res['message']['content'])

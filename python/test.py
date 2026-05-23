import ollama

print("TinyLlama Offline Chat")
print("Running locally via Ollama | No data leaves your PC")
print("Type 'exit' to quit")
print("=" * 50)

while True:
    user_prompt = input("\nYou: ")
    
    if user_prompt.lower() in ['exit', 'quit', 'q']:
        print("Closing local chat...")
        break
    
    if not user_prompt.strip():
        continue
        
    res = ollama.chat(
        model='tinyllama', 
        messages=[{'role': 'user', 'content': user_prompt}]
    )
    
    print(f"\nTinyLlama: {res['message']['content']}")

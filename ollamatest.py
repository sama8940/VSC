import ollama

response =ollama.chat(
        model="gemma3:1b",
        messages=[
            {"role" : "system" ,
            "content" : "あなたは親切なアシスタントです"} ,
            {"role" : "system" ,
            "content" : "アルゼンチンの首都は？"}
        ]
    )
print(response["message"]["content"])


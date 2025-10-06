import ollama

response =ollama.chat(
        model="gemma3:1b",
        messages=[
            {"role" : "system" ,
            "content" : "あなたは親切なアシスタントです"} ,
            {"role" : "system" ,
            "content" : "日本の大統領は？"}
        ]
    )
print(response["message"]["content"])


from openai import OpenAI

client = OpenAI(base_url="http://127.0.0.1:8080/v1" ,
                api_key="dummy")

response = client.chat.completions.create(
    model= "Qwen3-30B-Q4_K_M.gguf" ,
    messages=[
        {"role" : "system" ,
         "content" : "あなたは親切なアシスタントです。"} ,
         {"role": "user" ,
          "content" : "忙しいときに、ストレスを減らす方法を教えてください。 /no_think"}
          
    ]
)

print(response.choices[0].message.content.strip())

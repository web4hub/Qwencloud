  import os
  from openai import OpenAI

  client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://maas.qwencloudapi.com/compatible-mode/v1",
  )

  completion = client.chat.completions.create(
    model="qwen3.8-max",
    messages=[
      {"role": "user", "content": "Hello! Tell me a fun fact about AI."}
    ]
  )

  print(completion.choices[0].message.content)

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.qwencloud.com/llms.txt
> Use this file to discover all available pages before exploring further.

# First API call

> Get started in a few minutes

Set up your account and make your first API call to Qwen models.

    <Tip>New users get a free quota to try models at no cost. See [Free quota](/resources/free-quota) for details.</Tip>

## Prerequisites

    <Steps>
    <Step title="Create an account">
    Go to [QwenCloud](https://home.qwencloud.com/) and sign in with GitHub or email.
    </Step>

    <Step title="Get your API key">
    Navigate to [**API Keys**](https://home.qwencloud.com/api-keys), click **Create API key**, and copy your key (starts with `sk-ws-`). [Detailed guide →](/api-reference/preparation/api-key)

     <Warning>
      Keep your API key secret! Never commit it to version control or share it publicly.
    </Warning>
    </Step>

     <Step title="Set your environment variable">
    Store your API key so your code can access it:

    <CodeGroup>
```bash macOS/Linux
      export DASHSCOPE_API_KEY="sk-your-api-key-here"
```

  ```powershell Windows PowerShell
      $env:DASHSCOPE_API_KEY = "sk-your-api-key-here"
```
    </CodeGroup>

    For permanent setup across sessions, see [Configure your API key →](/api-reference/preparation/export-api-key-env).
    </Step>
    </Steps>

## Make your first call

     <Tabs>
    <Tab title="Python">
    Install the OpenAI SDK:

   ```bash
    pip install openai
   ```

    Create a file `hello_qwen.py`:

  ```python
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
 ```

  Run it:

   ```bash
    python hello_qwen.py
  ```
  </Tab>

  <Tab title="Node.js">
    Install the OpenAI SDK:

  ```bash
    npm install openai
   ```

    Create a file `hello_qwen.mjs`:

  ```javascript
    import OpenAI from "openai";

    const openai = new OpenAI({
      apiKey: process.env.DASHSCOPE_API_KEY,
      baseURL: "https://maas.qwencloudapi.com/compatible-mode/v1"
    });

    const completion = await openai.chat.completions.create({
      model: "qwen3.8-max",
      messages: [
        { role: "user", content: "Hello! Tell me a fun fact about AI." }
      ]
    });

    console.log(completion.choices[0].message.content);
 ```

   Run it:

```bash
    node hello_qwen.mjs
```
  </Tab>

  <Tab title="curl">
    <CodeGroup>
  ```bash macOS/Linux
      curl -X POST https://maas.qwencloudapi.com/compatible-mode/v1/chat/completions \
        -H "Authorization: Bearer $DASHSCOPE_API_KEY" \
        -H "Content-Type: application/json" \
        -d '{
          "model": "qwen3.8-max",
          "messages": [
            {
              "role": "user",
              "content": "Hello! Tell me a fun fact about AI."
            }
          ]
        }'
      ```

   ```powershell Windows PowerShell
      curl -X POST https://maas.qwencloudapi.com/compatible-mode/v1/chat/completions `
        -H "Authorization: Bearer $env:DASHSCOPE_API_KEY" `
        -H "Content-Type: application/json" `
        -d '{
          \"model\": \"qwen3.8-max\",
          \"messages\": [
            {
              \"role\": \"user\",
              \"content\": \"Hello! Tell me a fun fact about AI.\"
            }
          ]
        }'
   ```
    </CodeGroup>
  </Tab>
</Tabs>

<Tip>
  For Java, Go, PHP, C#, and other languages, use the OpenAI-compatible endpoint shown in the curl tab with your language's HTTP client. For Java, you can also use the [DashScope Java SDK](/developer-guides/text-generation/quickstart).
</Tip>

## What's next?

- [Text generation guide](/developer-guides/text-generation/quickstart) — Streaming, function calling, and more
- [Vision models](/developer-guides/multimodal/vision) — Analyze images and videos
- [Model selection](/developer-guides/getting-started/model-selection) — Choose the right model for your use case
- [Try AI](https://home.qwencloud.com/try-ai) — Try models interactively

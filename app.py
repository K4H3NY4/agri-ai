import os
import anthropic
from dotenv import load_dotenv, dotenv_values

load_dotenv()

client = anthropic.Anthropic(
    
    api_key=os.environ.get("ANTHROPIC_API_KEY")
)
message = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1000,
    temperature=0.9,
    system="Agriculture in kenya",
    messages=[
        {"role": "user", "content": "how to grow potatoes"}
    ]
)

print(message.content[0].text)
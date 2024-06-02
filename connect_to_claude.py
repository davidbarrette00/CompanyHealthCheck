#https://docs.anthropic.com/claude/docs/quickstart-guide

import anthropic
davids_key = "sk-ant-api03-XPu...DAAA"
govindas_key = ""
sindhus_key = ""
jirens_key = ""

client = anthropic.Anthropic(
    api_key=davids_key #REPLACE WITH YOUR KEY
)

message = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1000,
    temperature=0.0,
    system="Respond only in Yoda-speak.",
    messages=[
        {"role": "user", "content": "How are you today?"}
    ]
)

print(message.content)
#https://docs.anthropic.com/claude/docs/quickstart-guide

import anthropic
davids_key = ""
govindas_key = ""
sindhus_key = ""
jirens_key = ""

client = anthropic.Anthropic(
    api_key=davids_key #REPLACE WITH YOUR KEY
)

messages = []
def send_message(message):
    messages.append({"role": "user", "content": message})
    print(messages)
    response = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=1000,
        temperature=0.0,
        system="Respond as a helpful financial analyst",
        messages=messages
    )
    response_text = response.content[0].text
    messages.append({"role": "assistant", "content": response_text})
    return response_text

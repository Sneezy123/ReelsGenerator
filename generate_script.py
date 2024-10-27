from g4f.client import Client


def return_script(prompt: str) -> str:

    client = Client()

    
    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "user",
            "content": prompt
            }],
    )

    return chat_completion.choices[0].message.content or None
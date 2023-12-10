import openai

""" with open('API.txt') as file:
    openai.api_key = file.read() """
openai.api_key = "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"

def get_api_response(prompt: str) -> str | None:
    text: str | None = None

    try:
        response: dict = openai.Completion.create(
            model='gpt-3.5-turbo-0613',
            prompt=prompt,
            temperature=0.9,            # randomness of bot -> higher = more random
            max_tokens=150,             # short answer
            top_p=1,                    # alternative to temperature -> lower = less random
            frequency_penalty=0,        # repetitiveness
            presence_penalty=0.6,       # talk about new subject
            stop=[' Human:', ' AI:']
        )

        print(response)
    except Exception as e:
        print("ERROR: ", e)

prompt="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: I'd like to cancel my subscription.\nAI:"
get_api_response(prompt)
from decouple import config
from openai import OpenAI

OPENAI_API_KEY = config("OPENAI_API_KEY", cast=str, default=None)
OPENAI_MODEL = "deepseek-chat"


def get_clinet():
    return OpenAI(api_key=OPENAI_API_KEY, base_url="https://api.deepseek.com")


def get_llm_response(get_message):
    client = get_clinet()
    completion = client.chat.completions.create(
        model=OPENAI_MODEL, messages=get_message
    )
    return completion.choices[0].message.content

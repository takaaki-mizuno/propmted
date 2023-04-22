import os

import openai

from .base import Base


class OpenAI(Base):

    def __init__(self, model: str = "gpt-3.5-turbo", api_key: str = None):
        self.api_key = self._get_api_key(api_key)
        self.model = model

    @staticmethod
    def _get_api_key(api_key: str = None) -> str:
        if api_key is None:
            api_key = os.getenv("OPENAI_API_KEY")
        if api_key is None:
            raise ValueError("No API key provided")
        return api_key

    def complete(self, prompt: str) -> str:
        openai.api_key = self._get_api_key(self.api_key)
        response = openai.ChatCompletion.create(model=self.model,
                                                messages=[
                                                    {
                                                        "role": "user",
                                                        "content": prompt
                                                    },
                                                ])
        return response["choices"][0]["message"]["content"]

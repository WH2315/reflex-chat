from typing import List
import reflex as rx

from . import ai


class ChatMessage(rx.Base):
    message: str
    is_bot: bool = False


class ChatState(rx.State):
    did_submit: bool = False
    message: List[ChatMessage] = []

    @rx.var
    def user_did_submit(self) -> bool:
        return self.did_submit

    def append_message(self, message, is_bot: bool = False):
        self.message.append(ChatMessage(message=message, is_bot=is_bot))

    def get_gpt_message(self):
        gpt_message = [
            {
                "role": "system",
                "content": "You are a helpful assistant that answers questions and provides information.",
            }
        ]
        for chat_message in self.message:
            role = "user"
            if chat_message.is_bot:
                role = "system"
            gpt_message.append({"role": role, "content": chat_message.message})
        return gpt_message

    async def handle_submit(self, form_data: dict):
        print(form_data)
        user_message = form_data.get("message")
        if user_message:
            self.did_submit = True
            self.append_message(user_message, is_bot=False)
            yield
            gpt_message = self.get_gpt_message()
            bot_response = ai.get_llm_response(gpt_message)
            self.did_submit = False
            self.append_message(bot_response, is_bot=True)
            yield

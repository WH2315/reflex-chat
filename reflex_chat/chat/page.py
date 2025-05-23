import reflex as rx

from reflex_chat import ui

from .form import chat_form
from .state import ChatMessage, ChatState

message_style = dict(
    display="inline-block",
    padding="1em",
    border_radius="8px",
    max_width=["30em", "30em", "50em", "50em", "50em", "50em"],
)


def message_box(chat_message: ChatMessage):
    return rx.box(
        rx.box(
            rx.markdown(
                chat_message.message,
                background_color=rx.cond(
                    chat_message.is_bot, rx.color("mauve", 4), rx.color("blue", 4)
                ),
                color=rx.cond(
                    chat_message.is_bot, rx.color("mauve", 12), rx.color("blue", 12)
                ),
                **message_style,
            ),
            text_align=rx.cond(
                chat_message.is_bot,
                "left",
                "right",
            ),
            margin_top="1em",
        ),
        width="100%",
    )


def chat_page():
    return ui.base_layout(
        rx.vstack(
            rx.heading("Chat Here", size="9"),
            rx.box(
                rx.foreach(ChatState.message, message_box),
                width="100%",
            ),
            chat_form(),
            margin="3rem auto",
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
    )

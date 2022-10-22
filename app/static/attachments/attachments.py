import app.static.localizations.en as l_en
from aiogram.types.inline_keyboard import InlineKeyboardMarkup as markup
from aiogram.types.inline_keyboard import InlineKeyboardButton as button


def authorization_inline_button(url: str):
    return (
        markup(row_width=1)
        .add(button(text=l_en.b_authorise, url=url))
    )

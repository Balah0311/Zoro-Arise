from pyrogram.types import InlineKeyboardButton

import config
from VIPMUSIC import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
        ],
        [
            InlineKeyboardButton(text="۞ 𝐇𝙴𝙻𝙿 ۞", callback_data="settings_back_helper"),
            InlineKeyboardButton(text="☢ 𝐒𝙴𝚃 ☢", callback_data="settings_helper"),
        ],
        [
            InlineKeyboardButton(text="🍭 𝐆ʀᴏᴜᴘ ✨", url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="😍 𝐓ᴀᴋᴇ 𝐌ᴇ 𝐁ᴀʙʏ 🤌🏻 😻",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text="🍭 𝐆ʀᴏᴜᴘ ✨", url=config.SUPPORT_CHAT),
            InlineKeyboardButton(text="𝐌ᴏʀᴇ🥀", url=config.SUPPORT_CHANNEL),
        ],
        [
            InlineKeyboardButton(
                text="❤️‍🔥 𝐅ᴇᴀᴛᴜʀᴇs ❤️‍🔥", callback_data="settings_back_helper"
            )
        ],
    ]
    return buttons

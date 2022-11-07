from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from Alone.config import BOT_USERNAME
from Alone.config import START_PIC
from Alone.config import OWNER_ID
from Alone.config import ASSUSERNAME
from Alone.config import UPDATE
from Alone.config import SUPPORT
from Alone.config import OWNER_USERNAME
from Alone.config import BOT_NAME


@Client.on_callback_query(filters.regex("cbhome"))
async def cbhome(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""Hi [👋]({START_PIC}) I'm **{BOT_NAME}**

You Can Use Alone Play Music In Your Groups.

Use Inline Buttons Given Below To Know More About Serena!!""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "❓ About", callback_data="cbabout"),
                    InlineKeyboardButton(
                        "🔰 Others", callback_data="others")
                ],
                [
                    InlineKeyboardButton(
                        "📚 Commands & Help", callback_data="cbevery")
                ],
                [
                    InlineKeyboardButton(
                        "✚ Add Me To Your Group ✚", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ]
                
           ]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds_set(_, query: CallbackQuery):
        await query.answer("commands menu")
        await query.edit_message_text(
        f"""Hi 👋 [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) 

Check Out All The Commands Given Below By Click On The Given Inline Buttons !!""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Sudo Users", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("Everyone", callback_data="cbevery"),
                    InlineKeyboardButton("Group Admins", callback_data="cbadmins"),
                ],[
                    InlineKeyboardButton("⬅️ Back", callback_data="cbhome")
                ],
            ]
        ),
    ) 


# Commands for Everyone !!
@Client.on_callback_query(filters.regex("cbevery"))
async def all_set(_, query: CallbackQuery):
    await query.answer("× Help Menu")
    await query.edit_message_text(
    f"""× /play (song name) or (YT link)
- plays the song in voice chat of your group 

× /song (song name) or (YT link)
- Downloads song in audio File 

× /tgm or /telegraph
- generate the link of given media

× /info 
- show all the information about a given user

× /search or /yt
- search link of the given song

× /ping
- Shows the ping message

× @AloneXRobot <query> 
- Get youtube url by inline mode""",
        reply_markup=InlineKeyboardMarkup(
            [
              [
                    InlineKeyboardButton(
                        "Admins", callback_data="cbadmins"),
                    InlineKeyboardButton(
                        "Sudo/Owner", callback_data="cbsudo")
                ],
              [InlineKeyboardButton("⬅️ Back", callback_data="cbhome")]]
        ),
    )


# Commands for SudoUsers
@Client.on_callback_query(filters.regex("cbsudo"))
async def sudo_set(_, query: CallbackQuery):
    await query.answer("sudo menu")
    await query.edit_message_text(
    f"""× /restart 
- restarts the bot in Heroku 

× /gcast 
- broadcast your message with pin in the served Chats

× /broadcast 
- broadcast your message without pin in the served chats

× /exec <code> 
- Execute any Code given by a sudo user of the bot

× /stats
- shows the Bot's system stats

× /userbotleaveall
- force the music assistant of the bot to leave all the served Chats""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⬅️ Back", callback_data="cbevery")
                ],
            ]
        ),
    )


# Commands for Group Admins
@Client.on_callback_query(filters.regex("cbadmins"))
async def admin_set(_, query: CallbackQuery):
    await query.answer("admins menu")
    await query.edit_message_text(
    f"""× /skip 
- skips music in the voice Chat 

× /pause 
- Pause music in the voice chat 

× /resume 
- Resumes music in the voice Chat

× /end or /stop
- stop playing music in the group's voice chat

× /cleandb
- Clears all raw files in your group which is uploaded by bot

× /userbotjoin
- invites the music assistant of the bot in your group

× /userbotleave
- Bot's music assistant will leaves your group""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⬅️ Back", callback_data="cbevery")
                ],
            ]
        ),
    )


# Bot about & Information
@Client.on_callback_query(filters.regex("cbabout"))
async def about_set(_, query: CallbackQuery):
    await query.edit_message_text(
    f"""Hi 👋 [{query.message.chat.first_name}](tg://user?id={query.message.chat.id})

Click On The Given Inline Buttons To Know All The Information About 𝐌𝐚𝐫𝐬𝐡𝐚𝐥𝐥 !!""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("📨 Support", url=f"https://t.me/{SUPPORT}"),
                    InlineKeyboardButton("📨 Updates", url=f"https://t.me/{UPDATE}")
                ],[
                    InlineKeyboardButton("👤 Owner", url=f"https://t.me/{OWNER_USERNAME}"),
                    InlineKeyboardButton("🎸 Assistant", url=f"https://t.me/{ASSUSERNAME}")
                ],[
                    InlineKeyboardButton("🤖 Source Code", url="https://t.me/SerenaUpdates")
                ],[
                    InlineKeyboardButton("⬅️ Back", callback_data="cbhome")
                ],
            ]
        ),
    )


# OTHERS CALLBACK
@Client.on_callback_query(filters.regex("others"))
async def others(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""Powered By : @{UPDATE}

After You Played Your Song Some Menu Buttons Will Be Comes To Manage Your Music Playing On Voice Chat. All The Buttons Are As Follows :

× ⏸ 
- Resume Music
× ▶️
- Pause Music
× ⏹ 
- End Music
× ⏩
- Skip Music

Only admins can use this buttons📍""",
        reply_markup=InlineKeyboardMarkup(
            [
              [
                    InlineKeyboardButton("Support 🚶", url=f"https://t.me/{SUPPORT}"),
                    InlineKeyboardButton("Updates 🤖", url=f"https://t.me/{UPDATE}")
                ],
            [InlineKeyboardButton("Basic Guide & Full Set-up", callback_data="setup")],
            [InlineKeyboardButton("⬅️ Back", callback_data="cbhome")]]
        ),
    )

@Client.on_callback_query(filters.regex("setup"))
async def setup(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**Basic SetUp Guide for the Bot Usage :**


× Add this Bot in your Group.

× Promote it as an administrator with needed powers.

× Now send /play or /userbotjoin command to invite assistant id in your Chat.

× Your All the Set-Up is Done, Now enjoy your favourite music in your groups voice chat without any limitations.


Thanks !!
Please don't forget to Join our Group :
@{UPDATE}""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⬅️ Back", callback_data="others")
                ],
            ]
        ),
    )

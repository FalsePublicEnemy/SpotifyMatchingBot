import app.static.attachments.attachments as at
import app.static.localizations.en as loc
import app.spotify.utils as sp
from app.log import logger
from main import dp

from aiogram import types


@dp.message_handler(commands=['start'])
async def start(message: types.Message) -> None:
    """Get authorisation url for application"""

    auth = sp.get_auth(username=message.chat.username)
    await message.reply(
        text=loc.f_authorization.format(name=message.chat.first_name),
        reply_markup=at.authorization_inline_button(auth.get_authorize_url()),
    )


@dp.message_handler(commands=['authorise'])
async def authorise(message: types.Message) -> None:
    auth = sp.get_auth(username=message.chat.username)
    auth._get_auth_response_local_server
    auth.get_auth_response(open_browser=True)
    logger.info('Auth')


@dp.message_handler(commands=['next_track', 'previous_track', 'pause', 'play'])
async def modify_playback(message: types.Message) -> None:
    """Skip playback to next track"""

    client = sp.get_client(username=message.chat.username)
    playback = {
        '/next_track': ('Track skipped', client.next_track),
        '/previous_track': ('Track skipped', client.previous_track),
        '/pause': ('Playback is paused', client.pause_playback),
        '/play': ('Playback is starting', client.start_playback),
    }[message.text]
    
    playback[-1]()
    await message.reply(text=playback[0])
    logger.info(f'Playback modified for {message.chat.username}')


@dp.message_handler(commands=['match_playlist'])
async def match_playlist(message: types.Message) -> None:
    ...

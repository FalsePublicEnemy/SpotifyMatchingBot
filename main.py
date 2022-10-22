import os
import aiogram

from app.log import logger
from app.config import *

sender = aiogram.Bot(token=os.environ.get('BOT_TOKEN'))
dp = aiogram.Dispatcher(sender)

from app.bot.views import *

if __name__ == '__main__':

    aiogram.executor.start_polling(dp, skip_updates=True)
    
    logger.info('Bot Started')

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from common.files.menu import private
import asyncio

token = '6495698589:AAF8IrqRoPuEERHNFztOqnikDtxL_xDBU10'
bot = Bot(token, parse_mode=ParseMode.HTML)
dp = Dispatcher()
commanda = Router()
dp.include_router(commanda)



'''
@commanda.message(Command('info'))
async def mes(message: types.Message) -> None:
    with open(r'common\files\data.json', 'r') as f:
        text = f.read()
    print('error')
    await message.answer(text)
'''

@commanda.message()
async def me(message: types.Message) -> None:
    a = str(message.text)
    with open(r'common\files\text.text', 'a', encoding='utf-8') as f:
        f.write(f'{a} \n')
    await bot.send_message(5270716903, a) #отправляет мне текст сообщений отправленных боту
    print(a)


async def main() -> None:
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.delete_webhook()
    await bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot)


def n():
    asyncio.run(main())

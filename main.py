import os
from telebot import TeleBot
from dotenv import load_dotenv
from telebot.types import Message

# Load environment variables
load_dotenv()
TELEGRAM_BOT_TOKEN: str = os.getenv('TELEGRAM_BOT_TOKEN')




import re
import asyncio
import logging
import smtplib
import random
from asyncio import sleep
from datetime import datetime

import requests
import sms as sms
import aiohttp

import certifi
from bs4 import BeautifulSoup
from core.utils.commands import COMMANDS
import core.utils.states as st
from aiogram import Dispatcher
import core.utils.keyboards as kb

from aiogram import Bot, Router, F
from aiogram.enums import ParseMode
import core.database.requests as req
from email.mime.text import MIMEText
from datetime import datetime, timedelta
from aiogram.fsm.context import FSMContext
from email.mime.multipart import MIMEMultipart
from core.middlewares.db import DataBaseSession
from sqlalchemy.ext.asyncio import AsyncSession
from aiogram.filters import Command, StateFilter
from aiogram.client.default import DefaultBotProperties
from core.database.models import async_main, async_session
from aiogram.types import Message, CallbackQuery


import uuid
import ssl
from urllib.parse import quote_plus
###################################################################################################
private = Router()
###################################################################################################
from colorama import init, Fore, Style, Back
init(autoreset=True)
###################################################################################################
###################################################################################################
class EnterSMS:
    def __init__(self, login: str, password: str, connect_id: str):
        self.login = login
        self.password = password
        self.connect_id = connect_id
        self.url = f"https://xml.smstec.ru/api/v3/easysms/{connect_id}/SendMessage"

    async def send_sms(self, phone_number: str, text_message: str) -> dict:
        """
        Отправка SMS через EasySMS API v3
        """
        payload = {
            "Header": {
                "login": self.login,
                "password": self.password
            },
            "Payload": {
                "message": {
                    "client_message_id": f"msg_{uuid.uuid4().hex[:8]}",  # уникальный ID
                    "messenger_type": "sms",
                    "originator": "gosinfobot",
                    "recipient": phone_number,
                    "text": text_message
                }
            }
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(self.url, json=payload) as resp:
                return await resp.json()  # вернём как словарь

# Инициализация клиента
sms_client1 = EnterSMS(
    login="Boostra_service",
    password="Uu9WcVog",
    connect_id="3131"
)

# Универсальная функция, которую можно вызывать где угодно
async def sender_enter_sms(phone: str, text: str):
    result = await sms_client1.send_sms(phone, text)
    if "error" in result:
        return {"status": "error", "details": result}
    return {"status": "success", "details": result}
###################################################################################################
class BoostraSMS:
    def __init__(self, login: str, password: str, connect_id: str):
        self.login = login
        self.password = password
        self.connect_id = connect_id
        self.url = f"https://xml.smstec.ru/api/v3/easysms/{connect_id}/SendMessage"

    async def send_sms(self, phone_number: str, text_message: str) -> dict:
        """
        Отправка SMS через EasySMS API v3
        """
        payload = {
            "Header": {
                "login": self.login,
                "password": self.password
            },
            "Payload": {
                "message": {
                    "client_message_id": f"msg_{uuid.uuid4().hex[:8]}",  # уникальный ID
                    "messenger_type": "sms",
                    "originator": "Boostra",
                    "recipient": phone_number,
                    "text": text_message
                }
            }
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(self.url, json=payload) as resp:
                return await resp.json()  # вернём как словарь

# Инициализация клиента
sms_client2 = BoostraSMS(
    login="Boostra_service",
    password="Uu9WcVog",
    connect_id="3131"
)

# Универсальная функция, которую можно вызывать где угодно
async def sender_boostra_sms(phone: str, text: str):
    result = await sms_client2.send_sms(phone, text)
    if "error" in result:
        return {"status": "error", "details": result}
    return {"status": "success", "details": result}
###################################################################################################
class CreditSMS:
    def __init__(self, login: str, password: str, connect_id: str):
        self.login = login
        self.password = password
        self.connect_id = connect_id
        self.url = f"https://xml.smstec.ru/api/v3/easysms/{connect_id}/SendMessage"

    async def send_sms(self, phone_number: str, text_message: str) -> dict:
        """
        Отправка SMS через EasySMS API v3
        """
        payload = {
            "Header": {
                "login": self.login,
                "password": self.password
            },
            "Payload": {
                "message": {
                    "client_message_id": f"msg_{uuid.uuid4().hex[:8]}",  # уникальный ID
                    "messenger_type": "sms",
                    "originator": "gosinfobot",
                    "recipient": phone_number,
                    "text": text_message
                }
            }
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(self.url, json=payload) as resp:
                return await resp.json()  # вернём как словарь

# Инициализация клиента
sms_client3 = CreditSMS(
    login="Boostra_service",
    password="Uu9WcVog",
    connect_id="3131"
)

# Универсальная функция, которую можно вызывать где угодно
async def sender_credit_sms(phone: str, text: str):
    result = await sms_client3.send_sms(phone, text)
    if "error" in result:
        return {"status": "error", "details": result}
    return {"status": "success", "details": result}
###################################################################################################
class EnterFIN:
    def __init__(self, login: str, password: str, connect_id: str):
        self.login = login
        self.password = password
        self.connect_id = connect_id
        self.url = f"https://xml.smstec.ru/api/v3/easysms/{connect_id}/SendMessage"

    async def send_sms(self, phone_number: str, text_message: str) -> dict:
        """
        Отправка SMS через EasySMS API v3
        """
        payload = {
            "Header": {
                "login": self.login,
                "password": self.password
            },
            "Payload": {
                "message": {
                    "client_message_id": f"msg_{uuid.uuid4().hex[:8]}",  # уникальный ID
                    "messenger_type": "sms",
                    "originator": "fin_info",
                    "recipient": phone_number,
                    "text": text_message
                }
            }
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(self.url, json=payload) as resp:
                return await resp.json()  # вернём как словарь

# Инициализация клиента
sms_clientFin = EnterFIN(
    login="Boostra_service",
    password="Uu9WcVog",
    connect_id="3131"
)

# Универсальная функция, которую можно вызывать где угодно
async def sender_enter_fin_sms(phone: str, text: str):
    result = await sms_clientFin.send_sms(phone, text)
    if "error" in result:
        return {"status": "error", "details": result}
    return {"status": "success", "details": result}
########################################################################################
class GosSafe:
    def __init__(self, login: str, password: str, connect_id: str):
        self.login = login
        self.password = password
        self.connect_id = connect_id
        self.url = f"https://xml.smstec.ru/api/v3/easysms/{connect_id}/SendMessage"

    async def send_sms(self, phone_number: str, text_message: str) -> dict:
        """
        Отправка SMS через EasySMS API v3
        """
        payload = {
            "Header": {
                "login": self.login,
                "password": self.password
            },
            "Payload": {
                "message": {
                    "client_message_id": f"msg_{uuid.uuid4().hex[:8]}",  # уникальный ID
                    "messenger_type": "sms",
                    "originator": "gossaferu",
                    "recipient": phone_number,
                    "text": text_message
                }
            }
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(self.url, json=payload) as resp:
                return await resp.json()  # вернём как словарь

# Инициализация клиента
sms_client4 = GosSafe(
    login="Boostra_service",
    password="Uu9WcVog",
    connect_id="3131"
)

# Универсальная функция, которую можно вызывать где угодно
async def sender_gossafe_sms(phone: str, text: str):
    result = await sms_client4.send_sms(phone, text)
    if "error" in result:
        return {"status": "error", "details": result}
    return {"status": "success", "details": result}
########################################################################################
class GosHelper:
    def __init__(self, login: str, password: str, connect_id: str):
        self.login = login
        self.password = password
        self.connect_id = connect_id
        self.url = f"https://xml.smstec.ru/api/v3/easysms/{connect_id}/SendMessage"

    async def send_sms(self, phone_number: str, text_message: str) -> dict:
        """
        Отправка SMS через EasySMS API v3
        """
        payload = {
            "Header": {
                "login": self.login,
                "password": self.password
            },
            "Payload": {
                "message": {
                    "client_message_id": f"msg_{uuid.uuid4().hex[:8]}",  # уникальный ID
                    "messenger_type": "sms",
                    "originator": "goshelperru",
                    "recipient": phone_number,
                    "text": text_message
                }
            }
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(self.url, json=payload) as resp:
                return await resp.json()  # вернём как словарь

# Инициализация клиента
sms_client5 = GosHelper(
    login="Boostra_service",
    password="Uu9WcVog",
    connect_id="3131"
)

# Универсальная функция, которую можно вызывать где угодно
async def sender_goshelper_sms(phone: str, text: str):
    result = await sms_client5.send_sms(phone, text)
    if "error" in result:
        return {"status": "error", "details": result}
    return {"status": "success", "details": result}
########################################################################################
def get_operator_info(number: str):
    number = number.strip()
    url = f"https://htmlweb.ru/json/mnp/phone/{number}"

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        ),
        "Accept": "application/json",
        "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
        "Referer": "https://htmlweb.ru",
    }

    r = requests.get(url, headers=headers, timeout=10)
    r.raise_for_status()
    data = r.json()  # получаем JSON сразу как dict

    # вытаскиваем нужные поля
    region = data.get("region", {}).get("name", "Не найден")
    operator_name = data.get("oper", {}).get("name", "")
    

    # если есть бренд — добавляем к имени
    operator = operator_name or "Не найден"

    return {
        "number": number,
        "region": region,
        "operator": operator
    }

    
###################################################################################################
async def normalize_phone(phone: str) -> str:
    """
    Убирает все спецсимволы и оставляет только цифры
    """
    digits = re.sub(r"\D", "", phone)
    return digits
###################################################################################################
@private.callback_query(StateFilter('*'), F.data == 'delete')
async def delete_message_callback(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.answer()
    await callback.message.delete()
###################################################################################################
TIME = datetime.now()
DATE = TIME.strftime('%d.%m.%Y')
JUST_TIME = TIME.strftime('%H:%M')
###################################################################################################
class ColorFormatter(logging.Formatter):
    def format(self, record):
        msg = super().format(record)
        if "is handled" in msg:
            return Fore.GREEN +"✅" + Style.RESET_ALL
        elif "is not handled" in msg:
            return Fore.RED +"❌" + Style.RESET_ALL
        return msg

formatter = ColorFormatter("[%(levelname)s] %(message)s")
handler = logging.StreamHandler()
handler.setFormatter(formatter)

# Aiogram logger
aiogram_logger = logging.getLogger("aiogram")
aiogram_logger.setLevel(logging.INFO)
aiogram_logger.addHandler(handler)
###################################################################################################
async def format_number(number: int) -> str:
    return f"{number:,}".replace(",", " ")
###################################################################################################
@private.message(Command('id'))
async def id(message: Message):
    del_message = message.message_id
    await message.answer(f'TG ID  <code>{message.from_user.id}</code>',
                          reply_markup=kb.delete_mess)    
    if message.message_id == del_message:
        await message.delete() 
###################################################################################################
@private.message(Command('cid'))
async def cid(message: Message):
    del_message = message.message_id
    await message.answer(f'TG Chat ID <code>{message.chat.id}</code>',
                          reply_markup=kb.delete_mess)    
    if message.message_id == del_message:
        await message.delete() 
###################################################################################################

# GosInfoBot #1
@private.message(Command('go'))
async def gosinfobot_1(message: Message, session, state: FSMContext):
    # if message.from_user.id == 8462198689:
    #     await state.set_state(st.gosinfobot.wait_phone)
    #     await message.answer(
    #         f'Направь мне номер получателя в формате <b>79991234567</b>:\n\n'
    #         f'<i>либо жми <b>Отмену</b>*</i>',
    #         reply_markup=await kb.cancel_button_sms()
    #     )
    
    if message.from_user.id == 7702371128: # 7937601695
        await state.set_state(st.gosinfobot.wait_phone)
        await message.answer(
            f'Создатель\n\n'
            f'Направь мне номер получателя в формате <b>79991234567</b>:\n\n'
            f'<i>либо жми <b>Отмену</b>*</i>',
            reply_markup=await kb.cancel_button_sms()
        )

    else:
        await message.answer('???')
        await state.clear()



# GosInfoBot #2
# @private.message(st.gosinfobot.wait_phone)
# async def gosinfobot_2(message: Message, session, state: FSMContext):
    
#     # info = get_operator_info(num)
#     await state.update_data(phone=message.text)
#     await state.set_state(st.gosinfobot.wait_message)
#     await message.answer(
#         f'Получатель: <b>{message.text}</b>\n\n'
#         f'Направь мне <b>текст сообщения</b> (одним сообщением)\n\n'
#         f'<i>либо жми <b>Отмену</b>*</i>',
#         reply_markup=await kb.cancel_button_sms()
#     )

@private.message(st.gosinfobot.wait_phone)
async def gosinfobot_2(message: Message, session, state: FSMContext):
    phone_raw = message.text.strip()

    # # убираем всё, кроме цифр
    # digits = ''.join(filter(str.isdigit, phone_raw))

    # # если номер начинается с 7 или 8 — убираем только первую цифру
    # if digits.startswith(('7', '8')) and len(digits) > 10:
    #     num = digits[1:]
    # else:
    #     num = digits

    # получаем инфу об операторе
    info = get_operator_info(phone_raw)

    # сохраняем номер в state (можешь сохранить исходный, если нужно)
    await state.update_data(phone=message.text)

    # устанавливаем следующее состояние
    await state.set_state(st.gosinfobot.wait_message)
    await state.update_data(oper=info["operator"])

    # формируем сообщение
    await message.answer(
        f"Получатель: <b>{message.text}</b>\n\n"
        f"Оператор: <b>{info["operator"]}</b>\n\n"
        f"Теперь направь <b>текст сообщения</b> (одним сообщением)\n\n"
        f"<i>либо жми <b>Отмену</b>*</i>",
        reply_markup=await kb.cancel_button_sms()
    )
    
# GosInfoBot #3
@private.message(st.gosinfobot.wait_message)
async def gosinfobot_3(message: Message, session, state: FSMContext):
    await state.update_data(message_text=message.text)
    data = await state.get_data()
    operator = data['oper']
    phone = data['phone']
    message_text = data['message_text']
    await state.set_state(st.gosinfobot.send_confirm)

    await message.answer(
        f'Получатель: +{phone}\n\n'
        f"Оператор: <b>{operator}</b>\n\n"  
        f'Текст: {message_text}',
        reply_markup=await kb.send_sms_button_choose()
    )

# GosInfoBot #4
@private.callback_query(st.gosinfobot.send_confirm)
async def gosinfobot_4(callback: CallbackQuery, session, state: FSMContext):
    await callback.answer()
    time = datetime.now()
    date = time.strftime('%d.%m.%Y')
    just_time = time.strftime('%H:%M:%S')

    data = await state.get_data()
    user_phone = data['phone']
    message_text = data['message_text']

    if callback.data == 'send_gosinfobot':
        await sms.sender_credit_sms(phone=user_phone, text=message_text)
        sender = 'GosInfoBot'

    elif callback.data == 'send_goshelperru':
        await sms.sender_goshelper_sms(phone=user_phone, text=message_text)
        sender = 'GosHelperRu'

    elif callback.data == 'send_gossaferu':
        await sms.sender_gossafe_sms(phone=user_phone, text=message_text)
        sender = 'GosSafeRu'

    elif callback.data == 'send_fin_info':
        await sms.sender_enter_fin_sms(phone=user_phone, text=message_text)
        sender = 'Fin_Info'

    elif callback.data == 'send_boostra':
        await sms.sender_boostra_sms(phone=user_phone, text=message_text)
        sender = 'Boostra'

    sms_data = {
                'tg_id': callback.from_user.id,
                'date_send': date,
                'time_send': just_time,
                'phone': user_phone,
                'text': message_text,
                'domen': sender
                }
    
    await req.add_sms_count(session, sms_data)
    
    records = await req.sms_today_how_much(session, date)
    count = len(records)
    print(Fore.WHITE + f'{count}' + Style.RESET_ALL)
    
    await callback.message.edit_text(
        f'{callback.message.text}\n\n'
        f'✅ <b>Сообщение отправлено</b>'
    )
    await state.clear()
###################################################################################################
@private.message(Command("count"))
async def count_sms(message: Message, session):
    args = message.text.split(maxsplit=1)  # делим команду и аргумент

    # Если пользователь не указал дату
    if len(args) < 2:
        return await message.answer("❗ Укажи дату в формате <b>ДД.ММ.ГГГГ</b>\n\nПример: <code>/count 04.11.2025</code>")

    date = args[1].strip()

    # Проверяем правильность формата
    try:
        datetime.strptime(date, "%d.%m.%Y")
    except ValueError:
        return await message.answer("⚠️ Неверный формат даты.\nИспользуй формат <b>ДД.ММ.ГГГГ</b>")

    # Запрашиваем записи из базы
    records = await req.sms_today_how_much(session, date)
    count = len(records)
    just_time = datetime.now().strftime("%H:%M:%S")

    await message.answer(
        f"📅 {date} ⏰ {just_time}\n\n"
        f"📊 Отправлено SMS за этот день: <b>{count}</b> шт."
    )
###################################################################################################
async def main():
    await async_main()
    bot = Bot(token=TELEGRAM_BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()
    dp.update.middleware(DataBaseSession(session_pool=async_session))
    dp.include_routers(private)
    print(Fore.MAGENTA + Style.BRIGHT + "bot was started" + Style.RESET_ALL)
    await bot.set_my_commands(commands=[])
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
###################################################################################################
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(Fore.MAGENTA + Style.BRIGHT + "bot was stopped" + Style.RESET_ALL)
###################################################################################################


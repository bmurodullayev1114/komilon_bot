import logging

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from data.config import ADMINS, CHANNELS
from keyboards.inline.manage_post import confirmation_keyboard, post_callback
from loader import dp, bot
from states.newpost import NewPost


@dp.message_handler(Command("yangi_elon"))
async def create_post(message: types.Message):
    await message.answer("Chop etish uchun e'lon yuboring !\n"
                         "\n"
                         "E'lon joylashtirish uchun: \n"
                         "1. Rasm:\n"
                         "2. Mahsulot nomi: (#Beda_press)\n"
                         "3. Holati: (Yangi yoki yil oshgan)\n"
                         "4. Narxi: (25000)\n"
                         "5. #Aloqa: (tel nomer-998914567891)\n"
                         "\n"
                         )
    await NewPost.NewMessage.set()


@dp.message_handler(state=NewPost.NewMessage, content_types = types.ContentTypes.ANY)
async def enter_message(message: Message, state: FSMContext):
    await state.update_data(text=message.html_text, mention=message.from_user.get_mention())
    await message.answer(f"E'lonni tekshirish uchun yuboraymi?",
                         reply_markup=confirmation_keyboard)
    await NewPost.next()


@dp.callback_query_handler(post_callback.filter(action="post"), state=NewPost.Confirm)
async def confirm_post(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        text = data.get("text")
        mention = data.get("mention")
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("E'lon Adminga yuborildi")
    await bot.send_message(ADMINS[0], f"Foydalanuvchi {mention} quyidagi e'lonni chop etmoqchi:")
    await bot.send_message(ADMINS[0], text, parse_mode="HTML", reply_markup=confirmation_keyboard)


@dp.callback_query_handler(post_callback.filter(action="cancel"), state=NewPost.Confirm)
async def cancel_post(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("E'lon rad etildi.")


@dp.message_handler(state=NewPost.Confirm)
async def post_unknown(message: Message):
    await message.answer("Chop etish yoki rad etishni tanlang")


@dp.callback_query_handler(post_callback.filter(action="post"), user_id=ADMINS)
async def approve_post(call: CallbackQuery):
    await call.answer("Chop etishga ruhsat berdingiz.", show_alert=True)
    target_channel = CHANNELS[0]
    message = await call.message.edit_reply_markup()
    await message.send_copy(chat_id=target_channel)


@dp.callback_query_handler(post_callback.filter(action="cancel"), user_id=ADMINS)
async def decline_post(call: CallbackQuery):
    await call.answer("E'lon rad etildi.", show_alert=True)
    await call.message.edit_reply_markup()

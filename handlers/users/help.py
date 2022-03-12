from cgitb import text

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp

@dp.message_handler(text="/help")
async def bot_help(message: types.Message):
    await message.reply(
        "Ushbu bot sizga 'Komilon Savdo' kanalida e'lon joylashtirishingizga yordam beradi !\n"
        "\n"
        "E'lon joylashtirish uchun: \n"
        "1. Rasm:\n"
        "2. Mahsulot nomi: (#Beda_press)\n"
        "3. Holati: (Yangi yoki yil oshgan)\n"
        "4. Narxi: (25000)\n"
        "5. #Aloqa: (tel nomer-998914567891)\n"
        "\n"
        "Yangi e'lon berish uchun /yangi_elon buyrug'ini bosing !"
        )
#    await message.answer("\n".join(text))
#@dp.message_handler(CommandHelp())
#async def bot_help(message: types.Message):
#    text = ("Buyruqlar: ",
#            "/start - Botni ishga tushirish",
#            "/help - Yordam",
#            "/yangi_elon - Yangi e'lon yuborish",)


    
#    await message.answer("\n".join(text))
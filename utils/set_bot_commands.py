from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand(command="start", description="Botni ishga tushurish"),
            types.BotCommand(command="help", description="Yordam"),
            types.BotCommand(command="menu", description="Bosh menyu"),
            types.BotCommand(command='set_language', description="Tilni o'zgartirish")
        ]
    )

from aiogram import Router, filters, types
from utils.constants import START_MESSAGE

router = Router()

@router.message(filters.CommandStart())
async def start_handler(message: types.Message):
    await message.answer(START_MESSAGE)

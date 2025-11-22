from math import lgamma

from aiogram import Router, filters, types

from config.settings import PAYMENT_TOKEN
from utils.constants import PRICES

router = Router()


@router.message(filters.Command('buy'))
async def buy_handler(message: types.Message):
    await message.bot.send_invoice(
        chat_id=message.from_user.id,
        title='Премиум подписка',
        description="Доступ к эксклюзивному контенту",
        payload="premium-access",
        provider_token=PAYMENT_TOKEN,
        currency='RUB',
        prices=PRICES,
        photo_url='https://i.pinimg.com/originals/47/8e/a4/478ea4c3f766b96aa23d87383d1bf3cd.jpg'
    )

@router.pre_checkout_query()
async def pre_checkout_query_handler(query: types.PreCheckoutQuery):
    await query.answer(ok=True)


@router.message(lambda message: message.successful_payment is not None)
async def successful_payment_handler(message: types.Message):
    await message.answer('Оплата успешно завершена!')

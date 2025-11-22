from aiogram import Router

router = Router()

from handlers.payment_handler import router as payment_router
router.include_router(payment_router)

from handlers.start_handler import router as start_router
router.include_router(start_router)

import logging
from random import randint

from aiogram import Bot

from db.requests.pincode import add_pincode, get_pincode, update_used_pincode

MIN_PINCODE = 1000
MAX_PINCODE = 9999

logger = logging.getLogger(__name__)

async def create_pincode(attempts: int = 10) -> int | None:
    logger.debug('create_pincode')

    while attempts > 0:
        pincode = randint(MIN_PINCODE, MAX_PINCODE)
        inserted = await add_pincode(pincode)
        if inserted:
            return pincode
        attempts -= 1
    return None

async def get_pincode_now() -> int | None:
    logger.debug('get_pincode_now')

    pincode = await create_pincode()
    if pincode:
        return pincode
    else:
        return None

async def is_pincode_right(payload: str) -> bool:
    logger.debug('is_pincode_right')

    pincode = int(payload)
    result = await get_pincode(pincode)

    if result and not result.is_used:
        await update_used_pincode(pincode)
        return True
    else: return False
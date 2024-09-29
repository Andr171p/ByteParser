import json
import time
import datetime

from aiogram.types import Message


def json_to_dict(_json: str) -> dict:
    _json = json.dumps(_json, ensure_ascii=False)
    _dict = json.loads(_json)
    return _dict


def bytes_to_json(_bytes: bytes) -> str:
    _json = json.loads(_bytes)
    return _json


def get_user_data(message: Message) -> tuple[int, str]:
    user_id = message.from_user.id
    username = message.from_user.username
    return user_id, username


def timestamp() -> int:
    return int(time.time())


def today() -> str:
    _today = datetime.date.today().isoformat()
    return _today


def calculate_timeout(
        hour: int, minute: int, second: int, microsecond: int
) -> int:
    now = datetime.datetime.now()
    future = now.replace(
        hour=hour,
        minute=minute,
        second=second,
        microsecond=microsecond
    )
    if future <= now:
        future += datetime.timedelta(days=1)
    timeout = int((future - now).total_seconds())
    return timeout


from random import choices, randint
from string import ascii_letters, digits
import uuid
from datetime import date, datetime

account_chars: str = digits + ascii_letters


def _genuid() -> str:
    uid = str(uuid.uuid4())
    return uid


def _random_account_id() -> str:
    return ''.join(choices(account_chars, k=12))


def _random_amount() -> float:
    return randint(-100000, 100000) / 100


def _current_date():
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    return d1


def _current_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time


def create_random_transaction() -> dict:
    return {
        'transaction_id': _genuid(),
        'source': _random_account_id(),
        'target': _random_account_id(),
        'amount': _random_amount(),
        'currency': 'KES',
        'date': _current_date(),
        'time': _current_time()
    }

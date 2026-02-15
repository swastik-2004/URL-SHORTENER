import random
import string
import validators
from app.models import URL

def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    while True:
        short_code = ''.join(random.choice(characters) for _ in range(length))
        if not URL.query.filter_by(short_code=short_code).first():
            return short_code

def is_valid_url(url):
    return validators.url(url)

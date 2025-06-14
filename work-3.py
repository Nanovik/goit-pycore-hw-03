import re

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

def normalize_phone(phone_number):
    pattern = r"[^\+\d]"
    replacement = ""
    phone_number_correct = re.sub(pattern, replacement, phone_number)
    if phone_number_correct.startswith("380"):
        phone_number_correct = "+" + phone_number_correct
    elif phone_number_correct.startswith("0"):
        phone_number_correct = "+38" + phone_number_correct
    return phone_number_correct

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
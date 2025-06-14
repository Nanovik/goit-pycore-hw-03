import random

min_int, max_int, quantity_int = 1, 49, 6

def get_numbers_ticket(min, max, quantity):
    if (isinstance(min, int) and isinstance(max, int) and isinstance(quantity, int)) \
        and (0 < min < 1000 and min < max <= 1000 and min < quantity < max):
        list_int = []
        while len(list_int) < quantity:
            number = random.randint(min, max)
            if number not in list_int:
                list_int.append(number)
        return list_int
    else:
        return "Ваші параметри не валідні, Прошу ввести нові, що відповідають умовам"

lottery_numbers = get_numbers_ticket(min_int, max_int, quantity_int)
if isinstance(lottery_numbers, list):
    lottery_numbers.sort()
    print("Ваші лотерейні числа:", lottery_numbers)
else:
    print(lottery_numbers)
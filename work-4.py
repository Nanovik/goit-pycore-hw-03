import datetime

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.06.15"},
    {"name": "Felix Kurt", "birthday": "1985.06.14"},
    {"name": "Sam Bolton", "birthday": "1990.06.16"}
]

def get_upcoming_birthdays(birthdays):
    congratulation_date =[]
    current_date = datetime.datetime.now().date()
    for user in birthdays:
        birthday_user = datetime.datetime.strptime(user.get("birthday"), "%Y.%m.%d").date()
        birthday_this_year = datetime.datetime(year = current_date.year, month=birthday_user.month, day=birthday_user.day).date()
        
        if birthday_this_year < current_date:
            congratulation_date_user = datetime.datetime(year = current_date.year + 1, month=birthday_user.month, day=birthday_user.day).date()
        else:
            congratulation_date_user = birthday_this_year
        
        if congratulation_date_user.weekday() == 5:
            congratulation_date_user = congratulation_date_user + datetime.timedelta(days=2)
        elif congratulation_date_user.weekday() == 6:
            congratulation_date_user = congratulation_date_user + datetime.timedelta(days=1)
        
        if congratulation_date_user.toordinal() - current_date.toordinal() < 7:
            user_congratulation = {'name': user.get("name"), \
                                'congratulation_date': congratulation_date_user.strftime("%Y.%m.%d")}
            congratulation_date.append(user_congratulation)
    return congratulation_date

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
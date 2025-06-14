import datetime

input_date_str = "2020-a10-09"

def get_days_from_today(date):
    try:
        date = datetime.datetime.strptime(input_date_str, "%Y-%m-%d")
        current_date = datetime.datetime.today()
        delta_time = current_date.toordinal() - date.toordinal()
        return delta_time
    except ValueError:
        return f" Некорректний формат дати: {input_date_str}\n Змініть її на такий формат (YYYY-MM-DD)"
    
print(get_days_from_today(input_date_str))
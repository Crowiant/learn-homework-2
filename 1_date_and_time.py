"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
import datetime as DT


def print_days():
    dt_now = DT.date.today()
    dt_yesterday = DT.timedelta(days=1)
    dt_thirty_days = DT.timedelta(days=30)
    return print(dt_now, (dt_now - dt_yesterday), (dt_now - dt_thirty_days))


def str_2_datetime(date_string):
    dt_method = DT.datetime.strptime(date_string, "%m/%d/%y %H:%M:%S.%f")
    return dt_method


if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))

from datetime import datetime
import logging

logging.basicConfig(filename='log4.log', encoding='utf-8', level=logging.ERROR)
log = logging.getLogger(__name__)


def text_to_date(text: str) -> datetime | None:
    try:
        count, week_day, month = text.split()
    except ValueError as e:
        log.error('Неверный формат строки!')
        return None

    days_list = ('пон', 'вто', 'сре', 'чет', 'пят', 'суб', 'вос')
    months_list = ('янв', 'фев', 'мар', 'апр', 'мая', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек')

    count = int(count[:-2])
    week_day = days_list.index(week_day[:3])
    month = months_list.index(month[:3]) + 1

    day_count = 0
    for day in range(1, 32):
        date = datetime(day=day, month=month, year=datetime.now().year)
        if date.weekday() == week_day:
            day_count += 1
            if day_count == count:
                return date


if __name__ == '__main__':
    print(text_to_date('1-й четверг ноября'))
    print(text_to_date('3-я среда мая'))
    print(text_to_date('среда1 июня'))

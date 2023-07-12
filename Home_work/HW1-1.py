MULT = 50
PERCENT = 0.015
EXTRA_PERCENT = 0.03
RICH_PERCENT = 0.1
MIN_CASH = 30
MAX_CASH = 600
MAX_COUNT = 3
MAX_SCORE = 5_000_000
count = 0
total_score = 50

def give_cash():
    return

def add_to_card(total_score, count):
    print("Укажите сумму для пополнения!")
    add_summa = int(input(""))
    if count > MAX_COUNT:
        add_summa *= EXTRA_PERCENT
        if add_summa % MULT == 0:
            total_score += add_summa
            print('Успешно!')
            print(f'Ваш баланс: {total_score}')
            count += 1
        else:
            print("Сумма должна быть кратна 50")
    else:
        return None


def start():

    print('Добро пожаловать в банкомат')
    print(f'Ваш баланс: {total_score}')
    print('Выберите операцию: ')

    print('''1. Просмотр баланса
2. Внесение денег
3. Снятие денег
4. Завершить работу
''')

    x = int(input(':'))
    while True:
        if x == 1:
            print(f'Баланс: {total_score}')

        elif x == 2:
            add_to_card(total_score, count)

        elif x == 3:
            give_cash(total_score, count)

        elif x == 4:
            print('Всего хорошего!')
            break
        else:
            continue

start()
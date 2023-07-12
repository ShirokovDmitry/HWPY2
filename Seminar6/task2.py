_result = {}

def questions(text: str, variants: list[str], counts: int) -> int:
    print('Отгадай загадку:')

    for count in range(1, counts + 1):
        x = input('Напишите ответ:')
        if x.lower() in variants:
            print('Правильный ответ!')
            return count
    print(f'Попытки закончились ({counts})')
    return 0



def guesses_dict(g_dict: dict[str, list[str]], count: int = 3) -> None:
    for key, value in g_dict.items():
        res = questions(key, value, count)
        result_score(key, res)
        print(f'\n Code {res}')

    printing_stat()


def result_score(txt: str, count_num: int) -> None:
    _result.update({txt: count_num})

def printing_stat():
    res = (f'Заг {key} отгадана за {value} попыток' if value > 0
           else f'Заг {key} не отгадана'
           for key, value in _result.items())
    print('Статистика\n')
    print('\n'.join(res))


# if __name__ == '__main__':
#     tex_riddle = 'Зимой и летом?'
#     count_num = 3
#     ans_ridle = ['Елка', 'Ёлка', 'ель', 'елка']


    # res = questions(tex_riddle, count_num, ans_ridle)
    # print(f'\n Code {res}')

if __name__ == '__main__':
    question = {'Зимой и летом?': ['Елка', 'Ёлка', 'ель', 'елка'],
                 'Зимой и летом??': ['Елка', 'Ёлка', 'ель', 'елка']}

    guesses_dict(question)




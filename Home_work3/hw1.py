# Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей.

camping_things = {
    'Igor': ('crackers', 'rabbit costume', 'gum', 'arrow target'),
    'Petr': ('magic wand', 'teddy bear', 'scary mask', 'arrow target'),
    'Masha': ('ice cream', 'arrow target', 'skis', 'teddy bear')
}

all_things = list(camping_things.values())
everyone_thing = set(all_things[0])
for items in all_things:
    everyone_thing = everyone_thing.intersection(set(items))
print(everyone_thing)

no_one_else = {}
for name, items in camping_things.items():
    no_one_else[name] = set(items).difference(everyone_thing)
print(no_one_else)
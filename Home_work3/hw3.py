# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.

text = 'Некоторые учёные считают, что кошка и вовсе не является одомашненным животным, ' \
       'а сама могла прийти к человеку, так как в селениях всегда в достатке водились синантропные' \
       ' животные или, проще говоря, многочисленные грызуны и птицы. Таким образом, кошка ' \
       'нашла для себя удобный источник пищи, закрепившись в «новой нише». Сосуществование человека ' \
       'и кошки было взаимовыгодным, так как человек избавлялся от грызунов, которые часто становились ' \
       'источником заболеваний и порчи хозяйства. Также весомым доводом противников идеи ' \
       'одомашнивания остаётся тот факт, что, по их мнению, кошка показывает любопытство к человеку только ' \
       'до тех пор, пока ей это выгодно, то есть маленький хищник не способен на верность. Другие же учёные' \
       ' продвигают иную точку зрения. По их мнению, тот факт, что кошки подвергались одомашниванию, подтверждается ' \
       'тем, что они способны на привязанность и игривое поведение, и именно для установления эмоционального контакта ' \
       'с человеком научились мурлыкать. Многие кошки показывают свою привязанность, устанавливая физический ' \
       'контакт с человеком, например, забираясь ему на колени; известны случаи, когда преданность кошки хозяину была ' \
       'сильнее, чем у многих собак, и это на фоне того, что кошки произошли из «опаснейших и неприветливейших' \
       ' хищников в мире». На негативный образ кошки как дикого и подозрительного животного повлиял и продолжает' \
       ' влиять тот факт, что в средневековой Европе Католическая церковь обвиняла кошек в связи с дьяволом' \
       ' и колдовством.'

word_count = {}
TEN = 10
srt_dict = {}
new_text = text.replace(',', ''). \
    replace('.', ''). \
    replace('!', ''). \
    replace('?', ''). \
    replace('"', ''). \
    lower(). \
    strip()
count_words = new_text.split()
for item in count_words:
    counter = count_words.count(item)
    word_count[item] = counter
sorted_values = sorted(word_count.values())[::-1]
for i in sorted_values:
    for k in word_count.keys():
        if word_count[k] == i:
            srt_dict[k] = word_count[k]

sorted_list = list(srt_dict.items())[:10]
print(sorted_list)
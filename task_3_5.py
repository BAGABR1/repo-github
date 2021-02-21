def get_jokes(n, key):
    """
    Генерирует заданное пользователем с клавиатуры количество шуток из случайного набора слов.
    Слова содержаться в трех списках и задаются изначально.
    """
    joke_list = []
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    i = 0
    from random import choice
    if key == 'да':
        while i < n:
            joke_list.append(choice(nouns))
            joke_list.append(choice(adverbs))
            joke_list.append(choice(adjectives))
            print(joke_list)
            joke_list = []
            i += 1
    if key == 'нет':
        if n > 5:
            n = int(input('Тогда количество шуток не должно быть больше пяти, введите новое количество шуток: '))
            while i < n:
                joke_list.append(choice(nouns))
                nouns.remove(joke_list[-1])
                joke_list.append(choice(adverbs))
                adverbs.remove(joke_list[-1])
                joke_list.append(choice(adjectives))
                adjectives.remove(joke_list[-1])
                print(joke_list)
                joke_list = []
                i += 1


get_jokes(int(input('Введите количество шуток : ')), input('можно или нельзя повторно использовать слова(да, нет): '))
print(help(get_jokes))

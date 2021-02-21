def num_translate_adv(word):
    eng_rec = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
               'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    for k, v in eng_rec.items():
        if word == k:
            print(v)
        if word == k.title():
            print(v.title())


num_translate_adv(input('введите числительное на английском языке: '))

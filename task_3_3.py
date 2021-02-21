def thesaurus(*args):
    names = {}
    names_list = []
    time_names = []
    for i in args:
        names_list.append(i[0])
    names_list = set(names_list)
    for i in names_list:
        for k in args:
            if i == k[0]:
                time_names.append(k)
        names[i] = time_names
        time_names = []
    print(names)


thesaurus("Иван", "Мария", "Петр", "Илья")

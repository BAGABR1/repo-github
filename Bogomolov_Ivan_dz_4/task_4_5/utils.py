def currency_rates(code):
    code = code.upper()
    index_1 = ''
    index_2 = ''
    from requests import get
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    if code == 'USD':
        index_1 = 'R01235'
        index_2 = 'R01239'
    if code == 'EUR':
        index_1 = 'R01239'
        index_2 = 'R01270'
    if code != 'USD' or 'EUR':
        return None
    val = float(str(response.content).split(index_1)[1].split(index_2)[0].split('Value')[1][1:-2].replace(',', '.'))
    print(f'1 {code} = {val} RUR')   # ^С помощью методов строк убираем все лишнее, заменяем запятую на точку
    date = str(response.content).split("Date=")[1][1:11]   # ^и преобразуем во float
    print(f'actual for {date}')


if __name__ == '__main__':
    currency_rates('USD')

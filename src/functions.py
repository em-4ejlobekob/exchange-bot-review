import config
import requests
import languages

from bs4 import BeautifulSoup


def str_to_num(str_num):
    str_num = '.'.join(str_num.split(','))
    if '.' in str_num and str_num.replace('.', '').isdigit():
        return float(str_num)
    elif str_num.isdigit():
        return int(str_num)
    else:
        return False


def transform_data():
    request = requests.get('https://www.cbr.ru/currency_base/daily/')
    html = BeautifulSoup(request.content, 'html.parser')
    html_data = str(html.select('.data'))

    for i in config.exceptions:
        html_data = ''.join(html_data).split(i)

    data = [i for i in html_data if i]
    for i in range(0, len(data), 5):
        cost_of_note = str_to_num(data[i + 4])
        notes = int(data[i + 2])
        config.dict_data[data[i + 1]] = cost_of_note / notes  # 'Название валюты' : 'Цена за одну банкноту в рублях'


def calculus(number, pair_money, d_money):
    number = str_to_num(number)
    return str(round(d_money[pair_money[0]] * number / float(d_money[pair_money[1]]), 2))


def generate_pair(pair, number_0, number_1, flag_pairs, ln_dict):
    s1 = ln_dict['currency_pair_txt'] + ': ' + ln_dict[flag_pairs[pair[0]][1]] + ' 💱 '\
         + ln_dict[flag_pairs[pair[1]][1]] + '\n'
    s2 = str(number_0) + flag_pairs[pair[0]][0] + ' = ' + str(number_1) + flag_pairs[pair[1]][0]
    return s1 + s2


def translate(message):
    if message == '🇷🇺':
        return languages.ru_dict
    elif message == '🇬🇧':
        return languages.en_dict
    elif message == '🇰🇿':
        return languages.kz_dict

import telebot
import languages as lang

from telebot import types
from config import pair, dict_data, flag_pairs, TOKEN, main_notes, notes, settings, to_convert_txt
from functions import str_to_num, transform_data, calculus, generate_pair, translate

transform_data()
bot = telebot.TeleBot(TOKEN)
ln_dict = lang.ru_dict


@bot.message_handler(commands=['start'])
def welcome(message):
    start_replica = ln_dict['welcome_txt'] + '{0.first_name}!\n' + ln_dict['im_txt'] + '<b>{1.first_name}</b>' \
                    + ln_dict['bot_replica_txt']
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    row_notes = [types.InlineKeyboardButton(i) for i in notes]
    row_settings = [types.InlineKeyboardButton(i) for i in settings]
    to_convert = types.KeyboardButton(to_convert_txt)

    markup.row(*row_notes)
    markup.row(*row_settings)
    markup.add(to_convert)
    bot.send_message(message.chat.id, start_replica.format(message.from_user, bot.get_me()), parse_mode='html',
                     reply_markup=markup)
    bot.send_message(message.chat.id, ln_dict['manual_script'])


@bot.message_handler(content_types=['text'])
def text(message):
    global ln_dict
    if message.chat.type == 'private':
        if message.text == 'ℹ':
            bot.send_message(message.chat.id, ln_dict['pair'] + flag_pairs[pair[0]][0] + flag_pairs[pair[1]][0])
        elif message.text == "⚙":
            bot.send_message(message.chat.id, ln_dict['manual_script'])
        elif message.text in notes:

            transform_data()
            exchange_rate = str(round(dict_data[main_notes[message.text][1]], 2))
            bot.send_message(message.chat.id, ln_dict[main_notes[message.text][0]] + exchange_rate + '!')

        elif message.text in settings:

            ln_dict = translate(message.text)

        elif str_to_num(message.text):

            transform_data()
            number_0 = message.text
            number_1 = calculus(message.text, pair, dict_data)
            bot.send_message(message.chat.id, generate_pair(pair, number_0, number_1, flag_pairs, ln_dict))

        elif message.text == to_convert_txt:

            inline_buttons = [types.InlineKeyboardButton(flag_pairs[i][0], callback_data=i) for i in flag_pairs]
            markup = types.InlineKeyboardMarkup(row_width=2)
            markup.row(*inline_buttons)
            bot.send_message(message.chat.id, ln_dict['choose_pair_txt'], reply_markup=markup)

        else:
            bot.send_message(message.chat.id, ln_dict['try_again_txt'])


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message and len(call.data) == 3:
            pair.pop(0)
            pair.append(call.data)
    except Exception as e:
        print(repr(e))


bot.polling(none_stop=True)
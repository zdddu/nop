import telebot , requests , random
bot = telebot.TeleBot('5018555972:AAFu9ybBN3i0zS5yyEDNW45qXHnf-CXzAx4')
@bot.message_handler(commands=['start'])
def cck(message):
    bot.send_message(message.chat.id, ' Ok, Wait >>>')
    while True:
        w = 'AaSsDdFfGgHJjKkLlPpOoziizuuzUuzyyTtRrEexxVBn'
        K = str("".join(random.choice(w)for i in range(1)))
        B = str("".join(random.choice(w)for i in range(1)))
        t = K+K+'_'+K+B+K+K
        y = requests.get(f'https://apis.red/api/telegram/?user={t}').json()
        h = y['data']
        if h == 'Taken User':
            bot.send_message(message.chat.id, f' ❌ غير متاح : @{t}')
        if h == 'Valid User':
            bot.send_message(message.chat.id, f' ✅ متاح : @{t}')
bot.polling(True)
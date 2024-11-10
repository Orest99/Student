import telebot
from telebot import types
from my_time import show_time
from my_time import main
from my_universal import universal
from read_token import get_token
tok = '7607049913:AAGZIfJPpNJrVd8BSEInb-1Q4PtWWHLvtqE'
bot = telebot.TeleBot(tok)
@bot.message_handler(commands = ['start'])
def start (message):
   sec =  universal(bot,message=message,text=['Вітаю,я допоможу обрати/зробити павер'],buttons=['До вибору :)'])
   bot.send_message(message.chat.id,text=sec)
@bot.message_handler(commands = ['exit'])
def exit_program(message):
    bot.send_message(message.chat.id, 'Гаразд')
    bot.stop_polling()
@bot.message_handler(content_types=['text'])

def next(message):
    if message.text == 'До вибору :)':
        universal(bot,message = message,text = ['Який павербанк бажаєте?'],buttons=['Ознайомча інформація'])
    if message.text == 'Ознайомча інформація':
        universal(bot,message=message, text=['Посилання на відео:', 'https://www.youtube.com/watch?v=iPkC28W1qfk','https://www.youtube.com/watch?v=iPkC28W1qfk'],buttons=['Купити', 'Зробити'])
    elif message.text == 'Купити':
        universal(bot,message=message, text=['Посилання на магазини: ', 'https://taksa.com.ua/', ' https://allo.ua/'],buttons=['Ціна'])
    elif message.text == 'Зробити':
        universal(bot,message=message, text=['Інформація збирання:', 'https://www.youtube.com/watch?v=ckn34_LugJE','https://www.youtube.com/watch?v=3Lr8am6iElg'],buttons=['Ціна', 'Деталі'])
    elif message.text == 'Деталі':
        universal(bot,message=message, text=['Деталі для павербанку'], buttons=['Основні_деталі','Корпус','Товари_до_павера','повернутися'])
    elif message.text == 'Ціна':
        universal(bot,message=message, text=['За яку ціну бажаєте?'], buttons=['Середня','Дорогий','Призначення','повернутися'])
    elif message.text == 'Середня':
        universal(bot,message=message, text=['Як варіант: https://allo.ua/ua/universalnye-mobilnye-batarei/romoss-30000mah-sense8-php30-401-02-belyj_2.html '], buttons=['повернутися'])
    elif message.text == 'Дорогий':
        universal(bot,message=message, text=['Як варіант: https://allo.ua/ua/universalnye-mobilnye-batarei/vneshnij-akb-romoss-60000mah-pea60-pea60-152-2142.html'], buttons=['повернутися'])
    elif message.text == 'Основні_деталі':
        universal(bot,message=message, text=['Деталі для павера'], buttons=['Плата зарядки','акумулятор','кабель_пайки','повернутися'])
    elif message.text == 'Повернутися_до_категорії':
        universal(bot,message=message, text=['Гаразд'], buttons=['Основні_деталі'])
    elif message.text == 'Корпус':
        universal(bot,message=message, text=['Тут підходить: https://www.aliexpress.com/w/wholesale-%D0%BA%D0%BE%D1%80%D0%BF%D1%83%D1%81-%D0%BF%D0%BE%D0%B2%D0%B5%D1%80%D0%B1%D0%B0%D0%BD%D0%BA%D0%B0-18650.html?spm=a2g0o.home.auto_suggest.1.650c76dbKoRezo'], buttons=['Готовий','альтернатива','повернутися'])
    elif message.text == 'Повернутися_до_категорії':
        universal(bot,message=message, text=['Гаразд'], buttons=['Корпус'])
    elif message.text == 'Готовий':
        universal(bot,message=message, text=['https://www.aliexpress.com'], buttons=['Повернутися_до_категорії'])
    elif message.text == 'альтернатива':
        universal(bot,message=message, text=['Можна купити харчовий лоточок для їжі в: https://avrora.ua/'], buttons=['Повернутися_до_категорії'])
    elif message.text == 'Плата зарядки':
        universal(bot,message=message, text=['https://www.aliexpress.com'], buttons=['Повільна','Швидка','Повернутися_до_категорії'])
    elif message.text == 'Повільна':
        universal(bot,message=message, text=['https://www.aliexpress.com/item/1005006178609600.html?spm=a2g0o.order_list.order_list_main.1049.6ccf1802sjjVBl#nav-review'], buttons=['Повернутися_до_категорії'])
    elif message.text == 'Швидка':
        universal(bot,message=message, text=['https://www.aliexpress.com/item/1005007378714516.html?spm=a2g0o.productlist.main.73.746fA3qmA3qmRu&algo_pvid=5adb9100-9b05-425d-b6df-680d680d96de&algo_exp_id=5adb9100-9b05-425d-b6df-680d680d96de-38&pdp_npi=4%40dis%21UAH%21297.19%21297.19%21%21%217.06%217.06%21%4021015c7617294316220011899e5619%2112000040492857408%21sea%21UA%214780673103%21X&curPageLogUid=4ziE01WAdPH1&utparam-url=scene%3Asearch%7Cquery_from%3A'], buttons=['Повернутися_до_категорії'])
    elif message.text == 'акумулятор':
        universal(bot,message=message, text=['https://akkb.com.ua/'], buttons=['Повернутися_до_категорії'])
    elif message.text == 'кабель_пайки':
        universal(bot,message=message, text=['Рекомендую від 22 і нижче ставити: https://www.aliexpress.com/item/1005006539408592.html?srcSns=sns_Telegram&spreadType=socialShare&bizType=ProductDetail&social_params=60833899642&aff_fcid=7a7fc6f4eb9c4cc7aae5637d3671aba9-1729431938995-04738-_EJVJynr&tt=MG&aff_fsk=_EJVJynr&aff_platform=default&sk=_EJVJynr&aff_trace_key=7a7fc6f4eb9c4cc7aae5637d3671aba9-1729431938995-04738-_EJVJynr&shareId=60833899642&businessType=ProductDetail&platform=AE&terminal_id=a73dbcd17275452997c4b19b9cd970f6&afSmartRedirect=y'], buttons=['Повернутися_до_категорії'])
    elif message.text == 'Товари_до_павера':
        universal(bot,message=message, text=['Обирайте'],buttons=['кабель зарядки','ліхтарик','стрічка(освітлення)','повернутися'])
    elif message.text == 'кабель зарядки':
        universal(bot,message=message, text=['Брав такий: https://www.aliexpress.com/item/1005006129902590.html?srcSns=sns_Telegram&spreadType=socialShare&bizType=ProductDetail&social_params=60828472883&aff_fcid=4292859f20bb4e539333448703398f34-1729431986302-06446-_EQ4UzGd&tt=MG&aff_fsk=_EQ4UzGd&aff_platform=default&sk=_EQ4UzGd&aff_trace_key=4292859f20bb4e539333448703398f34-1729431986302-06446-_EQ4UzGd&shareId=60828472883&businessType=ProductDetail&platform=AE&terminal_id=a73dbcd17275452997c4b19b9cd970f6&afSmartRedirect=y'], buttons=['Повернутися_до_категорії'])
    elif message.text == 'ліхтарик':
        universal(bot,message = message,text=['https://www.aliexpress.com/item/1005005991033841.html?spm=a2g0o.productlist.main.1.5e9a7807ebu9iY&algo_pvid=a664dfa5-fb89-4b2f-aff9-585b48bc070f&algo_exp_id=a664dfa5-fb89-4b2f-aff9-585b48bc070f-0&pdp_npi=4%40dis%21UAH%2175.77%2175.77%21%21%211.80%211.80%21%40211b618e17294324548054233eb8e2%2112000035206740195%21sea%21UA%214780673103%21X&curPageLogUid=3xj21nwiJ0mS&utparam-url=scene%3Asearch%7Cquery_from%3A'],buttons=['Повернутися_до_категорії'])
    elif message.text == 'стрічка(освітлення)':
        universal(bot,message=message, text=['https://www.aliexpress.com/item/1005007445971292.html?spm=a2g0o.order_list.order_list_main.53.3d721802oMfJZV'],buttons=['Повернутися_до_категорії'])
    elif message.text == 'Повернутися_до_категорії':
        universal(bot,message=message, text=['Гаразд'],buttons=['Товари_до_павера'])
    elif message.text == 'Призначення':
        universal(bot,message = message,text=['Чудово'],buttons=['Ноут','Телефон'])
    elif message.text == 'Ноут':
        universal(bot,message = message,text=['Варіант: https://allo.ua/ua/universalnye-mobilnye-batarei/vneshnij-akb-romoss-40000mah-pea40-pro-pd-65w-pea40-282-2183h-chernyj.html'],buttons=['Повернутися_до_категорій'])
    elif message.text == 'Телефон':
        universal(bot,message=message,text=['Варіант: https://allo.ua/ua/universalnye-mobilnye-batarei/romoss-30000mah-sense8-php30-401-02-belyj_2.html'],buttons=['Повернутися_до_категорій'])
    elif message.text == 'повернутися':
        universal(bot,message=message,text=['Гаразд'],buttons=['Купити','Зробити','Призначення'])
    elif message.text == 'Повернутися_до_категорій':
        universal(bot,message = message,text=['Гаразд'],buttons=['Ознайомча інформація','Купити','Зробити','Призначення','Деталі','Ціна','Основні_деталі','Товари_до_павера','Призначення'])
        return
if __name__ == "__main__":
    main()
    bot.polling(non_stop=True)

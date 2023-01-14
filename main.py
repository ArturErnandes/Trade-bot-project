import telebot
from telebot import types
import bs4 as b
from  bs4 import  BeautifulSoup
import requests
Token = open("venv/token.txt", 'r')
bot = telebot.TeleBot(Token.read())



@bot.message_handler(commands=['start'])
def start (message):
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    help = types.InlineKeyboardButton('help')
    markup1.add(help)
    bot.send_message(message.chat.id, 'Я бот, который поможет научиться основам трейдинга в простой форме', reply_markup=markup1)
    markup = types.InlineKeyboardMarkup(row_width=2)

    go = types.InlineKeyboardButton('Go', callback_data='go')
    markup.add(go)

    photo1 = 'https://i.pinimg.com/564x/f2/ea/dc/f2eadce93e391d7a67c1550ffbc73167.jpg'
    bot.send_photo(message.chat.id, photo1 , reply_markup=markup)





@bot.callback_query_handler(lambda c: c.data == 'go')
def go (call):
    bot.delete_message(call.message.chat.id, call.message.message_id)
    bot.delete_message(call.message.chat.id, call.message.message_id - 1)
    bot.delete_message(call.message.chat.id, call.message.message_id -2)
    markup = types.InlineKeyboardMarkup(row_width=2)
    trade = types.InlineKeyboardButton('Биржа', callback_data='trd')
    howstart = types.InlineKeyboardButton('Как начать', callback_data='hws')
    informa = types.InlineKeyboardButton(' Информация', callback_data='info')
    markup.add(trade, howstart,informa)
    photo1 = 'https://rusvest.ru/wp-content/uploads/2017/08/Crypto-exchange.jpg'
    bot.send_photo(call.message.chat.id,photo1, '', reply_markup= markup)

@bot.callback_query_handler(lambda c: c.data == 'trd')
def answer1 (call):
    bot.delete_message(call.message.chat.id, call.message.message_id)

    markup = types.InlineKeyboardMarkup(row_width=2)
    game = types.InlineKeyboardButton('Симулятор', callback_data='play')
    study = types.InlineKeyboardButton('Обучение', callback_data='ycheba')
    back = types.InlineKeyboardButton('Назад', callback_data='backtostart')
    markup.add(game, study, back)
    photo1 = 'https://miro.medium.com/max/3202/1*aGT1oTkxqPLVYWgXCSOSgw.png'

    bot.send_photo(call.message.chat.id, photo1, reply_markup= markup)

@bot.callback_query_handler(lambda c: c.data == 'backtostart')
def answer1 (call):
    bot.delete_message(call.message.chat.id, call.message.message_id)

    markup = types.InlineKeyboardMarkup(row_width=2)
    trade = types.InlineKeyboardButton('Биржа', callback_data='trd')
    howstart = types.InlineKeyboardButton('Как начать', callback_data='hws')
    info = types.InlineKeyboardButton('Информация', callback_data='info')
    markup.add(trade, howstart, info)
    photo1 = 'https://rusvest.ru/wp-content/uploads/2017/08/Crypto-exchange.jpg'
    bot.send_photo(call.message.chat.id, photo1, '', reply_markup=markup)


@bot.callback_query_handler(lambda c: c.data == 'hws')
def answer2 (call):
    bot.delete_message(call.message.chat.id, call.message.message_id)

    markup = types.InlineKeyboardMarkup(row_width=2)
    beg = types.InlineKeyboardButton(text='Посмотреть',url= 'https://www.tinkoff.ru/invest/education/courses/')
    backtotrade = types.InlineKeyboardButton('Назад', callback_data='backtt')
    markup.add(beg, backtotrade)
    photo1 ='https://img.freepik.com/premium-photo/printed-question-mark-covering-a-magnifying-glass_124595-67.jpg'

    bot.send_photo(call.message.chat.id,photo1, 'Ссылка на обучение',reply_markup=markup)


@bot.callback_query_handler(lambda c: c.data == 'backtt')
def answer1(call):
    bot.delete_message(call.message.chat.id, call.message.message_id)

    markup = types.InlineKeyboardMarkup(row_width=2)
    trade = types.InlineKeyboardButton('Биржа', callback_data='trd')
    howstart = types.InlineKeyboardButton('Как начать', callback_data='hws')
    informa = types.InlineKeyboardButton('Иформация', callback_data='info')
    markup.add(trade, howstart, informa)
    photo1 = 'https://rusvest.ru/wp-content/uploads/2017/08/Crypto-exchange.jpg'
    bot.send_photo(call.message.chat.id, photo1, '', reply_markup=markup)



@bot.callback_query_handler(lambda c: c.data == 'ycheba')
def answer1(call):
    bot.delete_message(call.message.chat.id, call.message.message_id)

    markup = types.InlineKeyboardMarkup(row_width=2)
    veb = types.InlineKeyboardButton('Статьи', callback_data='veb')
    howstart = types.InlineKeyboardButton('Видео', callback_data='mp4')
    backtotrd = types.InlineKeyboardButton('Назад', callback_data='bttrade')
    markup.add(veb, howstart,backtotrd)
    photo1 = 'https://i.pinimg.com/564x/9a/b3/7f/9ab37fdc8e5a22cffd0868ff75b21b08.jpg'
    bot.send_photo(call.message.chat.id, photo1, '', reply_markup=markup)



@bot.callback_query_handler(lambda c: c.data == 'mp4')
def answer1(call):
    bot.delete_message(call.message.chat.id, call.message.message_id)

    markup = types.InlineKeyboardMarkup(row_width=2)
    howstart = types.InlineKeyboardButton('Blockchain', callback_data='vid1')
    backtotrd = types.InlineKeyboardButton('Назад', callback_data='bttrade')
    markup.add( howstart,backtotrd)
    photo1 = 'https://i.pinimg.com/564x/9a/b3/7f/9ab37fdc8e5a22cffd0868ff75b21b08.jpg'
    bot.send_photo(call.message.chat.id, photo1, '', reply_markup=markup)

#@bot.callback_query_handler(lambda c: c.data == 'vid1')
def answer1(call):
    bot.delete_message(call.message.chat.id, call.message.message_id)

    markup = types.InlineKeyboardMarkup(row_width=2)
    backtotrd = types.InlineKeyboardButton('Назад', callback_data='mp4')
    markup.add(backtotrd)
    vide = 'https://www.youtube.com/watch?v=ksZ6YhrErOk&feature=youtu.be'
    bot.send_video(call.message.chat.id, vide,reply_markup=markup)




@bot.callback_query_handler(lambda c: c.data == 'veb')      ########################
def state (call):
        bot.delete_message(call.message.chat.id, call.message.message_id)
        markup = types.InlineKeyboardMarkup(row_width=1)
        st = types.InlineKeyboardButton('Краткая история биткойна', callback_data='abzac1')
        stt = types.InlineKeyboardButton('Blockchain', callback_data='blockchain')
        backtoychoba = types.InlineKeyboardButton('Назад', callback_data='ycheba')
        markup.add(st,stt,backtoychoba)
        photo1 = 'https://staging.ifamagazine.com/wp-content/uploads/2021/03/rsz_adobestock_408057388-scaled.jpg'
        bot.send_photo(call.message.chat.id, photo1, reply_markup=markup)



#@bot.callback_query_handler(lambda c: c.data == 'abzac1')
#def state1 (call):
        #bot.delete_message(call.message.chat.id, call.message.message_id)
        #markup = types.InlineKeyboardMarkup()
        #st = types.InlineKeyboardButton('Вперёд', callback_data='abzac2')
        #g = types.InlineKeyboardButton('Назад к статьям', callback_data='veb')
        #abzac1 = open('venv/states/1stfile.txt', 'r')
        #markup.add(st,g)
        #@bot.send_message(call.message.chat.id, abzac1.read(), reply_markup=markup)




@bot.callback_query_handler(lambda c: c.data == 'abzac1')
def state1 (call):
        bot.delete_message(call.message.chat.id, call.message.message_id)
        markup = types.InlineKeyboardMarkup()
        st = types.InlineKeyboardButton('Вперёд', callback_data='abzac2')
        g = types.InlineKeyboardButton('Назад к статьям', callback_data='veb')
        markup.add(st,g)
        bot.send_message(call.message.chat.id, 'История главной мировой криптовалюты началась 31 октября 2008 года, когда никому не известный человек под псевдонимом Сатоши Накамото опубликовал статью «Биткойн: P2P электронные деньги». В этой статье он описал будущий протокол биткоина – свод правил, по которым должна была работать создаваемая система.',reply_markup=markup)



@bot.callback_query_handler(lambda c: c.data == 'abzac2')
def state2 (call):
        markup = types.InlineKeyboardMarkup()
        st = types.InlineKeyboardButton('Вперёд', callback_data='abzac3')
        markup.add(st)
        bot.send_message(call.message.chat.id, 'Все части системы были известны и до Накамото. Криптографические алгоритмы, заложенные в основу биткоина, уже существовали. Распределенное хранение данных в децентрализованных сетях также использовалось.',reply_markup=markup)

@bot.callback_query_handler(lambda c: c.data == 'abzac3')
def state3 (call):
        markup = types.InlineKeyboardMarkup()
        st = types.InlineKeyboardButton('Вперёд', callback_data='abzac4')
        markup.add(st)
        bot.send_message(call.message.chat.id, 'Гениальность Накамото была в том, что именно он собрал отдельные куски в целое, выстроил систему и заставил ее работать. Предлагаемая система была действительно революционной, ничего подобного ранее не существовало.',reply_markup=markup)



@bot.callback_query_handler(lambda c: c.data == 'abzac4')
def state4 (call):
        markup = types.InlineKeyboardMarkup()
        st = types.InlineKeyboardButton('Вперёд', callback_data='abzac5')
        markup.add(st)
        bot.send_message(call.message.chat.id, 'Вскоре после публикации протокола, 3 января 2009 года, Сатоши был сгенерирован первый блок в цепочке блокчейна. В этот момент были намайнены первые 50 биткоинов.',reply_markup=markup)



@bot.callback_query_handler(lambda c: c.data == 'abzac5')
def state5 (call):
        markup = types.InlineKeyboardMarkup()
        stt = types.InlineKeyboardButton('Круто! А теперь к инвестициям', callback_data='ven')
        st = types.InlineKeyboardButton('А что было дальше?', callback_data='abzac6')
        markup.add(st, stt)
        bot.send_message(call.message.chat.id, '''
Последнее сообщение от «Сатоши» — кто бы ни скрывался за этим псевдонимом – было получено 12 декабря 2010 года. После этого он исчез из Cети и больше не участвовал ни в дальнейшем развитии биткоина, ни вообще в какой-либо деятельности…
Такова история появления биткоина.''',reply_markup=markup)


@bot.callback_query_handler(lambda c: c.data == 'ven')
def state (call):
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.delete_message(call.message.chat.id, call.message.message_id - 1)
        bot.delete_message(call.message.chat.id, call.message.message_id - 2)
        bot.delete_message(call.message.chat.id, call.message.message_id - 3)
        bot.delete_message(call.message.chat.id, call.message.message_id - 4)
        markup = types.InlineKeyboardMarkup(row_width=2)
        st = types.InlineKeyboardButton('Краткая история биткойна', callback_data='abzac1')
        stt = types.InlineKeyboardButton('Blockchain', callback_data='blockchain')
        backtoychoba = types.InlineKeyboardButton('Назад', callback_data='ycheba')
        markup.add(st,stt,backtoychoba)
        photo1 = 'https://staging.ifamagazine.com/wp-content/uploads/2021/03/rsz_adobestock_408057388-scaled.jpg'
        bot.send_photo(call.message.chat.id, photo1, reply_markup=markup)



@bot.callback_query_handler(lambda c: c.data == 'abzac6')
def state6 (call):
        markup = types.InlineKeyboardMarkup()
        st = types.InlineKeyboardButton('вперёд', callback_data='abzac7')
        markup.add(st)
        bot.send_message(call.message.chat.id,'Сразу после появления биткоина началось его активное развитие.Уже через 9 месяцев, 5 октября 2009 года, был впервые установлен обменный курс биткоина. На ресурсе New Liberty Standart можно было обменять 1 доллар на 1 309,03 биткоинов. То есть, за 1 цент можно было купить 13 биткоинов! Вы можете сопоставить эту цифру с сегодняшним курсом и понять, каков был рост у биткоина за все время.',reply_markup=markup)

@bot.callback_query_handler(lambda c: c.data == 'abzac7')
def state8 (call):
        markup = types.InlineKeyboardMarkup()
        stt = types.InlineKeyboardButton('Круто! А теперь к инвестициям', callback_data='vek')
        markup.add(stt)
        bot.send_message(call.message.chat.id,'22 мая 2010 года состоялся настоящий прорыв! Впервые биткоины были обменены на реальный товар.Американец Ласло Ханеч за 10 000 биткоинов получил две пиццы. Это было по-настоящему революционным событием. Биткоин перестал быть сугубо виртуальным феноменом и проник в реальный мир.',reply_markup=markup)

@bot.callback_query_handler(lambda c: c.data == 'vek')
def state (call):
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.delete_message(call.message.chat.id, call.message.message_id - 1)
        bot.delete_message(call.message.chat.id, call.message.message_id - 2)
        bot.delete_message(call.message.chat.id, call.message.message_id - 3)
        bot.delete_message(call.message.chat.id, call.message.message_id - 4)
        bot.delete_message(call.message.chat.id, call.message.message_id - 5)
        bot.delete_message(call.message.chat.id, call.message.message_id - 6)

        markup = types.InlineKeyboardMarkup(row_width=2)
        st = types.InlineKeyboardButton('Краткая история биткойна', callback_data='abzac1')
        stt = types.InlineKeyboardButton('Blockchain', callback_data='blockchain')
        backtoychoba = types.InlineKeyboardButton('Назад', callback_data='ycheba')
        markup.add(st,stt,backtoychoba)
        photo1 = 'https://staging.ifamagazine.com/wp-content/uploads/2021/03/rsz_adobestock_408057388-scaled.jpg'
        bot.send_photo(call.message.chat.id, photo1, reply_markup=markup)




















@bot.callback_query_handler(lambda c: c.data == 'bttrade')
def answer1 (call):
    bot.delete_message(call.message.chat.id, call.message.message_id)

    markup = types.InlineKeyboardMarkup(row_width=2)
    game = types.InlineKeyboardButton('Симулятор', callback_data='play')
    study = types.InlineKeyboardButton('Обучение', callback_data='ycheba')
    back = types.InlineKeyboardButton('Назад', callback_data='backtostart')
    markup.add(game, study, back)
    photo1 = 'https://miro.medium.com/max/3202/1*aGT1oTkxqPLVYWgXCSOSgw.png'

    bot.send_photo(call.message.chat.id, photo1, reply_markup= markup)




@bot.callback_query_handler(lambda c: c.data == 'info')
def answer1(call):
    bot.delete_message(call.message.chat.id, call.message.message_id)

    markup = types.InlineKeyboardMarkup(row_width=2)
    mast = types.InlineKeyboardButton('Владельцы', callback_data='mybot')
    passport = types.InlineKeyboardButton('Прочитать', callback_data='online')
    backtosta = types.InlineKeyboardButton('Назад', callback_data='btt')
    markup.add(mast, passport, backtosta)
    photo1 = 'https://resh.edu.ru/uploads/lesson_extract/7316/20200113122314/OEBPS/objects/m_info_7_2_1/5df618b1e2002477581035db.jpg'
    bot.send_photo(call.message.chat.id, photo1, '', reply_markup=markup)


@bot.callback_query_handler(lambda c: c.data == 'btt')
def go(call):
    bot.delete_message(call.message.chat.id, call.message.message_id)

    markup = types.InlineKeyboardMarkup(row_width=2)
    trade = types.InlineKeyboardButton('Биржа', callback_data='trd')
    howstart = types.InlineKeyboardButton('Как начать', callback_data='hws')
    informa = types.InlineKeyboardButton('информация', callback_data='info')
    markup.add(trade, howstart,informa)
    photo1 = 'https://rusvest.ru/wp-content/uploads/2017/08/Crypto-exchange.jpg'
    bot.send_photo(call.message.chat.id,photo1, '', reply_markup=markup)












@bot.callback_query_handler(lambda c: c.data == 'mybot')
def answer1(call):
    bot.delete_message(call.message.chat.id, call.message.message_id)

    markup = types.InlineKeyboardMarkup(row_width=2)
    backtosta = types.InlineKeyboardButton('Назад', callback_data='btt')
    markup.add(backtosta)
    photo1 = 'https://resh.edu.ru/uploads/lesson_extract/7316/20200113122314/OEBPS/objects/m_info_7_2_1/5df618b1e2002477581035db.jpg'
    bot.send_photo(call.message.chat.id, photo1, '''
Владельцы:
======================
https://t.me/ss_We_can
======================
https://t.me/lagovdp
======================
https://t.me/arthurphotographer
======================
https://t.me/Mr_SaZaN
======================''', reply_markup=markup)

















@bot.callback_query_handler(lambda c: c.data == 'play')
def answer1(call):
    bot.delete_message(call.message.chat.id, call.message.message_id)

    markup = types.InlineKeyboardMarkup(row_width=2)
    mast = types.InlineKeyboardButton('Играть', callback_data='play2')
    passport = types.InlineKeyboardButton('Об игре', callback_data='infof')
    backtosta = types.InlineKeyboardButton('Назад', callback_data='trd')
    markup.add(mast, passport, backtosta)
    photo1 = 'https://i.pinimg.com/564x/f8/e9/bc/f8e9bc430a5926eed3e166f8f2c6697c.jpg'
    bot.send_photo(call.message.chat.id, photo1, '', reply_markup=markup)

#@bot.callback_query_handler(lambda c: c.data == 'play2')
def answer1(call):
    bot.delete_message(call.message.chat.id, call.message.message_id)
    URL = 'https://bcs-express.ru/kotirovki-i-grafiki/BTCUSD'
    r = requests.get(URL)
    soup = BeautifulSoup(r.text, 'html.parser')
    btc = soup.find_all('div', class_="KPOM")

    bot.send_message(call.message.chat.id, '-', btc)


bot.polling(none_stop=True)
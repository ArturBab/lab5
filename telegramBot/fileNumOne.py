import telebot
from telebot import types # Модуль для работы кнопопк

name = ''
surname = ''
age = 0

#5018699864:AAHd7D2ZsP-xNYKN-S5indathHw9gnwk_eg - token

bot = telebot.TeleBot("5018699864:AAHd7D2ZsP-xNYKN-S5indathHw9gnwk_eg")

##################################
@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Чем могу вам помочь?")

@bot.message_handler(commands=['myinfo'])
def send_myinfo(message):
    bot.reply_to(message, "Данные:\n\n"
                          "Исполнитель: Бабаян А.А.\n"
                          "Группа: ИУ5Ц-52Б\n"
                          "Дата рождения: 12.01.2001 г.\n"
                          "Факультет: ГУИМЦ, Информатика и вычислительная техника, ИУ\n"
                          "Курс: 3")

################## Команды (через слэш "/")

#################
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if message.text == 'Привет':
	    bot.reply_to(message, 'Привет создатель бота!')
    elif message.text == 'hi':
        bot.reply_to(message, 'Hello bot creator! How can I help you?')

################## Обработка сообщений




        #Регистрация
    elif message.text == '/reg':
        bot.send_message(message.from_user.id, "Здравствуйте! Введите свои данные:") #Передали айди нашего чата
        
        #Функция, сохраняющая имя пользователя переменным
        
        bot.register_next_step_handler(message, regName)
    
    elif message.text == 'test call':
        bot.reply_to(message, 'test echoCall is done')
    #bot.reply_to(message, message.text)




def regName(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, "Какая у Вас фамилия?")
    bot.register_next_step_handler(message, regSurname)

def regSurname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, "Сколько Вам лет?")
    bot.register_next_step_handler(message, regAge)

def regAge(message):
    global age
    #age = message.text
    while age == 0: # Цикл, который проверяет правильность ввода
        try:
            age = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, "Вводите цифрами!!")

    ###Вывод кнопок на экран###
    keyboard = types.InlineKeyboardMarkup()

    keyYes = types.InlineKeyboardButton(text = 'да', callback_data = 'yes')
    keyboard.add(keyYes)

    keyNo = types.InlineKeyboardButton(text = 'нет', callback_data = 'no')
    keyboard.add(keyNo)

    question = "Вам " + str(age)+' лет? и Вас зовут: '+name+' '+surname+' ? '
    bot.send_message(message.from_user.id, question, reply_markup=keyboard)

@bot.callback_query_handler(func = lambda call: True)
def callback_worker(call):
    if call.data == "yes": #Получили ответ
        bot.send_message(call.message.chat.id, "Вы зарегистрированы")

    elif call.data == "no": #Получили ответ
        bot.send_message(call.message.chat.id, "Введите свои данные еще раз!")
        bot.send_message(call.message.chat.id, "Введите данные еще раз:")  # Передали айди нашего чата
        bot.register_next_step_handler(call.message, regName)


bot.polling()
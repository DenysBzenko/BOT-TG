import telebot

# Створення бота та налаштування API ключа
bot = telebot.TeleBot("6165897201:AAFtL_Sq4zKIyZTSiuHCLzD2vjYwZYtixWw")

# Вхідна річ
start_message = ("Вітаю вас, новий користувачу! Я - бот, який допомагає отримувати рефералів для різних сайтів, таких як crew3 або gleam. Якщо ви шукаєте спосіб збільшити кількість рефералів на цих сайтах, то ви знайшли правильного помічника.Якщо у вас є якісь запитання або потрібна допомога, натисність на Support  в меню . Ми завжди раді допомогти вам зі збільшенням кількості рефералів на ваших улюблених сайтах.")
# Кнопки для вибору
menu_buttons = telebot.types.InlineKeyboardMarkup()
menu_buttons.row(
    telebot.types.InlineKeyboardButton("Telegram channel ", callback_data='option1'),
    telebot.types.InlineKeyboardButton("Support", callback_data='option4'),
    telebot.types.InlineKeyboardButton("Balance", callback_data='option3')
)


# Кнопки для опції 1
option1_buttons = telebot.types.InlineKeyboardMarkup()
option1_buttons.row(
    telebot.types.InlineKeyboardButton("First" , url="https://t.me/lachentyt", callback_data='option1-1'),
    telebot.types.InlineKeyboardButton("Second", url="https://t.me/irpingrisha", callback_data='option1-2')
)
option1_buttons.row(
    telebot.types.InlineKeyboardButton("Back", callback_data='back')
)
option3_buttons = telebot.types.InlineKeyboardMarkup()
option3_buttons.row(
    telebot.types.InlineKeyboardButton("Використати бали." ,callback_data='option2-1'),
    telebot.types.InlineKeyboardButton("Отримати бали.", callback_data='option2-2'),
)



option2_buttons = telebot.types.InlineKeyboardMarkup()
option2_buttons.row(
    telebot.types.InlineKeyboardButton("Back", callback_data='back2')
)
back_button = telebot.types.InlineKeyboardMarkup()
back_button.row(
    telebot.types.InlineKeyboardButton("Back", callback_data='back')
)




# Обробник повідомлень
@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == 'option1':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Select option :", reply_markup=option1_buttons)
    elif call.data == 'option1-1':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ви обрали Опцію 1-1!")
    elif call.data == 'option1-2':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ви обрали Опцію 1-2!")
    elif call.data == 'option2':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="тут петро повинен написати текст!")
    elif call.data == 'option3':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="You can choose ", reply_markup=back_button)
    elif call.data == 'back':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=start_message, reply_markup=menu_buttons)
    elif call.data == 'option2-1':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Your balance")
    elif call.data == 'option2-2':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ви обрали Опцію 1-2!")
    elif call.data == 'option4':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Support - Щоб почати користуватися ботом вам потрібні бали, отримати бали ви можете після підписки на канали спонсорів або після виповнення рефералки іншого користувача. Щоб використати бали перейдіть у розділ Balance. Зв'язок з тех. підтримкою ", reply_markup=option2_buttons)
    elif call.data == 'option3':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ви обрали Опцію 4!", reply_markup=option2_buttons)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, start_message, reply_markup=menu_buttons)

# Запуск бота
bot.polling()

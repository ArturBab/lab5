# Лабораторная работа 5 – Создание Telegram-бота  

**Описание**  
Данный репозиторий содержит лабораторную работу по созданию **Telegram-бота** на Python с использованием библиотеки `pyTelegramBotAPI`.  

## Функционал бота  
**Обработка команд:**  
   - `/start` – приветственное сообщение.  
   - `/help` – вывод справки.  
   - `/myinfo` – отображение информации о пользователе.  
   - `/reg` – процесс регистрации (имя, фамилия, возраст).  
**Обработка текстовых сообщений** (например, "Привет" → "Привет, создатель бота!").  
**Инлайн-кнопки** ("Да" / "Нет") для подтверждения данных.  
**Проверка корректности ввода** (например, проверка возраста на число).  

---

## Структура репозитория  
lab5_telegram_bot/ ├── bot.py # Основной код бота ├── config.py # Конфигурационный файл (токен бота) └── README.md # Описание проекта


---
Бот использует telebot для обработки сообщений и InlineKeyboardMarkup для кнопок.
Пример кода:
   ```bash
import telebot
from telebot import types

TOKEN = "YOUR_BOT_TOKEN"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()

   ```
---

## Запуск Telegram-бота  
### Установка зависимостей 
Перед запуском убедитесь, что у вас установлен пакет `pyTelegramBotAPI`:  
```bash
pip install pyTelegramBotAPI

1. **Склонировать репозиторий:**  
   ```bash
   git clone https://github.com/ArturBab/lab5_telegram_bot.git
   cd lab5_telegram_bot

2. **Запустить основной скрипт:**
   ```bash
   python bot.py
```

**Связанные материалы:** 
- [Документация pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)

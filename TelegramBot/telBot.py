import telebot #liberia per fare il bot
import webbrowser
import keyboard
import time
import mouse

chrome = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"

API_TOKEN = "5342868948:AAGEprbqi5fmt80Su8NKDKgVziV5J69dNuk" #token del bot

bot = telebot.TeleBot(API_TOKEN) 

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message,"Dammi il link che vuoi eseguire")

#1006, 794

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)
    link = message.text
    webbrowser.get(chrome).open_new(link)
    time.sleep(2)
    keyboard.press_and_release('alt+tab')
    time.sleep(0.1)
    keyboard.press_and_release('ctrl+w')
    time.sleep(0.1)
    keyboard.press_and_release('alt+tab')
    time.sleep(0.1)
    mouse.move(1006,794, absolute = True, duration=0.1)
    time.sleep(0.1)
    mouse.click('left')



bot.polling() # per ricevere il messaggio.
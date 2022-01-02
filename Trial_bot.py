import os
import telebot
from dotenv import load_dotenv
import yfinance as yf
import random

load_dotenv()

API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['Greet'])
def greet(message):
    bot.reply_to(message, "Whats up buddy??")


@bot.message_handler(commands=['hello'])
def hello(message):
    bot.send_message(message.chat.id, "Chatting..")


@bot.message_handler(commands=['Finance'])
def finance(message):
    response = ""
    stocks = ['gme', 'amc']
    stock_data = []
    for stock in stocks:
        data = yf.download(tickers=stock, period='2d')
        data = data.reset_index()
        response += f"{stock}:  "
        stock_data.append([stock])
        columns = ['stock']
        for index, row in data.iterrows():
            stock_pos = len(stock_data) - 1
            price = row['Close']
            format_date = row['Date'].strftime('%y/%m/%d')
            response += f"{format_date}--> $ {price}\n"
            stock_data[stock_pos].append(price)
            columns.append(format_date)
            bot.send_message(message.chat.id, response)


def st_req(message):
    if len(message.text) == 1:
        return True
    return False


@bot.message_handler(func=st_req)
def finance(message):
    bot.reply_to(message, "VOLA, you were right")


bot.polling()

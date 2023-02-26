import telebot
from bs4 import BeautifulSoup
import requests

a = []
req = requests.get('https://www.olx.kz/elektronika/noutbuki-i-aksesuary/noutbuki/')
soup = BeautifulSoup(req.text, 'html.parser')
titles = soup.find_all(attrs={'class':'marginright5 link linkWithHash detailsLink linkWithHashPromoted'})
for i in range(len(titles)):
    a.append(titles[i].find('strong').string)

token='5117472172:AAEJNiYhjgz83bxRUG9CdGLNINpt_korCBI'
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
    for i in range(len(a)):  
      bot.send_message(message.chat.id, a[i])
bot.polling()

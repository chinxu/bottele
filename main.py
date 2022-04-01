from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests
from bs4 import BeautifulSoup
 
def kimdong(update: Update, context: CallbackContext) -> None:
    kim_lich = requests.get("https://nxbkimdong.com.vn/blogs/lich-phat-hanh-sach-dinh-ky")
    soup_kimlich = BeautifulSoup(kim_lich.text,"html.parser")
    mydiv_kim = soup_kimlich.findAll('div',{'class':'article-title'})
    div_final = []
    for div in mydiv_kim:
        div1 = div.a.get('href')
        div2 = "https://nxbkimdong.com.vn" + div1
        div_final.append(div2)
    update.message.reply_text(f'Lịch phát hành nhà xuất bản Kim Đồng\n {div_final[0]} ')

    
def zing(update: Update, context: CallbackContext) -> None:
    zing = requests.get("https://zingnews.vn/")
    soup_zing = BeautifulSoup(zing.text,"html.parser")
    div_zing = soup_zing.findAll('p', {'class':'article-title'})
    zing_link = []
    for div_z in div_zing:
        div1z = div_z.a.get("href")
        div2z = "https://zingnews.vn" + div1z
        zing_link.append(div2z)
    for zing_3 in zing_link[0:5]:
        update.message.reply_text(f'Tin mới Zing\n {zing_3} ')

def coin(update: Update, context: CallbackContext) -> None:
    name_coin = ["pegaxy", "vigorus"]
    for abc in name_coin:
        coin = requests.get("https://coinmarketcap.com/currencies/" + str(abc) + "/")
        soup_coin = BeautifulSoup(coin.text, "html.parser")
        div_soup = soup_coin.findAll("div",{"class":"priceValue"})
        div_soup2 = soup_coin.findAll("small",{"class":"nameSymbol"})
        div_soup_str = str(div_soup)
        div_soup_str2 = str(div_soup2)
        coin_title = div_soup_str2[27:30]
        coin_price = div_soup_str[31:38]
        coin_info = coin_title + "\n" + coin_price
        update.message.reply_text(f'Giá coin\n {coin_info} ')
updater = Updater('5276260976:AAEajvvhXvrfAyeeAzFg_hz7cD6llZjwnwE')


updater.dispatcher.add_handler(CommandHandler('kimdong', kimdong))
updater.dispatcher.add_handler(CommandHandler('zing', zing))
updater.dispatcher.add_handler(CommandHandler('coin', coin))
updater.start_polling()
updater.idle()

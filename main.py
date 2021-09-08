import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from tracker import get_prices

telegram_bot_token = "1372871302:AAHTNbEfrEVLZtLE5m_zOCld9X6Gp_KfIPs"

updater = Updater(token=telegram_bot_token, use_context=True)

dispatcher = updater.dispatcher

def help(update, context):
  
  chat_id = update.effective_chat.id
  
  message = "Hey! \n You can See Prices of Bitcoin, Ethereum ,Dogecoin"
  
  context.bot.send_message(chat_id =chat_id, text=message)

def bestCoin(update, context):
  
  chat_id = update.effective_chat.id
  
  message =" In 2021, \n Best coice between the variety of crypto coins is by DOGE - Dogecoin by Far most likely to be a good investment until Elon musk gets bored on hope on some new rocket TO THE MOON "
  
  context.bot.send_message(chat_id = chat_id, text= message)

def dogeCoin(update, context):
  
  chat_id = updater.effective_chat.id
  
  message ="Dogecoin was Created by IBM software engineer Billy Markus from Portlad. Oregon and Adobe software engineer Jackson palmer , Who set out to create a peer-to-peer digital currency that could reach a broader demographic than Bitcoin. In addition They wanted To distance it from the convenrsial history of other coins. \n Dogecoin was officially launched on Dec 6 ,2013 and within first 30 days there were over a million visitiors to Dogecoin.com"
  
  context.bot.send_message(chat_id =chat_id, text= message)

def coins(update, context):
    
    chat_id = update.effective_chat.id
    
    message = ""

    crypto_data = get_prices()
    for i in crypto_data:
        coin = crypto_data[i]["coin"]
        price = crypto_data[i]["price"]
        change_day = crypto_data[i]["change_day"]
        change_hour = crypto_data[i]["change_hour"]
        message += f"Coin: {coin}\nPrice: ${price:,.2f}\nHour Change: {change_hour:.3f}%\nDay Change: {change_day:.3f}%\n\n"

    context.bot.send_message(chat_id=chat_id, text=message)

def disclaimer(update,context):
  
  chat_id = update.effective_chat.id
 
  message = " I Am not Invester. \n Im Not even a millionaire \n Just tried some thing new so that wanna share this through the Bot."    
  
  context.bot.send_message(chat_id = chat_id, text=message)


dispatcher.add_handler(CommandHandler("help", help))
dispatcher.add_handler(CommandHandler("bestCoin", bestCoin))
dispatcher.add_handler(CommandHandler("dogeCoin", dogeCoin))
dispatcher.add_handler(CommandHandler("coins", coins))
dispatcher.add_handler(CommandHandler("disclaimer",disclaimer))
updater.start_polling()
updater.idle()

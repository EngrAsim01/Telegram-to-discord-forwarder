import requests
import telebot
import keep_alive

bot = telebot.TeleBot("Telegram bot api key")

# Discord Webhook URL
# How to get webhook form discord.. See in the readme file...
webhook_url = "Discord bot webhook url"

# this is optional 
group_id = " Group or channel id where you want to use the bot."

@bot.message_handler(content_types=['text'])
def send_to_discord(message):
  # if message.author == client.user:
  #   return
    if message.chat.id == group_id:
        
      try:
          # Sends message from Telegram to Discord
          if "Msg has keywords" in message.text:
              requests.post(webhook_url, json={'content': f'{message.text}\n{message.id}'})
              # requests.post(webhook_url, json={'content': f"messageid {message.id}" })

              # bot will reply that your msg is processed 
              bot.reply_to(message, text="Your Msg is processed.")
          else:
                # To get ihe group id eaisly 
              print(f"groud id is {message.chat.id}")

              # Can also delete the spam msgs if the keyword not in msg will delete the msg with 
              # the reply msg 
              bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
              bot.send_message(chat_id=message.chat.id, text="Please send keyword only.")
      except:
          print('invalid message')
  
# To know the purpose of this line of code go to the readme file.
keep_alive.keep_alive()

bot.infinity_polling()
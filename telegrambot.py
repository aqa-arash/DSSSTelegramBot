import telepot
from telepot.loop import MessageLoop
import time
from mistralai import Mistral


api_key = "Key here"
model = "mistral-small-2402"
client = Mistral(api_key=api_key)


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id, msg)
    chat_response = client.chat.complete(
        model= model,
        messages = [
            {
                "role": "user",
                "content": msg['text'],
            },
        ]
    )
    bot.sendMessage(chat_id, chat_response.choices[0].message.content)

bot = telepot.Bot('Bot key here ')
MessageLoop(bot, handle).run_as_thread()

while True:
    time.sleep(10)




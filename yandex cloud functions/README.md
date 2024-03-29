# tgb_googletranslate
Bot code adaptation to run it at Yandex Cloud Functions

I used [this article](https://habr.com/ru/articles/550456/) as a referrence.

Steps to launch it:

1. You need to have a payment account at Ycloud ([details...](https://cloud.yandex.ru/ru/docs/functions/tutorials/telegram-bot-serverless#before-begin))
2. Create a cloud function, upload the files (`main.py`, `index.py`, `requirements.txt`), insert bot's `TOKEN` into `Environment variables` field. After creating, copy the field `ID` from the `Overview` section.
3. Create API Gateway with the following text (you need to replace `YOUR_FUNCTION_ID` with your real `ID`):
```yaml
openapi: 3.0.0
info:
 title: for-python-tg-bot
 version: 1.0.0
paths:
 /:
   post:
     x-yc-apigateway-integration:
       type: cloud-functions
       function_id: YOUR_FUNCTION_ID
     operationId: tg-webhook-function
```
4. In the `Overview` section of your recently created API Gateway copy the field `Default domain`. You need to set this webhook address to your bot with these commands:
```python 
# pip install pyTelegramBotAPI
import telebot

bot = telebot.TeleBot("YOUR_TOKEN")

bot.remove_webhook()
bot.set_webhook("Default domain URL")
```
5. Finally, turn on the `Public function` switch in the `Overview` section of your cloud function. From now it works!

### Useful links
- https://cloud.yandex.ru/ru/docs/functions/quickstart/create-function/python-function-quickstart
- https://cloud.yandex.ru/ru/docs/functions/tutorials/telegram-bot-serverless
- https://cloud.yandex.ru/ru/docs/billing/concepts/serverless-free-tier
- https://pytba.readthedocs.io/_/downloads/en/4.6.0/pdf/

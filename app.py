#web app
#SDK : https://github.com/line/line-bot-sdk-python


from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('90qjqw/96af1K0Dvg1uonvKtxr1AWclNXtQ859EnDyzMndasSWFQI7dElvpXtPXGRq6EPH4GyMxjjmN5qBVXWZXZJiv0Kp9sqigPkc8vTLUvWdmC1v/wqxUiYnFBh8skjLUlqcfg1KEFFls3k5ht9QdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('375de5b1e6fe72bd8fb3b58cb304ec4c')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
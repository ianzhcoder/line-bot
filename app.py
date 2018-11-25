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
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage
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

#rule-based
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r_msg = "對不起請輸入現在的心情..."


    if "給個表情吧" in msg:
        sticker_message = StickerSendMessage(
        #https://devdocs.line.me/files/sticker_list.pdf
        # package_id=1,
        # sticker_id=1
        package_id=random.randint(1,2),
        sticker_id=random.randint(1,527)
        )

        line_bot_api.reply_message(
            event.reply_token,
            sticker_message)

        return

    if msg in ['hi','Hi','HI']:
        r_msg = "HI~很高興見到你..."
    elif msg == "我好開心":
        r_msg = "記住開心的感覺喔..."
    elif msg == "我好生氣":
        r_msg = "So What?"
    elif msg == "我好難過":
        r_msg = "你現在感覺如何？"
    elif msg == "我好孤單":
        r_msg = "我一直都在..."


    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r_msg))


if __name__ == "__main__":
    app.run()
from flask import Flask, render_template
import smtplib
from flask_mail import Mail, Message

import flask

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    # EMAIL SETTINGS
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME='automateuipath@gmail.com',
    MAIL_PASSWORD='Uipath@8732'
)
mail = Mail(app)


@app.route('/send-mail/')
def send_mail():
    try:
        msg = Message("Send Mail Tutorial!",
                      sender="automateuipath@gmail.com",
                      recipients=["debmitra9674@gmail.com"])
        # msg.body = "Yo!\nHave you heard the good word of Python???"
        # msg.html = render_template('text.html')
        msg.html = render_template('SurveyForm.html')
        mail.send(msg)
        return 'Mail sent!'
    except Exception as e:
        return e


if __name__ == '__main__':
    app.run(host='0.0.0.0')

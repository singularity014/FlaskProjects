from flask import Flask, render_template, request
import smtplib
from flask_mail import Mail, Message
import sqlalchemy
from push_to_db import *

import flask

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    # EMAIL SETTINGS
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME='<youremail@example.com>',
    MAIL_PASSWORD='<your_password>'
)
mail = Mail(app)
poll_data = {
    'question1': 'Which web framework do you use?',
    'fields1': ['Flask', 'Django', 'TurboGears', 'web2py', 'pylonsproject'],
    'question2': 'Which languages do you prefer?',
    'fields2': ['JAVA', 'C++', 'Python', '.Net', 'PHP']
}
filename = 'data.txt'


def populate_table(username, vote1, vote2):
    # will insert into the table
    # username and vote
    value = {}
    value['username'] = username
    value['vote1'] = vote1
    value['vote2'] = vote2
    action = 'insert'
    db_res = create_insert_table(action, value)
    return db_res


@app.route('/', methods=['GET'])
def root():
    try:
        msg = Message("Send Mail Tutorial!",
                      sender="youremail@example.com",
                      recipients=["recepients1@example.com", "recepients2@example.com"])
        # msg.body = "Yo!\nHave you heard the good word of Python???"
        # msg.html = render_template('text.html')

        msg.html = render_template('SurveyForm.html', data=poll_data)
        mail.send(msg)
        return 'Mail sent!'
    except Exception as e:
        return e


# @app.route('/')
# def root():
#     return render_template('SurveyForm.html', data=poll_data)


@app.route('/survey', methods=['GET'])
def survey():
    all_data = dict(request.args.lists())#ImmutableMultiDict
    print(f'all_data - {all_data}')
    print()
    l_username = ''.join(all_data.get('username'))
    l_vote1 = ','.join(all_data.get('field1')) # Question 1 - answers
    l_vote2 = ','.join(all_data.get('field2')) # Questions 2 - answers
    print(l_vote1)
    print(l_vote2)

    call_table = populate_table(l_username, l_vote1, l_vote2)
    print(f'call table response - {call_table}')
    # result_string = f'user is - {username}, voted for {vote}'
    # out = open(filename, 'a')
    # out.write(result_string + '\n')
    # out.close()

    return render_template('thankyou.html', data=poll_data)


if __name__ == "__main__":
    app.run(debug=True)

import request
from flask import Flask, render_template, request
from flask_mail import Mail, Message
from push_to_db_relationship import *
from fetch_from_db import *
from dbmodel_conf import  app

# app.config.fom_object("config.DevelopmentConfig")
# print(app.config["EMAIL_PASSWORD"])
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
poll_data = {
    'question1': 'Which web framework do you use?',
    'fields1': ['Flask', 'Django', 'TurboGears', 'web2py', 'pylonsproject'],
    'question2': 'Which languages do you prefer?',
    'fields2': ['JAVA', 'C++', 'Python', '.Net', 'PHP']
}
filename = 'data.txt'


@app.route('/', methods=['GET'])
def root():
    try:
        # msg = Message("Survey Form",
        #               sender="automateuipath@gmail.com",
        #                 recipients=["debmitra9674@gmail.com", "sidmitra8732@gmail.com"])
        action = 'select'
        msg = Message("Survey Form",
                      sender="automateuipath@gmail.com",
                      recipients=fetch_from_table(action))
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
    all_data = dict(request.args.lists())  # ImmutableMultiDict
    print(f'all_data - {all_data}')
    print()
    l_username = ''.join(all_data.get('username'))
    l_vote1 = ','.join(all_data.get('field1'))  # Question 1 - answers
    l_vote2 = ','.join(all_data.get('field2'))  # Questions 2 - answers
    print(l_vote1)
    print(l_vote2)

    # ----- Building user reponse dict -------
    d_user_response_data = {}
    d_user_response_data['username'] = l_username
    d_user_response_data['vote1'] = l_vote1
    d_user_response_data['vote2'] = l_vote2
    action = 'insert'

    # ---- Building initiator dict -------------
    d_initiator_data = {}
    d_initiator_data['initiator_name'] = 'Deb'
    d_initiator_data['initiator_email'] = 'abcd@gmail.com'
    d_initiator_data['initiator_date'] = str(datetime.now().date())

    # ------- inserting/creating table -----------
    create_response = create_insert_relationship_table(action, d_user_response_data, d_initiator_data)
    print(f'Table Create response  -- {create_response}')

    return render_template('thankyou.html', data=poll_data)


if __name__ == "__main__":
    app.run(debug=True)

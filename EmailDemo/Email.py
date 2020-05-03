import smtplib
import email
from email import policy
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import urllib.request

fname = r"C:\Users\User\Documents\UipathDocs\GE\SurveyForm.html"
HtmlFile = open(fname, 'r', encoding='utf-8')
source_code = HtmlFile.read()

gmail_user = 'automateuipath@gmail.com'
gmail_password = 'Uipath@8732'

sent_from = gmail_user
# to = ['me@gmail.com', 'bill@gmail.com']
# msg = MIMEMultipart('alternative')
to = ['debmitra9674@gmail.com']
subject = 'OMG Super Important Message'
# body = 'Hey, what up?\n\n- You'
body = source_code
mail = email.message_from_string(body, policy=policy.default)
# msg.attach(MIMEText(body, 'html', 'utf-8'))
email_text = """\
From: %s
To: %s
Subject: %s
    
%s
""" % (sent_from, ", ".join(to), subject, body)
try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print("Email sent!")
except Exception as e:
    print("Something went wrong...")
    print(e)
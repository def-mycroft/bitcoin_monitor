import urllib
import json 
import smtplib
from email.mime.text import MIMEText


def get_data():
    """Gets data from blockchain API"""
    url = 'https://blockchain.info/ticker'
    response = urllib.urlopen(url)
    data = json.loads(response.read())['USD']
    return data


def send_email(message, to_address):
    """Sends an email"""
    sender_address = 'merc.test101@gmail.com'
    message = MIMEText(message)
    server = smtplib.SMTP("smtp.gmail.com:587")
    server.starttls()
    server.login(sender_address, 'kuc6zest')
    server.sendmail(sender_address, to_address, message.as_string())


def send_alert_message():
    price = get_data()['last']
    message = "BTC Price Alert! Last: %s" % price
    send_email(message, '6205068151@messaging.sprintpcs.com')



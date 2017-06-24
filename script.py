import urllib
import json 
import smtplib


def get_data():
    """Gets data from blockchain API"""
    url = 'https://blockchain.info/ticker'
    response = urllib.urlopen(url)
    data = json.loads(response.read())['USD']
    return data

def send_email():
    sender_address = 'merc.test101@gmail.com'
    to_address = 'dasenbrockjw@gmail.com'
    msg = 'here is a message'
    server = smtplib.SMTP("smtp.gmail.com:587")
    server.starttls()
    server.login('merc.test101@gmail.com', 'kuc6zest')
    server.sendmail(sender_address, to_address, msg)



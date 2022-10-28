import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.com/Sony-Alpha-a6400-Mirrorless-Camera/dp/B07MV3P74D/ref=sr_1_1_sspa?dchild=1&keywords=sony%2Bmirrorless%2Bcamera&qid=1634829939&sr=8-1-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyTFUyTFFXM0Y5NlFFJmVuY3J5cHRlZElkPUEwMjU2NDgxMzRCUVJOMFFDWFBaWiZlbmNyeXB0ZWRBZElkPUEwNDI5ODY5MVVJTkxMQThQUjA2QiZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU&th=1'

headers = {"user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.50'}

def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    print(soup.prettify())

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[0:5])

    if (converted_price < 1700):
        send_mail()

    print(title.strip())
    print(price)
    print(converted_price)

    if(converted_price>1.700):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('incisltd@gmail.com', 'A$E@N1r0InC1s')
    subject = 'Price fall down'
    body = 'Check the amazon link https://www.amazon.com/Sony-Alpha-a6400-Mirrorless-Camera/dp/B07MV3P74D/ref=sr_1_1_sspa?dchild=1&keywords=sony%2Bmirrorless%2Bcamera&qid=1634829939&sr=8-1-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyTFUyTFFXM0Y5NlFFJmVuY3J5cHRlZElkPUEwMjU2NDgxMzRCUVJOMFFDWFBaWiZlbmNyeXB0ZWRBZElkPUEwNDI5ODY5MVVJTkxMQThQUjA2QiZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU&th=1'
    msg = f"subject: {subject}\n\n{body}"

    server.sendmail(
        'incisltd@gmail.com',
        'mniniro@hotmail.com',
        msg
    )
    print('Email has been sent')

    server.quit()

while (True):
    check_price()
    time.sleep(60*60*24)

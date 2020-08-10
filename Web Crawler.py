import requests

from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page = 1

    while page <= max_pages:
        url = 'https://thenewboston.com/search.php?type=0&sort=reputation&page==' + str(page)
        source_code = requests.get(url, allow_redirects=False)

        # just get the code, no headers or anything
        plain_text = source_code.text.encode('ascii', 'replace')

        # BeautifulSoup objects can be sorted through easy
        soup = BeautifulSoup(plain_text,'html.parser')

        for link in soup.findAll('a', {'class': 'user-name'}):
            href = link.get('href')
            title = link.string  # just the text, not the HTML
            print(href)
            print(title)

            #get_single_item_data(href)
        page += 1


def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,"lxml")

    # if you want to gather photos from that user
    for item_name in soup.findAll('img', {'class': 'img-responsive'}): # all photos of the user
        photo='https://thenewboston.com'+item_name.get('src')
        print(photo)

    # if you want to gather links for a web crawler
    for link in soup.findAll('a'):
        href = link.get('href')
        print(href)





trade_spider(1)

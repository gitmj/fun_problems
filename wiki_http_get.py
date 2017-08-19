
import urllib2
import json
from bs4 import BeautifulSoup
from pprint import pprint

def count_token(token):
    url_addr = 'https://en.wikipedia.org/w/api.php?action=parse&section=0&prop=text&format=json&page=' + token
    data = urllib2.urlopen(url_addr)

    # data = json.load(data)

    # html = data['parse']['text']
    soup = BeautifulSoup(data, "lxml")

    text = soup.get_text().lower()

    index = text.find(token)
    count = 1
    while index != -1:
        index = text.find(token, index + 1)
        count += 1

    return count

if __name__ == '__main__':
    print count_token('pizza')

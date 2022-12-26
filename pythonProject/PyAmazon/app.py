import requests
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from fake_useragent import UserAgent


def get_soup_retry():
    ua = UserAgent()
    uag_rand = ua.random

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/96.0.4664.93 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9'
    }


    isCaptcha = True
    while isCaptcha:
        page = requests.get(url, headers=header)
        assert page.status_code == 200
        soup = BeautifulSoup(page.content, 'lxml')
        if 'captcha' in str(soup):
            print('bot detected')
        else:
            print('bot bypassed')
            return soup


def search_keyword(kw):
    count_page = 0
    count_asin = 0
    while True:
        count_page += 1
        url = f'https://www.amazon.com/s?k={kw}&page={count_page}'
        print(f'Getting page: {count_page} | {url}')
        soup = get_soup_retry(url)
        result = soup.find('div', attrs={'class': 's-main-slot s-result-list s-search-results sg-row'}).find_all('div', attrs={'data-component-type': 's-search-result'})

        for ids in result:
            count_asin += 1
            asin = ids['data-asin']
            url = f'https://www.amazon.com/dp/{asin}'
            print(f'{count_asin}. {url}')

        # last_page = soup.find('li', {'class': 'a-disabled a-last'})
        # if not last_page:
        #     pass
        # else:
        #     break

    search_keyword('headphones')


# driver = webdriver.Chrome()
# url = 'https://www.amazon.com/'
# driver.get(url)
# #
#
# def get_url(search_term):
#     """Generate a url from search term """
#     template = 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw={}&_sacat=0'
#     search_term = search_term.replace(' ', '+')
#     return template.format(search_term)
#
#
# url = get_url('electric scooter')
# print(url)
# driver.get(url)

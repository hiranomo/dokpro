import urllib.request
from urllib.parse import urljoin
from bs4 import BeautifulSoup


class Scraper:
    """

    ニュースをスクレイピングする

    Parameters
    ----------
    site : str
        ニュースサイトのURL
    urls : str
        見つけた記事のURLが被らないようするためのset_list

    """

    def __init__(self, site):
        self.site = site
        self.urls = set()

    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        sp = BeautifulSoup(html, 'html.parser')
        for tag in sp.find_all('a'):
            url = tag.get('href')
            if url is None:
                continue
            if not url.endswith('.html'):
                continue
            if url in self.urls:
                continue
            self.urls.add(url)
            full_url = urljoin(self.site, url)
            print('\n' + full_url)


news = 'https://trendy.nikkeibp.co.jp/news/'
Scraper(news).scrape()

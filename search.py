import requests
from bs4 import BeautifulSoup
from PySide6.QtWidgets import QListWidgetItem


class searchDmhyXml:

    def __init__(self, searchStr):
        self.searchStr = searchStr
        self.searchResult: list[searchResult] = []

    def doSearch(self):
        try:
            r = requests.get('https://dmhy.org/topics/rss/rss.xml?keyword=' +
                             self.searchStr +
                             '&sort_id=0&team_id=0&order=date-desc')
        except requests.RequestException:
            print('exception')
        else:
            self.searchResult.clear()
            r.encoding = 'utf-8'
            bs = BeautifulSoup(r.text, 'xml')
            datas = bs.find_all('item')
            for data in datas:
                result = searchResult()
                result.title = (str)(data.find('title')).replace(
                    '<title>', '').replace('</title>', '')
                result.torrent = (str)(data.find('enclosure').get('url'))
                self.searchResult.append(result)


class searchResult:

    def __init__(self):
        self.title = ''
        self.torrent = ''
        self.widget: QListWidgetItem = None

    def print(self):
        print((str)(self.index)+self.title+self.torrent)

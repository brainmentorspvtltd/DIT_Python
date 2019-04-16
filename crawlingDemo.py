# BeautifulSoup - Used to crawl data from web
import bs4
import urllib.request as url

path = "https://www.imdb.com/title/tt2631186/?ref_=fn_al_tt_1"

http = url.urlopen(path)
#print(http)
#lxml - library xtensible markup language
page = bs4.BeautifulSoup(http, 'lxml')

title = page.find('div', class_='title_wrapper')
#print(title.text)
title = title.text.replace('\n','')
#print(title)
text = ' '.join(title.split())
print(text)


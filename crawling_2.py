import bs4
import urllib.request as url

while True:
    path = "https://www.imdb.com/find?ref_=nv_sr_fn&q="
    movie = input("Enter movie name : ")
    http = url.urlopen(path+movie)

    page = bs4.BeautifulSoup(http, 'lxml')
    td = page.find('td', class_='result_text')
    #print(td)
    a = td.find('a')
    href = a['href']
    #print(href)
    newPath = 'https://www.imdb.com'+href
    #print(newPath)

    http = url.urlopen(newPath)

    page = bs4.BeautifulSoup(http, 'lxml')

    title = page.find('div', class_='title_wrapper')
    #print(title.text)
    title = title.text.replace('\n','')
    #print(title)
    text = ' '.join(title.split())
    print(text)

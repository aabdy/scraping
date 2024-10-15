import re
from requests_html import HTMLSession
import requests
import csv
from csv import writer
import cloudscraper

s = cloudscraper.create_scraper(delay=10,   browser={'custom': 'Mozilla',})
url = 'https://freelance.habr.com/tasks?categories=development_bots'
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:127.0) Gecko/20100101 Firefox/127.0'
    }
url
params = {
    'forceLocation': False,
    'locationId': 653040,
    'lastStamp': 1683748131,
    'limit': 30,
    'offset': 89,
    'categoryId': 4
}

session = HTMLSession()
def listToString(g):
    strl = " "
    return (strl.join(g))

with open('list_of_habr_links.csv', 'a', newline='', encoding='utf=8') as f_object:
    #writer_object = writer(f_object)
    response = session.get(url, headers=headers, params=params)
    list_of_links = []
    list_of_links = response.html.find('a[href*="/tasks/"]')
    lst = []
    list_of_new_links = []

    count = 0


    with open('list_of_habr_links.csv', 'r', newline='', encoding='utf=8') as source:
        links_reader = csv.reader(source)
        for i in range (1, len(list_of_links)):
            list_of_links[i] = listToString(list_of_links[i].links)

        for link in links_reader:
            #print(link)
            link = listToString(link)
            lst.append(link)

        for i in range (1, len(list_of_links)):
            for link in lst:
                if link == list_of_links[i]:
                    count = count + 1
                    #print(link)

                else:

                    continue

            if count == 0:
                #writer_object.writerow(list_of_links[i])
                list_of_new_links.append(list_of_links[i])

                #print(lst)
            else:
                print(count)
                count = 0

                continue
    #    print(lst)
    #    print(list_of_new_links)


        for i in range (1, len(list_of_new_links)):
            f_object.write(list_of_new_links[i])
            f_object.write('\n')
        #for link in list_of_new_links:


#            print(link)


with open('list_of_habr_links.csv', 'r', newline='', encoding='utf=8') as source:
    links_reader = csv.reader(source)
    for link in links_reader:
        link = listToString(link)
        link = ('https://freelance.habr.com') + link
        print(link)
#print(lst[1])

'''
with open('habr_page.html', 'w+') as file:
    file.write(response.text)
'''

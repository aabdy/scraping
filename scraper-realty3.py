import re
from requests_html import HTMLSession
import csv
from csv import writer

url = 'https://propertiabali.com/bali-villas-for-sale'
s = HTMLSession()
response = s.get(url)
for html in response.html:  
    about = html.find('a.noHover')
    i = len(about)
    #entering cycle
    k = []
    for l in range(0, i):
        for element in about:
            k.append(element.links)
    #still in cycle
    k = list(k)
    k[1] = list(k[1])
    def listToString(g):
        strl = " "
        return (strl.join(g))
    with open('villa2.txt', 'a', newline='', encoding='utf=8') as f_object:
        writer_object = writer(f_object)
        for j in range (0, i):
            st = listToString(k[j])
            urln = st
            session = HTMLSession()
            q = session.get(urln)   
            about = q.html.find('h1.title_text')
            about1 = q.html.find('.wpl_category_1 > div:nth-child(2)')
            about2 = q.html.find('#wpl-dbst-show3008 > span:nth-child(1)')
            lst = []
            lst_of_titles = []
            lst_of_descripts = []
            lst_of_areas = []
            for title in about:
                  lst_of_titles.append(title.text)
            for villa_desc in about1:
                  lst_of_descripts.append(villa_desc.text)
            for villa_area in about2:
                  lst_of_areas.append(villa_area.text)
            for item, bitem, nitem in zip(lst_of_areas, lst_of_titles, lst_of_descripts):
                  lst.append(item)
                  lst.append(bitem)
                  lst.append(nitem)
                  lst.append(k[j])              
                  writer_object.writerow(lst)
                  print(lst)
    f_object.close()
               
with open('villa2.txt', 'r') as file:
    x = file.read()
    x = x.replace('"\n', '",')     

with open('villa2.txt', 'w', newline='') as file:
    file.write(x)

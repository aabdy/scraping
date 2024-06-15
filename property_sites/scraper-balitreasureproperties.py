import re
from requests_html import HTMLSession
import csv
from csv import writer



url = 'https://balitreasureproperties.com/properties/freehold-leasehold-villa-for-sale'
s = HTMLSession()
response = s.get(url)

for html in response.html:
    print(html)
    about = html.find('div.right_part h2 [href]')
    i = len(about)
    k = []
    
    print(about)
    for l in range(0, i):
    
        for element in about:
           k.append(element.links)
    k = list(k)
    k[1] = list(k[1])
    def listToString(g):
        strl = " "
        return (strl.join(g))
    with open('villa5.csv', 'a', newline='', encoding='utf=8') as f_object:
        writer_object = writer(f_object)
        for j in range (0, i):
            st = listToString(k[j])
            urln = st
            #    print(type(urln))
            session = HTMLSession()
            q = session.get(urln)

            about = q.html.find('div.right_part h1')
            about1 = q.html.find('div.listing-info')
            about2 = q.html.find('div.right_part span.area:nth-child(3)')
          
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
                 
    f_object.close()

import re
from requests_html import HTMLSession
import csv

url = 'https://www.villabalisale.com/projects'
s = HTMLSession()
response = s.get(url)
about = response.html.find('a.btn-project-LM')
i = len(about)
k = []
for element in about:   
    k.append(element.links)
k = list(k)
k[1] = list(k[1])
with open('villa.csv', 'w', newline='') as csvfile:
    f = csv.writer(csvfile, dialect = 'excel')
    for j in range (0, i):
        st = listToString(k[j])       
        urln = st       
        session = HTMLSession()
        q = session.get(urln)
        about = q.html.find('.detail-villa-title')
        about1 = q.html.find('.detail-villa-desc')        
        lst = []
        lst_of_titles = []
        lst_of_descripts = []
        for title in about:
            lst_of_titles.append(title.text)
        for villa_desc in about1:
            lst_of_descripts.append(villa_desc.text)
        for item in zip(lst_of_titles, lst_of_descripts):
            lst.append(item)
            lst.append([st]) 
            
        for element in lst:
            str(element).replace('"\n', '"\n,')
       
        f.writerows(lst)

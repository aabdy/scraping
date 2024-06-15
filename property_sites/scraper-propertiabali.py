import re
from requests_html import HTMLSession
import csv
from csv import writer


url = 'https://propertiabali.com/bali-villas-for-sale'
headers = {
'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.7) Gecko/2009032803'
}
s = HTMLSession()
response = s.get(url, headers=headers)
def listToString(g):
        strl = " "
        return (strl.join(g))

about = response.html.find('h2 [target="_self"]')
i = len(about)

k = []
        

for element in about:
        k.append(element.absolute_links)
with open('vila2_list_of_links.csv', 'a', newline='', encoding='utf=8') as file_with_links:
        writer_file_with_links = writer(file_with_links)
        writer_file_with_links.writerows(k)
        file_with_links.close()

next_page = []
next_page = response.html.find('[aria-label="Next"]')
print(next_page)


url = listToString(next_page[0].absolute_links)
       
while url:        
# repeat until we got correct response from server:
        while True:
                try:
                        response = s.get(url, headers=headers)
                        break
                        
                except request.exceptions.ConnectionError:
                        sleep(3)
                        continue
        
        next_page = []
        next_page = response.html.find('[aria-label="Next"]')
        
        if len(next_page) == 0:
                break
        url = listToString(next_page[0].absolute_links)
        print('url=', url)
 
        
        about = []
        about = response.html.find('h2 [target="_self"]')

        for element in about:
                k.append(element.absolute_links)
        with open('vila2_list_of_links.csv', 'a', newline='', encoding='utf=8') as file_with_links:
                writer_file_with_links = writer(file_with_links)
                writer_file_with_links.writerows(k)
                file_with_links.close()
        
       


i = len(k)
with open('villa2.csv', 'a', newline='', encoding='utf=8') as f_object:
    writer_object = writer(f_object)
    for j in range (0, i):
            st = listToString(k[j])
            urln = st
            session = HTMLSession()
            while True:
                    try:
                            q = session.get(urln)
                            break
                
                    except request.exceptions.ConnectionError:
                            sleep(3)
                            continue
               
            about = q.html.find('h1')
            about1 = q.html.find('ul', containing ='Property')
            about2 = q.html.find('.detail-area > span:nth-child(2)')
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
            for item1, item2, item3 in zip(lst_of_areas, lst_of_titles, lst_of_descripts):

                  lst.append(item1)
                  lst.append(item2)
                  lst.append(item3)
                  lst.append(k[j])              
                  writer_object.writerow(lst)
                  
    f_object.close()
               
with open('villa2.csv', 'r') as file:
    x = file.read()
    x = x.replace('"\n', '",')     

with open('villa2.csv', 'w', newline='') as file:
    file.write(x)

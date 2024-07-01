import re
from requests_html import HTMLSession
import csv
from csv import writer


url = 'https://iherb.group/'
s = HTMLSession()
response = s.get(url)
main_links = response.html.find('div.footer-box_col:nth-child(3) > ul:nth-child(2) > li')
#gathering product categories
lim = len(main_links)
list_of_links = []

for link in main_links:
    list_of_links.append(link.absolute_links)
    #writing links to categories to the list
def listToString(g):
    strl = " "
    return (strl.join(g))



with open('herb.csv', 'a', newline='', encoding='utf=8') as f_object:
    writer_object = writer(f_object)
    for j in range (0, lim):
    #visiting each category
        st = listToString(list_of_links[j])
        urln = st
        session = HTMLSession()
        q = session.get(urln)
        print(urln)
        next_page = q.html.find('a.inline-link')#find next page link
        url = (next_page[0].absolute_links)
        def listToString(g):
            strl = " "
            return (strl.join(g))
        while True:
            session = HTMLSession()
            _link = listToString(list(url))
            response = session.get(_link)
            next_page = []
            next_page = response.html.find('ul.pagination li a.inline-link')
            if len(next_page) == 1:
                break
            else:
                url = next_page[1].absolute_links
                print(url)
                products = response.html.find('[data-product-num]')
               
                list_of_products = []
                for element in products:
                    list_of_products.append(element.absolute_links)
                    #gathering links to each product in category		
            
                k = len(list_of_products)
                #print(k)
                for l in range (0, k):
                    session2 = HTMLSession()
                    #visiting each link with a product
                    str_link = listToString(list_of_products[l])
                    t = session2.get(str_link)
                    product_name = t.html.find('h1.product_name')
                    product_description = t.html.find('span [itemprop="sku"]')
                    product_features = t.html.find('table.Product__features')
                    product_price = t.html.find('.product__price')
                    product_image = t.html.find('[id^="product-image"]')

                    lst = []
                    list_of_product_names = []
                    list_of_descriptions = []
                    list_of_feature = []
                    list_of_prices = []
                    list_of_images = []
                    for name in product_name:
                        list_of_product_names.append(name.text)
                    for description in product_description:
                        list_of_descriptions.append(description.text)
                    for feature in product_features:
                        list_of_feature.append(feature.text)
                    for price in product_price:
                        list_of_prices.append(price.text)
                    for image in product_image:
                        list_of_images.append(image.absolute_links)
                    str_val = str(list_of_images)

                    for name, description, feature, price in zip(list_of_product_names, list_of_descriptions, list_of_feature, list_of_prices):
                        lst.append(name)
                        lst.append(description)
                        lst.append(feature)
                        lst.append(price)
                        lst.append(str_link)
                        lst.append(str_val)

                    writer_object.writerow(lst)
f_object.close()
print('end')



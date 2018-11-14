from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = "https://houston.craigslist.org/d/for-sale/search/sss"

# scrape the web page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# create a file to write parsed data
filename = "Lin_HW4_ScrapedData.csv"
f = open(filename, 'w')
headers = "Craigslist: items for sale in Houston\n"
f.write(headers)

# applying BeautifulSoup to the obtained html
page_soup = soup(page_html, "html.parser")

# find all the result in the first page
containers = page_soup.findAll("li", {"class": "result-row"})
for container in containers:
    try:
        date_container = container.findAll("time", {"class": "result-date"})
        date = date_container[0].text.strip()
        print("Date:", date)
    except: date='NaN'
    try:
        location_container = container.findAll("span", {"class": "result-hood"})
        location = location_container[0].text.strip()
        print("Location:", location)
    except: location='NaN'
    try:
        price_container = container.findAll("span", {"class": "result-price"})
        price = price_container[0].text.strip()
        print("Price:", price)
    except: price='NaN'
    try:
        description_container = container.findAll("a", {"class": "result-title hdrlnk"})
        description = description_container[0].text.strip()
        print("Description:", description)
    except: description = 'NaN'
    f.write(date + ',' + location.replace(",", ";") + ',' + description.replace(",", ";") + ',' + price + '\n')

#Next pages (for all)
i=120
my_url = "https://houston.craigslist.org/d/for-sale/search/sss?s=" + str(i)
while True:
    i = i+120
    try:
        my_url = "https://houston.craigslist.org/d/for-sale/search/sss?s=" + str(i)
        uClient = uReq(my_url)  # sends GET request to URL
        page_html = uClient.read()  # reads returned data and puts it in a variable
        uClient.close()

        page_soup = soup(page_html, "html.parser")  # applying BeautifulSoup to the obtained html

        containers = page_soup.findAll("li", {"class": "result-row"})

        for container in containers:
            try:
                date_container = container.findAll("time", {"class": "result-date"})
                date = date_container[0].text.strip()
                print("Date:", date)
            except:
                date = 'NaN'
            try:
                location_container = container.findAll("span", {"class": "result-hood"})
                location = location_container[0].text.strip()
                print("Location:", location)
            except:
                location = 'NaN'
            try:
                price_container = container.findAll("span", {"class": "result-price"})
                price = price_container[0].text.strip()
                print("Price:", price)
            except:
                price = 'NaN'
            try:
                description_container = container.findAll("a", {"class": "result-title hdrlnk"})
                description = description_container[0].text.strip()
                print("Description:", description)
            except:
                description = 'NaN'
            f.write(date + ',' + location.replace(",", ";") + ',' + description.replace(",", ";") + ',' + price + '\n')
    except:
        f.close()
        break

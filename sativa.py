import requests
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import time
import csv

# Target classes
strain_tile = 'strain-tile'

# Website link
link = 'https://www.leafly.com/strains/lists/category/sativa'

# Get the website
# source = requests.get(link).text

driver = webdriver.Chrome()
driver.get(link)

# Clicks yes I am 18
try:
    continue_button = driver.find_element_by_id("tou-continue")
    continue_button.click()
except:
    pass

# Navigates to sativa page
try:
    continue_button = driver.find_element_by_xpath(
        "/html/body/main/div/section[2]/div[3]/div/a[3]")
    continue_button.click()
except:
    pass

# Closes cookie popup
try:
    continue_button = driver.find_element_by_xpath(
        "/html/body/div[1]/div[8]/button")
    continue_button.click()
except:
    pass

# Waits for popup
time.sleep(15)

# Closes popup
try:
    continue_button = driver.find_element_by_xpath(
        "/html/body/div[1]/div[9]/div/button")
    continue_button.click()
except:
    pass


# scrolling

lastHeight = driver.execute_script("return document.body.scrollHeight")
pause = 0.8

print("Checking page now ...")
while True:
    try:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(pause)
        newHeight = driver.execute_script("return document.body.scrollHeight")
        if newHeight == lastHeight:
            break
        lastHeight = newHeight
        loadmore = driver.find_element_by_xpath("//button[contains(text(),'load more')]")
        loadmore.click()
    except NoSuchElementException:
        print("Reached bottom of page")
        break

# Load the source into bs4
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Setup csv file
csv_sativa = open('csv_sativa.csv', 'w')
csv_writer = csv.writer(csv_sativa)
csv_writer.writerow(['strain_name', 'strain_variant'])

# print(soup.prettify().encode('utf-8'))

strain_tile_ob = soup.find_all('a', class_=strain_tile)

strain_name = ''
strain_variant = ''

for ob in strain_tile_ob:
    try:
        strain_name = ob.div.text
        strain_variant = ob.span.text
    except Exception as e:
        pass

    csv_writer.writerow([strain_name, strain_variant])


csv_sativa.close()

# Save the page to the file
# with open("sativa_html.html", "w") as file:
#     file.write(soup.prettify().encode('utf-8'))

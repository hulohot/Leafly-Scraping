import requests
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import time
import csv

# Target classes
strain_tile = 'strain-tile'

# Website link
link = 'https://www.leafly.com/strains/lists/category/indica'
base_url = 'https://www.leafly.com'

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

# Navigates to indica page
try:
    continue_button = driver.find_element_by_xpath(
        "/html/body/main/div/section[2]/div[3]/div/a[2]")
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
pause = 1

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
csv_indica = open('csv_indica.csv', 'w')
csv_writer = csv.writer(csv_indica)
csv_writer.writerow(['strain_name', 'strain_variant', 'strain_url', ''])

# print(soup.prettify().encode('utf-8'))

strain_tile_ob = soup.find_all('a', class_=strain_tile)

print("Finished Loading Page!")
print("Found %d items" % len(strain_tile_ob))

strain_name = ''
strain_variant = ''
strain_url = ''

can_ob = []

for ob in strain_tile_ob:
    try:
        strain_name = ob.div.text.encode('utf-8')
        strain_variant = ob.span.text.encode('utf-8')
        strain_url = base_url + ob['href']
    except Exception as e:
        strain_name = 'Not Found'
        strain_variant = 'Not Found'
        strain_url = 'Not Found'
        pass

    csv_writer.writerow([strain_name, strain_variant, strain_url])


csv_indica.close()

# Save the page to the file
# with open("indica_html.html", "w") as file:
#     file.write(soup.prettify().encode('utf-8'))

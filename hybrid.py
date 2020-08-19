import requests
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import time
import csv
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("window-size=1400,600")


def getStrainLink(obj):
    return 'https://www.leafly.com/' + str(obj.get('href'))


# Target classes
strain_tile = 'strain-tile'

# Website link
link = 'https://www.leafly.com/strains/lists/category/hybrid'

# Get the website
# source = requests.get(link).text

driver = webdriver.Chrome(chrome_options=options)
driver.get(link)

time.sleep(2)

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

# Closes cookies banner
try:
    continue_button = driver.find_element_by_xpath(
        "/html/body/div[1]/div[7]/button")
    continue_button.click()
    print('Closed Cookie Banner')
except:
    pass

# Waits for popup
time.sleep(20)

# Closes Newsletter popup
try:
    continue_button = driver.find_element_by_xpath(
        "/html/body/div[1]/div[8]/div/button")
    continue_button.click()
    print('Closed out of news letter')
except:
    pass

# Load the source into bs4
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Setup csv file
csv_hybrid = open('csv_hybrid.csv', 'w', newline='')
csv_writer = csv.writer(csv_hybrid)
csv_writer.writerow(['category', 'name', 'variant', 'adj-1', 'adj-2', 'adj-3', 'description', 'image_url', 'feelings-1-name', 'feelings-1-percent',
                     'feelings-2-name', 'feelings-2-percent', 'feelings-3-name', 'feelings-3-percent', 'feelings-4-name', 'feelings-4-percent', 'feelings-5-name', 'feelings-5-percent', 'helps-with-1-name', 'helps-with-1-percent', 'helps-with-2-name', 'helps-with-2-percent', 'helps-with-3-name', 'helps-with-3-percent', 'helps-with-4-name', 'helps-with-4-percent', 'helps-with-5-name', 'helps-with-5-percent', 'negatives-1-name', 'negatives-1-percent', 'negatives-2-name', 'negatives-2-percent', 'negatives-3-name', 'negatives-3-percent', 'negatives-4-name', 'negatives-4-percent', 'negatives-5-name', 'negatives-5-percent', ])


# Find number of pages
num_of_pages = int(driver.find_element_by_xpath(
    "/html/body/main/div/div[2]/div[4]/span").text.split(' ')[2])
current_page = 1

print("Checking page now ...")
while True:
    try:
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        strain_tile_ob = soup.find_all('a', class_=strain_tile)
        strain_name = 'null'
        strain_variant = 'null'
        adj_1 = 'null'
        adj_2 = 'null'
        adj_3 = 'null'
        description = 'null'
        image_url = 'null'
        feelings_1_name = 'null'
        feelings_2_name = 'null'
        feelings_3_name = 'null'
        feelings_4_name = 'null'
        feelings_5_name = 'null'
        feelings_1_percent = 'null'
        feelings_2_percent = 'null'
        feelings_3_percent = 'null'
        feelings_4_percent = 'null'
        feelings_5_percent = 'null'
        helps_with_1_name = 'null'
        helps_with_2_name = 'null'
        helps_with_3_name = 'null'
        helps_with_4_name = 'null'
        helps_with_5_name = 'null'
        helps_with_1_percent = 'null'
        helps_with_2_percent = 'null'
        helps_with_3_percent = 'null'
        helps_with_4_percent = 'null'
        helps_with_5_percent = 'null'
        negatives_1_name = 'null'
        negatives_2_name = 'null'
        negatives_3_name = 'null'
        negatives_4_name = 'null'
        negatives_5_name = 'null'
        negatives_1_percent = 'null'
        negatives_2_percent = 'null'
        negatives_3_percent = 'null'
        negatives_4_percent = 'null'
        negatives_5_percent = 'null'

        for obj in strain_tile_ob:
            try:
                strain_name = obj.div.next_sibling.text
                strain_variant = obj.span.text

                # Get Strain Link
                strain_link = getStrainLink(obj)

                # Visit strain page
                driver.get(strain_link)

                # Wait for page to load image
                strain_soup = BeautifulSoup(driver.page_source, 'html.parser')

                # Get data from strain page
                # Adjs
                if driver.find_element_by_xpath('/html/body/main/div/div/article/div[2]/div[2]/ul/li[1]/div/span'):
                    adj_1 = driver.find_element_by_xpath(
                        '/html/body/main/div/div/article/div[2]/div[2]/ul/li[1]/div/span').text
                print(adj_1)
                if driver.find_element_by_xpath('/html/body/main/div/div/article/div[2]/div[2]/ul/li[2]/div/span'):
                    adj_2 = driver.find_element_by_xpath(
                        '/html/body/main/div/div/article/div[2]/div[2]/ul/li[2]/div/span').text
                if driver.find_element_by_xpath('/html/body/main/div/div/article/div[2]/div[2]/ul/li[3]/div/span'):
                    adj_3 = driver.find_element_by_xpath(
                        '/html/body/main/div/div/article/div[2]/div[2]/ul/li[3]/div/span').text
                # Description
                if driver.find_element_by_xpath('/html/body/main/div/div/article/div[3]/div/div/div/p'):
                    description = driver.find_element_by_xpath(
                        '/html/body/main/div/div/article/div[3]/div/div/div/p').text
                print(description)

                # Image URL
                # if driver.find_element_by_xpath('/html/body/main/div/div/div/div/section/div[1]/div/div/div[1]/div/div/ul/li[1]/div/img'):
                #     print('Found an image')
                #     print(driver.find_element_by_xpath(
                #         '/html/body/main/div/div/div/div/section/div[1]/div/div/div[1]/div/div/ul/li[1]/div/img').get('src'))
                #     image_url = driver.find_element_by_xpath(
                #         '/html/body/main/div/div/div/div/section/div[1]/div/div/div[1]/div/div/ul/li[1]/div/img').get('src')
                #     print(image_url)
                # else:
                #     print('No Image found')

                # Feelings
                if driver.find_element_by_xpath('/html/body/main/div/div/article/section[1]/div[2]/div/div[1]/div[1]/div[1]'):
                    feelings_1_name = ' '.join(driver.find_element_by_xpath(
                        '/html/body/main/div/div/article/section[1]/div[2]/div/div[1]/div[1]/div[1]').text.split(' ')[:-1])
                if driver.find_element_by_xpath('/html/body/main/div/div/article/section[1]/div[2]/div/div[1]/div[2]/div[1]'):
                    feelings_2_name = ' '.join(driver.find_element_by_xpath(
                        '/html/body/main/div/div/article/section[1]/div[2]/div/div[1]/div[2]/div[1]').text.split(' ')[:-1])
                if driver.find_element_by_xpath('/html/body/main/div/div/article/section[1]/div[2]/div/div[1]/div[3]/div[1]'):
                    feelings_3_name = ' '.join(driver.find_element_by_xpath(
                        '/html/body/main/div/div/article/section[1]/div[2]/div/div[1]/div[3]/div[1]').text.split(' ')[:-1])
                if driver.find_element_by_xpath('/html/body/main/div/div/article/section[1]/div[2]/div/div[1]/div[4]/div[1]'):
                    feelings_4_name = ' '.join(driver.find_element_by_xpath(
                        '/html/body/main/div/div/article/section[1]/div[2]/div/div[1]/div[4]/div[1]').text.split(' ')[:-1])
                if driver.find_element_by_xpath('/html/body/main/div/div/article/section[1]/div[2]/div/div[1]/div[5]/div[1]'):
                    feelings_5_name = ' '.join(driver.find_element_by_xpath(
                        '/html/body/main/div/div/article/section[1]/div[2]/div/div[1]/div[5]/div[1]').text.split(' ')[:-1])

                if driver.find_element_by_xpath('/html/body/main/div/div/article/section[1]/div[2]/div/div[1]/div[1]/div[1]/span'):
                    feelings_1_percent = driver.find_element_by_xpath(
                        '/html/body/main/div/div/article/section[1]/div[2]/div/div[1]/div[1]/div[1]/span').text
                if driver.find_element_by_xpath('/html/body/main/div/div/article/section[1]/div[2]/div/div[1]/div[2]/div[1]/span'):
                    feelings_2_percent = driver.find_element_by_xpath(
                        '/html/body/main/div/div/article/section[1]/div[2]/div/div[1]/div[2]/div[1]/span').text
                if driver.find_element_by_xpath('/html/body/main/div/div/article/section[1]/div[2]/div/div[1]/div[3]/div[1]/span'):
                    feelings_3_percent = driver.find_element_by_xpath(
                        '/html/body/main/div/div/article/section[1]/div[2]/div/div[1]/div[3]/div[1]/span').text
                if driver.find_element_by_xpath('/html/body/main/div/div/article/section[1]/div[2]/div/div[1]/div[4]/div[1]/span'):
                    feelings_4_percent = driver.find_element_by_xpath(
                        '/html/body/main/div/div/article/section[1]/div[2]/div/div[1]/div[4]/div[1]/span').text
                if driver.find_element_by_xpath('/html/body/main/div/div/article/section[1]/div[2]/div/div[1]/div[5]/div[1]/span'):
                    feelings_5_percent = driver.find_element_by_xpath(
                        '/html/body/main/div/div/article/section[1]/div[2]/div/div[1]/div[5]/div[1]/span').text
                
                # Helps With
                if driver.find_element_by_xpath('/html/body/main/div/div/article/section[1]/div[2]/div/div[2]/div[1]/div[1]'):
                    helps_with_1_name = ' '.join(driver.find_element_by_xpath(
                        '/html/body/main/div/div/article/section[1]/div[2]/div/div[2]/div[1]/div[1]').text.split(' ')[:-1])
                if driver.find_element_by_xpath('/html/body/main/div/div/article/section[1]/div[2]/div/div[2]/div[2]/div[1]'):
                    helps_with_2_name = ' '.join(driver.find_element_by_xpath(
                        '/html/body/main/div/div/article/section[1]/div[2]/div/div[2]/div[2]/div[1]').text.split(' ')[:-1])
                if driver.find_element_by_xpath('/html/body/main/div/div/article/section[1]/div[2]/div/div[2]/div[3]/div[1]'):
                    helps_with_3_name = ' '.join(driver.find_element_by_xpath(
                        '/html/body/main/div/div/article/section[1]/div[2]/div/div[2]/div[3]/div[1]').text.split(' ')[:-1])
                if driver.find_element_by_xpath('/html/body/main/div/div/article/section[1]/div[2]/div/div[2]/div[4]/div[1]'):
                    helps_with_4_name = ' '.join(driver.find_element_by_xpath(
                        '/html/body/main/div/div/article/section[1]/div[2]/div/div[2]/div[4]/div[1]').text.split(' ')[:-1])
                if driver.find_element_by_xpath('/html/body/main/div/div/article/section[1]/div[2]/div/div[2]/div[5]/div[1]'):
                    helps_with_5_name = ' '.join(driver.find_element_by_xpath(
                        '/html/body/main/div/div/article/section[1]/div[2]/div/div[2]/div[5]/div[1]').text.split(' ')[:-1])

                if driver.find_element_by_xpath('/html/body/main/div/div/article/section[1]/div[2]/div/div[2]/div[1]/div[1]/span'):
                    helps_with_1_percent = driver.find_element_by_xpath(
                        '/html/body/main/div/div/article/section[1]/div[2]/div/div[2]/div[1]/div[1]/span').text
                if driver.find_element_by_xpath('/html/body/main/div/div/article/section[1]/div[2]/div/div[2]/div[2]/div[1]/span'):
                    helps_with_2_percent = driver.find_element_by_xpath(
                        '/html/body/main/div/div/article/section[1]/div[2]/div/div[2]/div[2]/div[1]/span').text
                if driver.find_element_by_xpath('/html/body/main/div/div/article/section[1]/div[2]/div/div[2]/div[3]/div[1]/span'):
                    helps_with_3_percent = driver.find_element_by_xpath(
                        '/html/body/main/div/div/article/section[1]/div[2]/div/div[2]/div[3]/div[1]/span').text
                if driver.find_element_by_xpath('/html/body/main/div/div/article/section[1]/div[2]/div/div[2]/div[4]/div[1]/span'):
                    helps_with_4_percent = driver.find_element_by_xpath(
                        '/html/body/main/div/div/article/section[1]/div[2]/div/div[2]/div[4]/div[1]/span').text
                if driver.find_element_by_xpath('/html/body/main/div/div/article/section[1]/div[2]/div/div[2]/div[5]/div[1]/span'):
                    helps_with_5_percent = driver.find_element_by_xpath(
                        '/html/body/main/div/div/article/section[1]/div[2]/div/div[2]/div[5]/div[1]/span').text
                
                # Negatives
                if driver.find_element_by_xpath('/html/body/main/div/div/article/section[1]/div[2]/div/div[3]/div[1]/div[1]'):
                    negatives_1_name = ' '.join(driver.find_element_by_xpath(
                        '/html/body/main/div/div/article/section[1]/div[2]/div/div[3]/div[1]/div[1]').text.split(' ')[:-1])
                if driver.find_element_by_xpath('/html/body/main/div/div/article/section[1]/div[2]/div/div[3]/div[2]/div[1]'):
                    negatives_2_name = ' '.join(driver.find_element_by_xpath(
                        '/html/body/main/div/div/article/section[1]/div[2]/div/div[3]/div[2]/div[1]').text.split(' ')[:-1])
                if driver.find_element_by_xpath('/html/body/main/div/div/article/section[1]/div[2]/div/div[3]/div[3]/div[1]'):
                    negatives_3_name = ' '.join(driver.find_element_by_xpath(
                        '/html/body/main/div/div/article/section[1]/div[2]/div/div[3]/div[3]/div[1]').text.split(' ')[:-1])
                if driver.find_element_by_xpath('/html/body/main/div/div/article/section[1]/div[2]/div/div[3]/div[4]/div[1]'):
                    negatives_4_name = ' '.join(driver.find_element_by_xpath(
                        '/html/body/main/div/div/article/section[1]/div[2]/div/div[3]/div[4]/div[1]').text.split(' ')[:-1])
                if driver.find_element_by_xpath('/html/body/main/div/div/article/section[1]/div[2]/div/div[3]/div[5]/div[1]'):
                    negatives_5_name = ' '.join(driver.find_element_by_xpath(
                        '/html/body/main/div/div/article/section[1]/div[2]/div/div[3]/div[5]/div[1]').text.split(' ')[:-1])

                if driver.find_element_by_xpath('/html/body/main/div/div/article/section[1]/div[2]/div/div[3]/div[1]/div[1]/span'):
                    negatives_1_percent = driver.find_element_by_xpath(
                        '/html/body/main/div/div/article/section[1]/div[2]/div/div[3]/div[1]/div[1]/span').text
                if driver.find_element_by_xpath('/html/body/main/div/div/article/section[1]/div[2]/div/div[3]/div[2]/div[1]/span'):
                    negatives_2_percent = driver.find_element_by_xpath(
                        '/html/body/main/div/div/article/section[1]/div[2]/div/div[3]/div[2]/div[1]/span').text
                if driver.find_element_by_xpath('/html/body/main/div/div/article/section[1]/div[2]/div/div[3]/div[3]/div[1]/span'):
                    negatives_3_percent = driver.find_element_by_xpath(
                        '/html/body/main/div/div/article/section[1]/div[2]/div/div[3]/div[3]/div[1]/span').text
                if driver.find_element_by_xpath('/html/body/main/div/div/article/section[1]/div[2]/div/div[3]/div[4]/div[1]/span'):
                    negatives_4_percent = driver.find_element_by_xpath(
                        '/html/body/main/div/div/article/section[1]/div[2]/div/div[3]/div[4]/div[1]/span').text
                if driver.find_element_by_xpath('/html/body/main/div/div/article/section[1]/div[2]/div/div[3]/div[5]/div[1]/span'):
                    negatives_5_percent = driver.find_element_by_xpath(
                        '/html/body/main/div/div/article/section[1]/div[2]/div/div[3]/div[5]/div[1]/span').text

                
                

                # Write to file
                print('Writing ' + strain_name)
                csv_writer.writerow(
                    ['Hybrid', strain_name, strain_variant, adj_1, adj_2, adj_3, description, image_url, feelings_1_name, feelings_1_percent, feelings_2_name, feelings_2_percent, feelings_3_name, feelings_3_percent, feelings_4_name, feelings_4_percent, feelings_5_name, feelings_5_percent, helps_with_1_name, helps_with_1_percent, helps_with_2_name, helps_with_2_percent, helps_with_3_name, helps_with_3_percent, helps_with_4_name, helps_with_4_percent, helps_with_5_name, helps_with_5_percent, negatives_1_name, negatives_1_percent, negatives_2_name, negatives_2_percent, negatives_3_name, negatives_3_percent, negatives_4_name, negatives_4_percent, negatives_5_name, negatives_5_percent])

                # Return to main strains listing page
                driver.get(link + '?page=' + str(current_page))

            except Exception as e:
                pass

        if current_page < num_of_pages:
            current_page += 1
            driver.get(link + '?page=' + str(current_page))
        else:
            break

    except NoSuchElementException:
        print("Reached bottom of page")
        break

print('End of scraping')

# Close CSV
csv_hybrid.close()

driver.close()

# Save the page to the file
# with open("sativa_html.html", "w") as file:
#     file.write(soup.prettify().encode('utf-8'))

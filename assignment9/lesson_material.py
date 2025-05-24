from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import csv
import json

options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Enable headless mode
options.add_argument("--window-size=1920x1080")  # Optional, set window size

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()), options=options
)
driver.get("https://en.wikipedia.org/wiki/Web_scraping")


def example1():

    title = (
        driver.title
    )  # Find the title.  Parts of the header are accessed directly, not via find_element(), which only works on the body
    print(title)

    body = driver.find_element(
        By.CSS_SELECTOR, "body"
    )  # Find the first body element, typically only one
    if body:
        links = body.find_elements(
            By.CSS_SELECTOR, "a"
        )  # Find all the links in the body.
        if len(links) > 0:
            print(
                "href: ", links[0].get_attribute("href")
            )  # getting the value of an attribute

    main_div = body.find_element(By.CSS_SELECTOR, 'div[id="mw-content-text"]')
    if main_div:
        bolds = main_div.find_elements(By.CSS_SELECTOR, "b")
        if len(bolds) > 0:
            print("bolds: ", bolds[0].text)

    # Extract all images with their src attributes
    images = [
        (img.get_attribute("src"))
        for img in body.find_elements(By.CSS_SELECTOR, "img[src]")
    ]  # all img elements with a src attribute
    print("Image Sources:", images)
    # hmm, this example uses a list comprehension.  We haven't talked about those.  This is the same as:
    image_entries = driver.find_elements(By.CSS_SELECTOR, "img[src]")
    images = []
    for img in image_entries:
        images.append(img.get_attribute("src"))

    print("Image Sources:", images)

    # You can then close the browser connection with:
    driver.quit()


# example1()
# Web scraping - Wikipedia
# href:  https://en.wikipedia.org/wiki/Web_scraping#bodyContent
# bolds:  needs additional citations for verification
# Image Sources: ['https://en.wikipedia.org/static/images/icons/wikipedia.png', 'https://en.wikipedia.org/static/images/mobile/copyright/wikipedia-wordmark-en.svg', 'https://en.wikipedia.org/static/images/mobile/copyright/wikipedia-tagline-en.svg', 'https://upload.wikimedia.org/wikipedia/en/thumb/9/99/Question_book-new.svg/60px-Question_book-new.svg.png', 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/Ambox_globe_content.svg/60px-Ambox_globe_content.svg.png', 'https://en.wikipedia.org/static/images/footer/wikimedia.svg', 'https://en.wikipedia.org/w/resources/assets/mediawiki_compact.svg']
# Image Sources: ['https://en.wikipedia.org/static/images/icons/wikipedia.png', 'https://en.wikipedia.org/static/images/mobile/copyright/wikipedia-wordmark-en.svg', 'https://en.wikipedia.org/static/images/mobile/copyright/wikipedia-tagline-en.svg', 'https://upload.wikimedia.org/wikipedia/en/thumb/9/99/Question_book-new.svg/60px-Question_book-new.svg.png', 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/Ambox_globe_content.svg/60px-Ambox_globe_content.svg.png', 'https://en.wikipedia.org/static/images/footer/wikimedia.svg', 'https://en.wikipedia.org/w/resources/assets/mediawiki_compact.svg']

# COMMON STRUCTURE:
# try:
#     driver.get("https://nonsense.never.com")
# except Exception as e:
#     print("couldn't get the web page")
#     print(f"Exception: {type(e).__name__} {e}")
# finally:
#     driver.quit()


# ROBOTS.txt
def example2():
    robots_url = "https://en.wikipedia.org/robots.txt"
    driver.get(robots_url)
    print(driver.page_source)
    driver.quit()


# example2()
# Print Output:
# <html><head><meta name="color-scheme" content="light dark"></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;"># robots.txt for http://www.wikipedia.org/ and friends
#
# Please note: There are a lot of pages on this site, and there are
# some misbehaved spiders out there that go _way_ too fast. If you're
# irresponsible, your access to the site may be blocked.
# ... a lot more rules


def example3():
    # This script assumes than the next immediate sibling <div> of See also:
    # would be a list of links, which is not always true.
    # Sometimes they incorporate different stuff, so link would not always be the very next one in line
    see_also_h2 = driver.find_element(
        By.CSS_SELECTOR, '[id="See_also"]'
    )  # our starting point
    links = []
    if see_also_h2:
        parent_div = see_also_h2.find_element(By.XPATH, "..")  # up to the parent div
        if parent_div:
            see_also_div = parent_div.find_element(
                By.XPATH, "following-sibling::div"
            )  # over to the div with all the links
            link_elements = see_also_div.find_elements(By.CSS_SELECTOR, "a")
            for link in link_elements:
                print(f"{link.text}: {link.get_attribute('href')}")
                name = link.text.strip()
                url = link.get_attribute("href")
                if name and url:
                    links.append({"name": name, "url": url})
    driver.quit()


# example3()

# Archive.today: https://en.wikipedia.org/wiki/Archive.today
# Comparison of feed aggregators: https://en.wikipedia.org/wiki/Comparison_of_feed_aggregators
# Data scraping: https://en.wikipedia.org/wiki/Data_scraping
# Data wrangling: https://en.wikipedia.org/wiki/Data_wrangling
# Importer: https://en.wikipedia.org/wiki/Importer_(computing)
# Job wrapping: https://en.wikipedia.org/wiki/Job_wrapping
# Knowledge extraction: https://en.wikipedia.org/wiki/Knowledge_extraction
# OpenSocial: https://en.wikipedia.org/wiki/OpenSocial
# Scraper site: https://en.wikipedia.org/wiki/Scraper_site
# Fake news website: https://en.wikipedia.org/wiki/Fake_news_website
# Spamdexing: https://en.wikipedia.org/wiki/Spamdexing
# Domain name drop list: https://en.wikipedia.org/wiki/Domain_name_drop_list
# Text corpus: https://en.wikipedia.org/wiki/Text_corpus
# Web archiving: https://en.wikipedia.org/wiki/Web_archiving
# Web crawler: https://en.wikipedia.org/wiki/Web_crawler
# Offline reader: https://en.wikipedia.org/wiki/Offline_reader
# Link farm: https://en.wikipedia.org/wiki/Link_farm
# Search engine scraping: https://en.wikipedia.org/wiki/Search_engine_scraping
# Web crawlers: https://en.wikipedia.org/wiki/Category:Web_crawlers


# Downloading DATA
def example4(links):

    # Save extracted data to a CSV file
    with open("scraped_data.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Link"])
        for link in links:
            writer.writerow([link["name"], link["url"]])


def example5(links):
    # Save data to a JSON file
    data = {"links": links}
    with open("scraped_data.json", "w") as json_file:
        json.dump(data, json_file, indent=4)
"""
Find By Vehicle 

https://www.copart.com/vehicleFinder/

"""

import time, json
from bs4 import BeautifulSoup
from pyvirtualdisplay import Display
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver



def get_random_headers():
    ua = UserAgent()
    headers = {
        'User-Agent': ua.random,
        'Accept-Language': 'en-US, en;q=0.5'
    }
    return headers

headers = get_random_headers()

print("\nMy Random Header is : \n", headers)
print("\n\n")

# for translation
prefs = {
  "translate_whitelists": {"ar":"en"},
  "translate":{"enabled":"true"}
}

# Set Chrome options
options = Options()
# options.headless = False
options.add_argument('--enable-logging')
options.add_argument('--log-level=0')
# options.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
options.add_argument(f'user-agent={headers["User-Agent"]}')
options.add_argument('--no-sandbox')
options.add_argument("chrome://settings/")
options.add_argument("--lang=en") 
options.add_argument("--disable-translate")
options.add_experimental_option("prefs", prefs)  # for translation
options.add_argument('--timeout=500') # for loading page



def vehicle_finder(driver : WebDriver):

    target_ul = driver.find_element(By.XPATH, "//ul[@class='nav nav-tabs borderNone']")
    all_li_tags= target_ul.find_elements(By.XPATH, ".//li[@class='ng-star-inserted']")
    all_find_by= {}
    for li in all_li_tags:
        time.sleep(2)
        a_tag= li.find_element(By.XPATH, ".//a[@class='nav-items']")
        find_by_title = a_tag.text.replace(" ", "_")
        print(find_by_title)
        a_tag.click()
        
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        
        target_span= soup.find('span', class_='list-group')
        all_child_spans= target_span.find_all('span', class_='ng-star-inserted')
        base_url= "https://www.copart.com/"
        category = {}
        for span in all_child_spans:
            a_tag= span.find('a')
            url= a_tag.get('href', None) if a_tag else None
            title= a_tag.get('title', None) if a_tag else None
            title= title.replace(" ", "") if title else None
            if url is not None and title is not None:
                category[title] = base_url+url
        
        all_find_by[find_by_title] = [category]
    
    data= {
        "vehicleFinder": [all_find_by]
    }
                
    print(json.dumps(data, indent=4))
    print("\n\n")

    return data





def sysInit():
    display = Display(visible=0, size=(800, 600))
    # display.start()
    # driver = None
    try:
        print(" *************** Starting CAR Scrapping *****************\n")
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        driver.maximize_window()
        # driver.get("https://www.copart.com/")

        # print("\n")
        # html = driver.page_source
        # time.sleep(5)
        # driver.execute_script("window.scrollBy(0, 200);")
        # html = driver.page_source
        # time.sleep(10)
        # driver.execute_script("window.scrollBy(0, 500);")
        # time.sleep(10)

        driver.get("https://www.copart.com/vehicleFinder/")

        time.sleep(20)
        driver.execute_script("window.scrollBy(0, 500);")
        html = driver.page_source

        time.sleep(1)
        data = vehicle_finder(driver= driver)

        for category in data["vehicleFinder"][0]:
            print(f"Category: {category}")
            category_urls = data["vehicleFinder"][0][category]

            # Loop through each URL in the category
            for url_name, url in category_urls[0].items():
                print(f"Opening URL: {url_name}")
                # Here you can perform actions to open the URL using Selenium or any other web automation tool
                # For demonstration purposes, we'll just print the URL
                print(f"URL: {url}")
            





    finally:
        print("QUIT WEB DRIVER ______________")
        # display.stop()
        if driver:
            driver.quit()


sysInit()







import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
from fake_useragent import UserAgent


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




def scrape_data_from_link(html):
    soup = BeautifulSoup(html, 'html.parser')
    data_dict = {}
    # Target the div with the specified id
    waypoint_div = soup.find('div', id='waypoint-trigger')
    # Extract key-value pairs from the specified ul element
    if waypoint_div:
        data_list_ul = waypoint_div.find('ul', class_='data-list--details')
        if data_list_ul:
            items = data_list_ul.find_all('li', class_='data-list__item')
            for item in items:
                label = item.find('span', class_='data-list__label').text.strip()
                value = item.find('span', class_='data-list__value').text.strip()
                data_dict[label] = value

    return [data_dict]

def scrape_iaai_website():

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.maximize_window()

    driver.get("https://www.iaai.com/Search?queryFilterValue=Automobiles&queryFilterGroup=InventoryTypes")

    time.sleep(40)
    # Scroll to the bottom of the page
    driver.execute_script("window.scrollBy(0, 2000);")

    time.sleep(10)  # Wait for content to load after scrolling

    html = driver.page_source

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find all anchor tags with 'href' attribute within the specified class
    container_elements = soup.find_all('div', class_='table-body border-l border-r')
    
    # Extract and save clean href values to a list with base URL
    base_url = "https://www.iaai.com/"
    links = []
    for container in container_elements:
        href_tags = container.find_all('a', href=True)
        for tag in href_tags:
            href_value = tag['href']
            # Check if the href starts with '/' to filter out unwanted links
            if href_value.startswith('/'):
                full_url = base_url + href_value
                links.append(full_url)

    # Open the browser and keep it open, scrape data for each link
    result_list = []
    for index, link in enumerate(links, start=1):
        print(f"************ Link no {index} is started link is {link}")
        driver.get(link)
        if index == 1:
            time.sleep(5)
            driver.execute_script("window.scrollBy(0, 200);")
            time.sleep(2)
            driver.execute_script("window.scrollBy(0, 500);")
            time.sleep(2)
            driver.execute_script("window.scrollBy(0, 1000);")
            time.sleep(2)
            driver.execute_script("window.scrollBy(0, 1500);")
            time.sleep(2)
            driver.execute_script("window.scrollBy(0, 200);")
            time.sleep(2)
        
        time.sleep(5)  # Adjust sleep time as needed
        html = driver.page_source
        print(html)

        data_list = scrape_data_from_link(html)
        single_json_result = json.dumps(data_list, indent=2)
        print(single_json_result)


        result_list.extend(data_list)

        if index == 20:
            break 


    # Convert the list of dictionaries to JSON
    json_result = json.dumps(result_list, indent=2)
    print("\n\n\n")
    print(json_result)


    driver.quit()

# Call the function to scrape data continuously
scrape_iaai_website()
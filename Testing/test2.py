from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time, json
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

options.add_argument('--timeout=50') # for loading page


# List of URLs to open
urls = [
    "https://www.iaai.com/VehicleDetail/39123681~US",
    "https://www.iaai.com/VehicleDetail/39119447~US",
]


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

    result_list = []
    for index, link in enumerate(urls, start=1):
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
        result_list.extend(data_list)


    # Convert the list of dictionaries to JSON
    json_result = json.dumps(result_list, indent=2)
    print("\n\n\n")
    print(json_result)

# Call the function to scrape data continuously
scrape_iaai_website()
"""
https://www.iaai.com/Vehicles-Auctions

"""


import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
from fake_useragent import UserAgent
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyvirtualdisplay import Display



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
options.add_argument('--enable-logging')
options.add_argument('--log-level=0')
options.add_argument(f'user-agent={headers["User-Agent"]}')
options.add_argument('--no-sandbox')
options.add_argument("chrome://settings/")
options.add_argument("--lang=en") 
options.add_argument("--disable-translate")
options.add_experimental_option("prefs", prefs)  # for translation
options.add_argument('--timeout=500') # for loading page





def scrape_data_from_link(html):
    soup = BeautifulSoup(html, 'html.parser')
    car_info_list = [] 
    tile_data_divs = soup.find_all('div', class_='tile--data')

    for tile_data_div in tile_data_divs:
        keys_values = {}
        label_span_elements = tile_data_div.select('span.data-list__label')
        for label_span in label_span_elements:
            key = label_span.get_text(strip=True).replace(' ', '').replace(':', '')  # Replace spaces with underscores
            key = key.replace('#', '')
            key = key.replace('/', '')
            key = "Keys" if key == 'Key' else key
            key = "VIN" if key == "VIN(Status)" else key
            value = label_span.find_next('span', class_='data-list__value').get_text(strip=True)
            keys_values[key] = value
        if keys_values:
                car_info_list.append(keys_values)  # Removed outer dictionary   
    
    if not car_info_list:
        return False

    return car_info_list




def save_in_db(payload):
    import requests
    import json

    url = "https://apiautomotor.devssh.xyz/vehicle-data"

    my_payload = json.dumps(payload)

    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=my_payload)
    print(response.text)
    print()
    resp = json.loads(response.text)    
    return resp['status']



def scraplinks(html):
    soup = BeautifulSoup(html, 'html.parser')
    container_element = soup.find('div', class_='table-body border-l border-r')
    all_cards_ele = container_element.find_all('div', class_='table-row table-row-border') if container_element else []
    base_url = "https://www.iaai.com/"
    links = []
    for card in all_cards_ele:
        title_ele = card.find('div', class_='table-cell table-cell--heading')
        h4 = title_ele.find('h4', class_='heading-7') if title_ele else ""
        a_tag = h4.find('a') if h4 else ""
        link = a_tag['href'] if a_tag and a_tag['href'] else None
        if link :
            full_url= base_url+link
            links.append(full_url)

    return links







def scrape_iaai_website():
    # display = Display(visible=0, size=(800, 600))
    # display.start()
    # driver = None
    try:
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        driver.maximize_window()
        driver.get("https://www.iaai.com/Search?queryFilterValue=Automobiles&queryFilterGroup=InventoryTypes")
        time.sleep(40)
        print("******** HTML ***********\n\n",driver.page_source)
        
        time.sleep(10)  
        driver.execute_script("window.scrollBy(0, 10000);")
        time.sleep(5)

        try:
            accept_cookies_btn = driver.find_element(By.XPATH, "//button[@id='onetrust-accept-btn-handler']")
            accept_cookies_btn.click()
            time.sleep(2)
        
        except Exception as e :
            print(e)
            pass

        html = driver.page_source

        alllinks = []
        links = scraplinks(html)
        alllinks.extend(links)
        
        # Click on Paginated pages
        count = 0
        while count < 3:
            try:
                driver.execute_script("window.scrollBy(0, 10000);")
                # Find the button element
                button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CLASS_NAME, "btn-next"))
                )
                button.click()
                time.sleep(10)
                html = driver.page_source
                links = scraplinks(html)
                alllinks.extend(links)
                count += 1
                print(f"Clicked {count} times.")
            except Exception as e:
                print("An error occurred:", e)
                break
        
        print(json.dumps(alllinks))
        # Open the browser and keep it open, scrape data for each link
        result_list = []
        count = 1

        folder_name = "iaai_scrapping"

        for index, link in enumerate(links, start=1):
            if link.startswith("https://www.iaai.com//SalesList"):
                continue
            try:
                with open(f"{folder_name}/iaai_all_previous_link_scrapped.json", "r") as file:
                    old_scrap_link = json.load(file)
                    print("\n\nPREVIOUS LINKS \n",json.dumps(old_scrap_link))

            except FileNotFoundError:
                old_scrap_link = []

            if link in old_scrap_link:
                continue

            print(f"** Link no {index} is started link is {link}")
            driver.get(link)
            if count == 1:
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
                count = count+1
            
            time.sleep(20)
            driver.execute_script("window.scrollBy(0, 500);")
            time.sleep(8)
            html = driver.page_source

            data_list = scrape_data_from_link(html)
            
            if data_list == False:
                print("**********************************  FALSE DATA NOT save in DB *************************** \n")
                continue

            image_urls = []
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')

            # for scrap title 
            title_ele = soup.find('div', class_='vehicle-header')
            h1_tag= title_ele.find('h1') if title_ele else ''
            vehicle_title = h1_tag.getText(strip= True) if h1_tag else ""

            # for scrap images 
            maindiv = soup.find_all("div", class_= "vehicle-image__thumb-container")
            maindiv = maindiv[0] if maindiv else None
            allimages = maindiv.find_all('img') if maindiv else []
            for img in allimages:
                src = img.get('src')
                if src:
                    if not src.startswith("https://vis.iaai.com/"):
                        continue
                    modified_params = src.replace("&width=161&height=120", "&width=845&height=633")
                    image_urls.append(modified_params)

            # Assign different names based on index
            dict_names = ['Vehicle_Details', 'Vehicle_Description', 'Bid_Information', 'Sale_Information']
            car_obj = {
                "Title":vehicle_title,
                "Vehicle_Website": "iaai",
                "Car_Images": image_urls,
                }  # Initialize "cars" as an empty list
            for i, data_dict in enumerate(data_list):
                if data_dict:  # Check if dictionary is not empty
                    car_obj[dict_names[i]] =  [data_dict]

            cars = {"cars": [car_obj]}
            single_json_result = json.dumps(cars, indent=2)
            print(single_json_result)

            old_scrap_link.append(link)
            # response = save_in_db(payload= cars)

            # if response == True:
            #     # Save the new link to the file
            #     with open(f"{folder_name}/iaai_all_previous_link_scrapped.json", "w") as file:
            #         json.dump(old_scrap_link, file, indent=2)

            #     print(f"Post {index} {link} is scrapped successfully\n\n")
    

    finally:
        print("QUIT WEB DRIVER ______________")
        print("******** HTML AFTER Exception ***********\n\n",driver.page_source)
        # display.stop()
        if driver:
            driver.quit()




    driver.quit()

# Call the function to scrape data continuously
scrape_iaai_website()
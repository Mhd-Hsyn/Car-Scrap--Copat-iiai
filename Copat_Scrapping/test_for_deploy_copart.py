"""
Testing script       CAR Scrap

https://www.copart.com/saleListResult/93/2024-02-02?location=AZ%20-%20Tucson&saleDate=1706900400000&liveAuction=false&from=&yardNum=93


-----------------------------------

https://www.copart.com/vehicle-search-type/automobiles?displayStr=Automobiles&from=%2FvehicleFinder
3000 data 
-----------------------------------



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



def scrap_links(html):
    all_links = []
    soup = BeautifulSoup(html, 'html.parser')
    main_table = soup.find('table', {'class': 'p-datatable-table'})
    tbody = main_table.find("tbody", class_= "p-datatable-tbody") if main_table else None
    all_rows = tbody.find_all('tr', {'class': 'p-element p-selectable-row ng-star-inserted'}) if tbody else []

    for row in all_rows:
        td_link_ele = row.find('a')
        link = td_link_ele['href'] if td_link_ele else None
        base_url = "https://www.copart.com"
        link = base_url+ link.replace(".","")
        all_links.append(link)

    return all_links




def scrap_data(html):
    data = {
        "Title": "",
        "Vehicle_Website": "coopart",
        "Car_Images": [],
        "Vehicle_Details": [],
        "Bid_Information" : [],
        "Sale_Information": []
    }
    soup = BeautifulSoup(html, "html.parser")
    
    heading_ele = soup.find('div', class_="title-and-highlights")
    heading_h1 = heading_ele.find('h1') if heading_ele else ""
    data['Title']= heading_h1.text.strip() if heading_h1 else ""

    # for Vehicle Details
    vehicle_details = {}
    # Iterate over each label and corresponding value
    for label_elem in soup.select('div.f-g2 label'):
        label = label_elem.text.strip()
        label = label.replace(":", "")
        label = label.replace(" ", "")

        # Find the corresponding value
        value_elem = label_elem.find_next(class_='lot-details-desc')
        value = value_elem.text.strip() if value_elem else None
        value = value.replace("\n", "").replace("  ", "")

        # Add the key-value pair to the details dictionary
        vehicle_details[label] = value
    
    data["Vehicle_Details"] = [vehicle_details]


    # For Bid Information 
    bid_details = {}
    # Extract Sale Status
    bid_div_main = soup.find('div', class_="bid-info-content")
    all_bid_divs = bid_div_main.find_all('div', class_="border-top-gray") if bid_div_main else []
    for bid_div in all_bid_divs:
        label_elem = bid_div.find("label")
        label = label_elem.get_text(strip=True) if label_elem else ""
        label = label.replace(":", "")
        span_ele = bid_div.find("span")
        span = span_ele.get_text(strip = True) if span_ele else ""
        span = span.replace("Add to Calendar", "")
        if label == "Eligibility Status" or label == "Your Bid":
            continue
        label = label.replace(" ", "")
        bid_details [label] = span

    data["Bid_Information"] = [bid_details]

    # for Sale Information
    sale_info_div = soup.find('div', {'id': 'sale-information-block'})
    sales_details = {}
    # Extract key-value pairs dynamically
    info_pairs = sale_info_div.find_all('div', class_='d-flex') if sale_info_div else ""
    for pair in info_pairs:
        label = pair.find('label').get_text(strip=True)
        label = label.replace(" ", "")
        label = label.replace(":", "")
        value = pair.find('span').get_text(strip=True)
        sales_details[label]= value

    data['Sale_Information'] = [sales_details]

    # Extract image URLs
    image_urls = []

    thumb_img_blocks = soup.find_all('span', class_='thumbImgblock')
    for thumb_img_block in thumb_img_blocks:
        img_url = thumb_img_block.find('img', class_='thumbnailImg')['ng-src']
        # Replace the ng-src attribute with the actual image URL
        img_url = img_url.replace('{{$index}}', '0')
        img_url = img_url.replace("thb", "ful")
        image_urls.append(img_url)

    if not image_urls :
        print("FALSE DATA")
        print(data)
        return False
    
    data["Car_Images"] = image_urls
    
    return data




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






def sysInit():
    display = Display(visible=0, size=(800, 600))
    display.start()
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

        driver.get("https://www.copart.com/vehicle-search-featured/select?displayStr=Copart%20Select&from=%2FvehicleFinder")
        time.sleep(25)
        driver.execute_script("window.scrollBy(0, 8000);")
        html = driver.page_source
        alllinks = []
        time.sleep(5)


        try:
            # Locate the main p-dropdown using the styleclass
            dropdown = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'p-paginator-rpp-options')))

            # Click on the dropdown trigger
            dropdown_trigger = dropdown.find_element(By.CLASS_NAME, 'p-dropdown-trigger')
            dropdown_trigger.click()
            time.sleep(5)

            # Wait for the dropdown options to appear
            dropdown_options = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'p-dropdown-items-wrapper'))
            )

            # Locate and click on the option with text "100"
            option_100 = dropdown_options.find_element(By.XPATH, "//li[@aria-label='100']")
            option_100.click()
            time.sleep(5)
            print("Selected '100' from the dropdown.")

        except Exception as e:
            print(f"An error occurred: {e}")

        except Exception as e:
            print(f"Error: {e}")
        
        time.sleep(15)
        driver.execute_script("window.scrollBy(1000, 19000);")
        time.sleep(5)
        
        # count = 1
        try:
            while True:
                # driver.execute_script("window.scrollBy(0, 1200);")
                time.sleep(3)
                html = driver.page_source
                links = scrap_links(html)
                alllinks.extend(links)
                time.sleep(10)
                button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'p-paginator-next')))
                # Check if the button is disabled
                if "p-disabled" in button.get_attribute("class"):
                    print("Button is disabled. Exiting loop.")
                    break
                # Click the button
                button.click()
                print("Click")
                time.sleep(10)
                
                # count += 1
                # if count == 2:
                #     break

        except ElementClickInterceptedException:
            print("ElementClickInterceptedException: Button is not clickable at the moment.")
        except NoSuchElementException:
            print("NoSuchElementException: Unable to locate the button.")


        print(json.dumps(alllinks))

        print(f"\n*********** All links are {len(alllinks)} ********** \n")

        count = 1
        for index, link in enumerate(alllinks, start= 1):
            try:
                with open("all_previous_link_scrapped.json", "r") as file:
                    old_scrap_link = json.load(file)
            except FileNotFoundError:
                old_scrap_link = []

            if link in old_scrap_link:
                continue

            print(f"Post {index} is scrapping")
            print(f"Link {link} is scrapping")

            driver.get(url = str(link))

            if count == 1:
                time.sleep(10)
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
                count = 100
                
            time.sleep(20)
            driver.execute_script("window.scrollBy(0, 500);")
            time.sleep(8)
            html = driver.page_source
            
            data = scrap_data(html)

            if data == False:
                print("**********************************  FALSE DATA NOT save in DB *************************** \n")
                continue

            final_data = {"cars" : [data]} 
            print(json.dumps(final_data, indent=2))
            time.sleep(4)
            old_scrap_link.append(link)
            # response = save_in_db(payload= final_data)

            # if response == True:
            #     # Save the new link to the file
            #     with open("all_previous_link_scrapped.json", "w") as file:
            #         json.dump(old_scrap_link, file, indent=2)

            #     print(f"Post {index} {link} is scrapped successfully\n\n")

            
    finally:
        print("QUIT WEB DRIVER ______________")
        display.stop()
        if driver:
            driver.quit()


sysInit()







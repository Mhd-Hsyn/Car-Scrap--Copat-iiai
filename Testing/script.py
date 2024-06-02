"""
Testing script       CAR Scrap

https://www.copart.com/


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
    main_span = soup.find('span', {'class': 'recommendation-blocks'})
    all_sub_spans = main_span.find_all('span', {'class': 'items items-box-shadow lot-card'}) if main_span else ''
    
    if all_sub_spans:
        for span in all_sub_spans:
            link_ele = span.find('a', {'class': 'borderNone f-1'})
            link = link_ele['href'] if link_ele else None
            base_url = "https://www.copart.com"
            link = base_url+ link.replace(".","")
            all_links.append(link)

    # print("\n\n", json.dumps(all_links))

    return all_links




def scrap_data(html):
    data = {
        "Car_Images": [],
        "Vehicle_Details": [],
        "Bid_Information" : [],
        "Sale_Information": []
    }
    soup = BeautifulSoup(html, "html.parser")
    
    # for Vehicle Details
    vehicle_details = {}
    # Iterate over each label and corresponding value
    for label_elem in soup.select('div.f-g2 label'):
        label = label_elem.text.strip()
        label = label.replace(":", "")
        label = label.replace(" ", "_")

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
        label = label.replace(" ", "_")
        bid_details [label] = span

    data["Bid_Information"] = [bid_details]

    # for Sale Information
    sale_info_div = soup.find('div', {'id': 'sale-information-block'})
    sales_details = {}
    # Extract key-value pairs dynamically
    info_pairs = sale_info_div.find_all('div', class_='d-flex') if sale_info_div else ""
    for pair in info_pairs:
        label = pair.find('label').get_text(strip=True)
        label = label.replace(" ", "_")
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

    data["Car_Images"] = image_urls

    return data





def sysInit():
    display = Display(visible=0, size=(800, 600))
    # display.start()
    driver = None
    try:
        print(" *************** Starting Script Hala-Canada Post Scrapping *****************\n")
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        driver.maximize_window()
        driver.get("https://www.copart.com/")

        print("\n")
        html = driver.page_source
        time.sleep(10)
        driver.execute_script("window.scrollBy(0, 200);")
        html = driver.page_source
        time.sleep(10)
        driver.execute_script("window.scrollBy(0, 500);")
        # time.sleep(10)

        html = driver.page_source
        alllinks = []
        links = scrap_links(html)
        alllinks.extend(links)

        
        while True:
            try:
                # Wait for the button to be clickable
                button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'ar-right-active')))
                
                # Click the button
                button.click()

                # You may want to add some waiting time to give the page time to update
                time.sleep(2)
                html = driver.page_source
                links = scrap_links(html)
                alllinks.extend(links)

            except Exception as e:
                # This exception will be triggered if the button becomes inactive
                print("Button is inactive. Stopping the loop.")
                break

        print(alllinks)
        final_data = {"cars" : []} 
        all_posts = []
        
        print(f"\n*********** All links are {len(alllinks)} ********** \n")

        for index, link in enumerate(alllinks) :
            print(f"Post {index+1} is scrapping")
            print(f"Link {link} is scrapping")


            driver.get(url = str(link))
            time.sleep(3)
            driver.execute_script("window.scrollBy(0, 500);")
            time.sleep(3)
            html = driver.page_source
            
            data = scrap_data(html)
            all_posts.append(data)
            time.sleep(4)
        
        final_data["cars"] = all_posts

        json_filename = 'all_cars_data.json'
        with open(json_filename, 'w', encoding='utf-8') as json_file:
            json.dump(final_data, json_file, ensure_ascii=False, indent=4)

    finally:
        print("QUIT WEB DRIVER ______________")
        # display.stop()
        if driver:
            driver.quit()


sysInit()
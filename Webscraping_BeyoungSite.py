#Project completed on 04-08-2023

import time

from selenium.common import NoSuchElementException as b
from selenium.webdriver import ActionChains, Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions() #To fix auto close issue (https://www.youtube.com/watch?v=ijT2sLVdnPM)
options.add_experimental_option("detach", True)
service_obj = Service("/Users/vinti/chromedriver")
driver = webdriver.Chrome(options=options,service=service_obj)
driver.get("https://www.beyoung.in/")
driver.maximize_window()


actions = ActionChains(driver)
Men = driver.find_element(By.LINK_TEXT, "MEN")
actions.move_to_element(Men).perform()
Printed_TShirts = driver.find_element(By.LINK_TEXT, "Printed T-Shirts")
actions.move_to_element(Printed_TShirts).click().perform()
time.sleep(3)

image= []
img = []
name = []
na = []
rate = []
status = []


try:
    time.sleep(2)  # Allow 2 seconds for the web page to open
    scroll_pause_time = 1  # You can set your own pause time. My laptop is a bit slow so I use 1 sec
    screen_height = driver.execute_script("return window.screen.height;")  # get the screen height of the web
    i = 1

    while True:
        # scroll one screen height each time
        driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
        i += 1
        time.sleep(scroll_pause_time)
        # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
        scroll_height = driver.execute_script("return document.body.scrollHeight;")
        # Break the loop when the height we need to scroll to is larger than the total scroll height
        if (screen_height) * i > scroll_height:
            break
        img_url = driver.find_elements(By.XPATH, "//a/img[@class = 'normalimg lazyload fade'] | //a/img[@class = 'lazyload fade']")
        image.extend(img_url)
    Name = driver.find_elements(By.XPATH, "//div[@class = 'products']/a/div/h2")
    Rate = driver.find_elements(By.XPATH,"//div[@class = 'price']/strong")

    imexc1 = "https://www.beyoung.in/api/catalog/footer/11Play-Store-footer.png"
    imexc2 = "https://www.beyoung.in/api/catalog/footer/12App-Store-footer.png"

    for i in image:
        out = i.get_attribute('src')
        if out not in img and (out != imexc1 and out != imexc2):
            print(out)
            img.append(out)
    print(len(img))

    exc1 = "Pick Your Favorite Mens T Shirts Online from 400+ Latest Designs"
    exc2 = "Buy T Shirts For Men at Best Price"
    exc3 = "Buy Best T Shirts For Men Online India at Beyoung"
    exc4 = "Mens T Shirts Online"

    for j in Name:
        out = j.text
        print(out)
        na.append(out)
    print(len(na))

    for k in Rate:
        out = k.text
        print(out)
        rate.append(out)
    print(len(rate))


    cnt = 1
    while cnt <= len(rate):
        cnt = str(cnt)
        filtr = ("//*[@id='__next']/section[3]/div/div[2]/div[2]/div[" + cnt + "]/div[@class = 'out-of-stock']/label")
        try:
            res1 = driver.find_element(By.XPATH, "//*[@id='__next']/section[3]/div/div[2]/div[2]/div[" + cnt + "]/div[@class = 'out-of-stock']/label")
            status.append(res1.text)
        except b:
            status.append("None")
        cnt = int(cnt)
        cnt += 1
        print(status[-1])

    print(len(status))

except Exception as e:
        print("The error is: ", e)

#To export the scraped data to excel format.
import pandas as pd

df = pd.DataFrame(zip(na,rate,status,img), columns=["T-Shirt_Names","Price","Status", "T-Shirt_Model"])
df.to_excel(r"F:\T-Shirt_Trend_Beyoung2.xlsx",index=False)

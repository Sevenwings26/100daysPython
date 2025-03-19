# from selenium import webdriver

# ## keep Chrome browser open after program finishes
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)

# driver = webdriver.Chrome()
# driver.get("https://www.amazon.com")



# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# # from bs4 import BeautifulSoup
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait

# from selenium.webdriver.support import expected_conditions as EC
# # import numpy as np
# # import pandas as pd

# DRIVER_PATH = "C:/Users/user/chromedriver-win64/chromedriver.exe"
# service = Service(DRIVER_PATH)
# driver = webdriver.Chrome(service=service)

# driver.get("https://www.amazon.co.uk")

# # taget a class
# price_pounds = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")

# print(f"THe whole price is {price_pounds.text}.{price_cents.text}")


# try:
#     webDriverWait(driver, 40).until(
# #         EC.presence_of_element_located((By.CLASS_NAME, '_276e7_3vaQt c8aa3_3j3oz'))
#         EC.presence_of_element_located((By.CLASS_NAME, '_050ef_K0hT7 e87b8_2Qi4v'))
#     )
# except:
#     print("No elements found")
    
# html_source = driver.page_source

# driver.close()
# driver.quit()


# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By

# DRIVER_PATH = "C:/Users/user/chromedriver-win64/chromedriver.exe"
# service = Service(DRIVER_PATH)

# # Set up Chrome options
# options = Options()
# options.add_argument("start-maximized")
# options.add_argument("disable-infobars")
# options.add_argument("--disable-blink-features=AutomationControlled")  # Avoid detection
# options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36")

# driver = webdriver.Chrome(service=service, options=options)
# driver.get("https://www.amazon.co.uk")

# try:
#     price_pounds = driver.find_element(By.CLASS_NAME, value="a-price-whole")
#     price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
#     print(f"The whole price is {price_pounds.text}.{price_cents.text}")
# except Exception as e:
#     print("Element not found:", e)

# driver.quit()

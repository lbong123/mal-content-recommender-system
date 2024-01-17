"""
This script will be dedicated to scraping 

"""
import requests
import time
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def main():
    # Set up Selenium options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode (without GUI)

    # Create a WebDriver instance
    driver = webdriver.Chrome()

    URL = f"https://myanimelist.net/animelist/lbong123?status=2"
    driver.get(URL)

    time.sleep(5)

    soup = BeautifulSoup(driver.page_source, "html.parser")

    listItems = soup.find_all("tbody", class_="list-item")

    for item in listItems:
        name = item.find("td", "data title clearfix").find("a", class_="link sort").text
        score = item.find("td", class_="data score").text

        print(name, score)


if __name__ == "__main__":
    main()
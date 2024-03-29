"""
This script will be dedicated to scraping members from various anime user lists using beautiful soup.
The scraped output will be saved into a CSV file called userList.txt.

"""
import requests
import time
from bs4 import BeautifulSoup

NUM_USERS = 60000

def main():
    with open("userList.txt", 'a', encoding="utf-8") as userList:
        pageNum = 75
        while pageNum < NUM_USERS:
            URL = f"https://myanimelist.net/anime/18897/Nisekoi/stats?m=all&show={pageNum}#members"
            page = requests.get(URL)

            if (page.status_code == 429):
                print("too many requests")
                break
            soup = BeautifulSoup(page.content, "html.parser")

            job_elements = soup.find_all("a", class_="word-break")
            for job_element in job_elements:
                text = job_element.text
                userList.write(f"{text}\n")
                print("wrote")

            pageNum += 75
            time.sleep(4)

if __name__ == "__main__":
    main()
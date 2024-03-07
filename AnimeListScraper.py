import requests
import time
from bs4 import BeautifulSoup
import csv

def main():
    with open("animeList.csv", 'w', newline='', encoding="utf-8") as file:
        pageNum = 0
        titles = []
        urls = []
        prev = None
        curr = 0

        try:
            while curr != prev:
                URL = f"https://myanimelist.net/topanime.php?limit={pageNum}"
                page = requests.get(URL)

                soup = BeautifulSoup(page.content, "html.parser")

                if (page.status_code == 429):
                    print("too many requests")

                animeList = soup.find_all("tr", class_="ranking-list")
                
                for anime in animeList:
                    element = anime.find("h3", class_="fl-l fs14 fw-b anime_ranking_h3")
                    title = element.text
                    url = element.find("a").get("href")
                    titles.append(title)
                    urls.append(url)

                print(len(titles))
                prev = curr
                curr = len(titles)
                pageNum += 50

                time.sleep(3)
            
            writer = csv.writer(file)
            writer.writerow(titles)
            writer.writerow(urls)
        except:
            writer = csv.writer(file)
            writer.writerow(titles)
            writer.writerow(urls)

        
if __name__ == "__main__":
    main()
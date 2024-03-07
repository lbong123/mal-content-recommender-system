"""
This script will be dedicated to scraping members from various anime user lists using beautiful soup.
The scraped output will be saved into a CSV file called userList.txt.

"""
import requests
import csv

def main():
    client_id = "9d5592d98582b78c2ccd1c47b4517aca"
    user_name = "lbong123"

    headers = {
    'X-MAL-CLIENT-ID': client_id,
    'Content-Type': 'application/json',
    }

    # read list of animes
    with open("animeList.csv", 'r', encoding="utf-8") as animeList:
        reader = csv.reader(animeList)
        animes = list(reader)[0]

    try:
        with open("uniqueUserList.txt", 'r', encoding="utf-8") as userList:
            with open("animeScores.csv", 'a', encoding="utf-8") as animeScores:
                writer = csv.writer(animeScores)
                for user in userList.readlines():
                    user = user.strip("\n")

                    response = requests.get(f'https://api.myanimelist.net/v0/users/{user}/animelist?limit=1000&fields=list_status', headers=headers)

                    # turn animes seen by user into a dictionary
                    scores = {}
                    for animeData in response.json()['data']:
                        title = animeData["node"]["title"]
                        score = animeData["list_status"]["score"]
                        scores[title] = score

                    scoreList = [0] * len(animes)
                    for i, anime in enumerate(animes):
                        scoreList[i] = scores.get(anime, 0)
                    
                    print(user)
                    writer.writerow(scoreList)

    except:
        print("failed")
        print(user)
    




if __name__ == "__main__":
    main()
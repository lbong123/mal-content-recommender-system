import requests

def main():
    response = requests.get("https://api.jikan.moe/v4/users")

    if response.status_code == 200:
        userList = response.json()
        for userDict in userList["data"]:
            print(userDict["username"])

if __name__ == "__main__":
    main()
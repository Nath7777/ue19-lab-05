import requests

def blagues():
    url = "https://blague-api.vercel.app/api?mode=dev"
    reponse = requests.get(url)

    if reponse.status_code == 200:
        data = reponse.json()
        blague = data["blague"]
        reponse = data["reponse"]

        print(blague)
        print(reponse)
    else:
        print("Erreur status_code")


if __name__ == "__main__":
    blagues()
from urllib import response
from requests import get

LOL_KEY = "?api_key=RGAPI-ccb73e02-e79a-4064-aabf-a2496c779776"
LOL_URL = "https://br1.api.riotgames.com"
LOL_NAME = input("Digite o nome de Invocador: ")


def get_links():
    response = get(LOL_URL+"/lol/summoner/v4/summoners/by-name/" +
                   LOL_NAME+LOL_KEY).json()
    return response


def ranked():
    lol_id = get_links()["id"]
    response = get(
        LOL_URL+"/lol/league/v4/entries/by-summoner/"+lol_id+LOL_KEY).json()
    return response


print(ranked())

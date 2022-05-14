from requests import get

LOL_KEY = "?api_key=RGAPI-89613424-0bda-4b09-9d27-faf8b9b040a0"
LOL_URL = "https://br1.api.riotgames.com"
LOL_CHAMPS = "/lol/summoner/v4/summoners/{encryptedSummonerId}"

summonerName = input('Digite o nome de Invocador: ')


def get_links():
    response = get(LOL_URL+LOL_CHAMPS+LOL_KEY).json()
    return response


print(get_links())

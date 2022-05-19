from requests import get

KEY = "RGAPI-35da394b-0416-483f-8213-2c548945d5f5"
LOL_KEY = "?api_key=" + KEY
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


for lol in ranked():
    elo = lol['tier']
    rankeada = lol['queueType']
    tier = lol['rank']
    pontos = lol['leaguePoints']
    vit = lol['wins']
    derrotas = lol['losses']
    txvit = vit*100/(vit+derrotas)


print("Tipo de rankeada: {}, Rank: {}, Tier: {}, Pontos: {}, \n Vitorias: {}, Derrotas: {}, Porgentagem de vitoria: {:.2f}%.".format(
    rankeada, elo, tier, pontos, vit, derrotas, txvit))

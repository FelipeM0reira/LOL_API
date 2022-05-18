from requests import get

KEY = "RGAPI-a0b4f9c2-ce38-4a19-9471-e6727dce4197"
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


for rank in ranked():
    elo = rank["tier"]
    rankeada = rank["queueType"]
    tier = rank["rank"]
    pontos = rank["leaguePoints"]
    vit = rank["wins"]
    derrotas = rank["losses"]
    txvit = vit*100/(vit+derrotas)


print("Tipo de rankeada: {}, Rank: {}, Tier: {}, Pontos: {}, Vitorias: {}, Derrotas: {}, Porgentagem de vitoria: {}%.".format(
    rankeada, elo, tier, pontos, vit, derrotas, txvit))

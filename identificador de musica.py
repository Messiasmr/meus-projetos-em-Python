import requests
import json

API_KEY = "sua_chave_de_api"  # Substitua pela sua chave de API

def identificar_musica(caminho_arquivo):
    url = "https://api.audd.io/"
    data = {
        'api_token': API_KEY,
        'return': 'timecode,apple_music,spotify',
    }
    files = {
        'file': open(caminho_arquivo, 'rb'),
    }
    response = requests.post(url, data=data, files=files)
    resultado = response.json()
    return resultado

if __name__ == "__main__":
    caminho_arquivo = 'caminho/para/seu/arquivo.mp3'  # Substitua pelo caminho do seu arquivo
    resultado = identificar_musica(caminho_arquivo)
    print(json.dumps(resultado, indent=4))

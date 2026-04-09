import os
import requests
from dotenv import load_dotenv

load_dotenv()

def clima(cidade: str):

    chave_api = os.getenv("OPENWEATHER_API_KEY")
    if not chave_api:
        print("Erro: chave da API não encontrada. Verifique o arquivo .env")
        return None

    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave_api}&units=metric&lang=pt_br"

    try:
        resposta = requests.get(url, timeout=10)
        resposta.raise_for_status()
        dados = resposta.json()

        if "main" in dados and "weather" in dados:
            temperatura = dados["main"]["temp"]
            descricao = dados["weather"][0]["description"]
            return temperatura, descricao
        else:
            print("Resposta inesperada da API:", dados)
            return None
    except requests.exceptions.RequestException as e:
        print("Erro de conexão com a API:", e)
        return None

if __name__ == "__main__":
    resultado = clima("Toledo")
    if resultado is not None:
        temp, desc = resultado
        print(f"Temperatura em Toledo: {temp}°C - {desc}")
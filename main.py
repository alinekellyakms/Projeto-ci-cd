import os
import requests
from dotenv import load_dotenv

load_dotenv()  # carrega variáveis do arquivo .env

def clima(cidade):
    chave_api = os.getenv("OPENWEATHER_API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave_api}&units=metric&lang=pt_br"
    resposta = requests.get(url)
    dados = resposta.json()
    if "main" in dados:
        return dados['main']['temp']
    else:
        print("Erro na resposta da API:", dados)
        return None

if __name__ == "__main__":
    resultado = clima("Toledo")
    if resultado is not None:
        temp, desc = resultado
        print(f"Temperatura em Toledo: {temp}°C - {desc}")



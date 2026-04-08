# Projeto CI/CD - Clima com OpenWeatherMap

Este projeto é um exemplo de integração contínua (CI) e entrega contínua (CD) usando **GitHub Actions**.  
Ele consulta a API do [OpenWeatherMap](https://openweathermap.org/) para obter a temperatura atual de uma cidade e 
valida o funcionamento com testes automatizados.


## Funcionalidades
- Consulta a temperatura atual de uma cidade usando a API do OpenWeatherMap.
- Uso de variáveis de ambiente para proteger a chave da API.
- Testes automatizados com **pytest**.
- Pipeline de CI/CD configurado com **GitHub Actions**.

## Tecnologias utilizadas
- Python 3.12
- Requests
- Pytest
- GitHub Actions
- python-dotenv (para carregar variáveis do `.env`)

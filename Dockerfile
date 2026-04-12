# Imagem base oficial do Python
FROM python:3.12-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia todos os arquivos do projeto para dentro do container
COPY . /app

# Instala as dependências listadas no requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Define a variável de ambiente (placeholder)
# A chave real será passada na hora de rodar o container
ENV OPENWEATHER_API_KEY=${OPENWEATHER_API_KEY}

# Comando padrão para rodar sua aplicação
CMD ["python", "main.py"]
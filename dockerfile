
# Use a imagem base do Python
FROM python:3.8

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .
COPY run.sh .
# Instale as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt
RUN chmod +x run.sh
# Copie o restante do código-fonte para o diretório de trabalho
COPY . .

# Exponha a porta em que o aplicativo estará em execução
EXPOSE 8000 8080

# Inicie o aplicativo usando o comando uvicorn
CMD ["./run.sh","&&","uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]

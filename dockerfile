
# Use a imagem base do Python
FROM python:3.8

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instale as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

RUN python3 -m fastchat.serve.controller
RUN python3 -m fastchat.serve.model_worker --model-path lmsys/fastchat-t5-3b-v1.0
RUN python3 -m fastchat.serve.openai_api_server --host localhost --port 8000
# Copie o restante do código-fonte para o diretório de trabalho
COPY . .

# Exponha a porta em que o aplicativo estará em execução
EXPOSE 8000 8080

# Inicie o aplicativo usando o comando uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]

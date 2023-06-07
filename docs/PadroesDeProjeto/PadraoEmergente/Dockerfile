# Imagem base do Python
FROM python:3.8

# Definir variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Diretório de trabalho
WORKDIR /code

# Instalar as dependências do projeto
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Copiar o código-fonte do projeto
COPY . /code/

# Configurações do PostgreSQL
ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD postgres
ENV POSTGRES_DB mydb
ENV POSTGRES_HOST db
ENV POSTGRES_PORT 5432

# Instalar o PostgreSQL
RUN apt-get update \
    && apt-get install -y postgresql-client

# Expor a porta 8000
EXPOSE 8000

# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3-slim

# Définit le répertoire de travail dans le conteneur
WORKDIR /app

# Copie tous les fichiers du répertoire courant dans le répertoire de travail du conteneur
COPY . /app

# Installe les dépendances du projet (celles listées dans requirements.txt)
RUN pip install -r requirements.txt

# Lance l'application Streamlit
CMD ["streamlit", "run", "app.py"]
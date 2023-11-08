FROM python:3.9

# Copier le contenu actuel du répertoire local dans le conteneur
COPY . /app

# Définir le répertoire de travail
WORKDIR /app

# Installer les dépendances de l'application Flask (ajoutez d'autres dépendances si nécessaires)
RUN pip install flask mysql-connector-python

# Exposer le port sur lequel l'application Flask s'exécute
EXPOSE 5000

# Commande pour exécuter l'application Flask
CMD ["python", "app.py"]

```markdown
# Détection de Tweet Suspect

## Description du projet

Ce projet vise à détecter des tweets suspects ou malveillants en utilisant des techniques d'apprentissage automatique. L'objectif est de classer les tweets en catégories : **suspect** ou **non suspect**, en utilisant des modèles de classification. Nous allons appliquer une série d'étapes, incluant l'exploration des données, le prétraitement du texte, l'entraînement de modèles et le déploiement d'une solution pratique.

### Objectifs :
- Appliquer des techniques d'apprentissage automatique pour la détection de discours suspect.
- Construire un modèle de classification robuste.
- Déployer un modèle pour une utilisation pratique via une interface Streamlit ou une API.

---

## Structure du répertoire

```
Tweet_Suspect_Detection/
│
├── data/
│   ├── raw_data.csv          # Données brutes (tweets non traités)
│   ├── processed_data.csv    # Données après prétraitement (tweets nettoyés)
│
├── notebooks/
│   ├── 1_data_exploration.ipynb   # Notebook pour l'analyse exploratoire des données
│   ├── 2_data_preprocessing.ipynb # Notebook pour le nettoyage et le prétraitement des données
│   ├── 3_model_training.ipynb     # Notebook pour l'entraînement des modèles
│   └── 4_model_evaluation.ipynb   # Notebook pour l'évaluation et la validation des modèles
│
├── src/
│   ├── __init__.py            # Fichier d'initialisation du package
│   ├── data_preprocessing.py   # Script pour le prétraitement des données
│   ├── feature_engineering.py  # Script pour la vectorisation et l'extraction des caractéristiques
│   ├── model_training.py      # Script pour l'entraînement des modèles
│   ├── model_evaluation.py    # Script pour l'évaluation et l'ajustement des modèles
│   └── utils.py               # Script utilitaire (fonction de nettoyage, gestion des paramètres, etc.)
│
├── requirements.txt           # Liste des dépendances Python du projet
├── app.py                     # Application Streamlit pour l'interface utilisateur
├── deploy_model.py            # Script pour déployer le modèle en production
├── README.md                  # Fichier de documentation du projet
└── config.yaml                # Fichier de configuration (par exemple, pour les hyperparamètres)
```

---

## Prérequis

Avant d'exécuter le projet, vous devez avoir installé Python et les bibliothèques suivantes. Vous pouvez installer les dépendances en utilisant le fichier `requirements.txt` :

### Installation des dépendances

1. Clonez le dépôt sur votre machine locale :
   ```bash
   git clone https://github.com/votre-utilisateur/Tweet_Suspect_Detection.git
   cd Tweet_Suspect_Detection
   ```

2. Créez un environnement virtuel (recommandé) :
   ```bash
   python -m venv venv
   source venv/bin/activate   # Sous Linux/MacOS
   venv\Scripts\activate      # Sous Windows
   ```

3. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

---

## Étapes du projet

Le projet est divisé en plusieurs étapes :

### 1. Exploration des données
- **But :** Analyser les données, comprendre leur structure et leur distribution.
- **Outils :** Pandas, Matplotlib, Seaborn
- **Notebook associé :** `1_data_exploration.ipynb`

### 2. Prétraitement des données
- **But :** Nettoyer les tweets, supprimer les caractères spéciaux, convertir le texte en minuscules, et vectoriser le texte.
- **Outils :** NLTK, Scikit-learn (TF-IDF)
- **Notebook associé :** `2_data_preprocessing.ipynb`

### 3. Construction et entraînement des modèles
- **But :** Tester différents modèles de classification (Régression logistique, Forêts aléatoires, SVM, etc.).
- **Outils :** Scikit-learn, TensorFlow/Keras
- **Notebook associé :** `3_model_training.ipynb`

### 4. Évaluation des modèles
- **But :** Mesurer les performances des modèles avec des métriques appropriées (précision, rappel, F-mesure, courbes ROC).
- **Outils :** Scikit-learn, Seaborn
- **Notebook associé :** `4_model_evaluation.ipynb`

### 5. Déploiement du modèle
- **But :** Déployer le modèle via une interface utilisateur (Streamlit) ou créer une API avec Flask/FastAPI.
- **Outils :** Streamlit, FastAPI, Flask
- **Fichiers associés :** `app.py` (Streamlit), `deploy_model.py` (API)

---

## Utilisation

### 1. Environnement d'exécution
Pour exécuter l'application Streamlit (interface utilisateur), assurez-vous d'avoir activé votre environnement virtuel et exécutez la commande suivante :

```bash
streamlit run app.py
```

Cela ouvrira une page Web où vous pourrez entrer un tweet et obtenir une prédiction (suspect ou non suspect).

### 2. Déploiement en API
Si vous préférez interagir avec l'API, vous pouvez utiliser **FastAPI** ou **Flask** :

```bash
python deploy_model.py
```

Cela démarrera l'API qui pourra être utilisée pour envoyer des requêtes de classification à votre modèle.

---

## Références

- [Scikit-learn Documentation](https://scikit-learn.org/stable/documentation.html)
- [Streamlit Documentation](https://streamlit.io/docs)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [NLTK Documentation](https://www.nltk.org/)

---

## Auteurs

- **Benewenwende Pierre BONKOUNGOU** (Développeur principal)
  - [B6WP2](https://github.com/VirtuelsDev/Tweet_Suspect_Detection.git)

---

## Licence

Ce projet est sous Open source - voir le fichier [LICENSE](LICENSE) pour plus de détails.

---
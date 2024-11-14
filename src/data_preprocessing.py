# src/data_preprocessing.py

import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Téléchargement des ressources NLTK nécessaires
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')


def clean_text(text):
    """
    Nettoyer le texte en supprimant les URLs, mentions, hashtags, ponctuations, chiffres,
    et en le convertissant en minuscules.
    
    Parameters:
    text (str): Le texte à nettoyer.
    
    Returns:
    str: Le texte nettoyé.
    """
    # Supprimer les URLs
    text = re.sub(r'http\S+', '', text)
    
    # Supprimer les mentions (@username)
    text = re.sub(r'@\w+', '', text)
    
    # Supprimer les hashtags (#hashtag)
    text = re.sub(r'#\w+', '', text)
    
    # Supprimer la ponctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Supprimer les chiffres
    text = re.sub(r'\d+', '', text)
    
    # Convertir en minuscules
    text = text.lower()
    
    return text


def tokenize_text(text):
    """
    Tokeniser le texte en mots, supprimer les stopwords et les tokens non alphabétiques,
    et effectuer la lemmatisation.
    
    Parameters:
    text (str): Le texte à tokeniser.
    
    Returns:
    list: Une liste de tokens nettoyés et lemmatisés.
    """
    # Tokenisation
    tokens = word_tokenize(text)
    
    # Suppression des stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word.isalpha() and word not in stop_words]
    
    # Lemmatisation
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    
    return tokens

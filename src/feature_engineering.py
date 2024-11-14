# src/feature_engineering.py

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import joblib


def vectorize_text(text_data, method='tfidf', max_features=1000):
    """
    Vectoriser les données textuelles en utilisant TF-IDF ou CountVectorizer.
    
    Parameters:
    text_data (list or Series): Les données textuelles nettoyées à vectoriser.
    method (str): La méthode de vectorisation à utiliser ('tfidf' ou 'count').
    max_features (int): Le nombre maximum de caractéristiques à conserver.
    
    Returns:
    X (sparse matrix): Les données textuelles vectorisées.
    vectorizer (TfidfVectorizer ou CountVectorizer): Le vectoriseur ajusté.
    """
    if method == 'tfidf':
        vectorizer = TfidfVectorizer(max_features=max_features)
    elif method == 'count':
        vectorizer = CountVectorizer(max_features=max_features)
    else:
        raise ValueError("Méthode de vectorisation invalide. Utilisez 'tfidf' ou 'count'.")
    
    X = vectorizer.fit_transform(text_data)
    
    return X, vectorizer


def load_vectorizer(vectorizer_path):
    """
    Charger un vectoriseur sauvegardé depuis un fichier.
    
    Parameters:
    vectorizer_path (str): Le chemin vers le fichier vectoriseur sauvegardé.
    
    Returns:
    vectorizer (TfidfVectorizer ou CountVectorizer): Le vectoriseur chargé.
    """
    vectorizer = joblib.load(vectorizer_path)
    return vectorizer

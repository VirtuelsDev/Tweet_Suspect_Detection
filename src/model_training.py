# src/model_training.py

from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from imblearn.over_sampling import SMOTE
from imblearn.pipeline import Pipeline
import joblib


def train_model(X_train, y_train, model_type='svm', params=None):
    """
    Entraîner un modèle de machine learning sur les données d'entraînement.
    
    Parameters:
    X_train (sparse matrix): Les données d'entraînement vectorisées.
    y_train (Series or array): Les étiquettes d'entraînement.
    model_type (str): Le type de modèle à entraîner ('logistic', 'nb', 'svm', 'rf').
    params (dict): Les hyperparamètres pour le modèle.
    
    Returns:
    model: Le modèle entraîné.
    """
    if model_type == 'logistic':
        model = LogisticRegression(max_iter=1000, **(params or {}))
    elif model_type == 'nb':
        model = MultinomialNB(**(params or {}))
    elif model_type == 'svm':
        model = SVC(kernel='linear', probability=True, **(params or {}))
    elif model_type == 'rf':
        model = RandomForestClassifier(**(params or {}))
    else:
        raise ValueError("Type de modèle invalide. Utilisez 'logistic', 'nb', 'svm', ou 'rf'.")
    
    # Créer un pipeline avec SMOTE pour gérer le déséquilibre des classes
    pipeline = Pipeline([
        ('smote', SMOTE(random_state=42)),
        ('classifier', model)
    ])
    
    # Entraîner le pipeline
    pipeline.fit(X_train, y_train)
    
    return pipeline


def save_model(model, model_path):
    """
    Sauvegarder le modèle entraîné sur le disque.
    
    Parameters:
    model: Le modèle entraîné à sauvegarder.
    model_path (str): Le chemin où sauvegarder le modèle.
    """
    joblib.dump(model, model_path)

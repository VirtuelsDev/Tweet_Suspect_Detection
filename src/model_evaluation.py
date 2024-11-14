# src/model_evaluation.py

import joblib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report, confusion_matrix, roc_curve, auc, accuracy_score
from sklearn.preprocessing import label_binarize


def evaluate_model(model, X_test, y_test):
    """
    Évaluer les performances d'un modèle entraîné sur les données de test.
    
    Parameters:
    model: Le modèle entraîné.
    X_test (sparse matrix): Les données de test vectorisées.
    y_test (Series or array): Les étiquettes réelles des données de test.
    
    Returns:
    dict: Un dictionnaire contenant le rapport de classification, la matrice de confusion, et la précision.
    """
    y_pred = model.predict(X_test)
    report = classification_report(y_test, y_pred, output_dict=True)
    conf_matrix = confusion_matrix(y_test, y_pred)
    accuracy = accuracy_score(y_test, y_pred)
    
    metrics = {
        'classification_report': classification_report(y_test, y_pred),
        'confusion_matrix': conf_matrix,
        'accuracy': accuracy
    }
    
    return metrics


def plot_confusion_matrix(conf_matrix, classes, title='Matrice de Confusion', cmap='Blues'):
    """
    Tracer une matrice de confusion.
    
    Parameters:
    conf_matrix (array-like): La matrice de confusion à tracer.
    classes (list): La liste des noms des classes.
    title (str): Le titre du tracé.
    cmap (str): La carte de couleurs à utiliser.
    """
    plt.figure(figsize=(8, 6))
    sns.heatmap(conf_matrix, annot=True, fmt='d', cmap=cmap, xticklabels=classes, yticklabels=classes)
    plt.title(title)
    plt.ylabel('Réel')
    plt.xlabel('Prédit')
    plt.show()


def plot_roc_curve(model, X_test, y_test):
    """
    Tracer la courbe ROC et calculer l'AUC.
    
    Parameters:
    model: Le modèle entraîné.
    X_test (sparse matrix): Les données de test vectorisées.
    y_test (array): Les étiquettes réelles des données de test.
    """
    if hasattr(model, "predict_proba"):
        y_score = model.predict_proba(X_test)[:, 1]
    else:
        y_score = model.decision_function(X_test)
    
    fpr, tpr, _ = roc_curve(y_test, y_score)
    roc_auc = auc(fpr, tpr)
    
    plt.figure(figsize=(8, 6))
    plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'Courbe ROC (AUC = {roc_auc:.2f})')
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('Taux de Faux Positifs (FPR)')
    plt.ylabel('Taux de Vrais Positifs (TPR)')
    plt.title('Courbe ROC')
    plt.legend(loc="lower right")
    plt.show()


def load_model(model_path):
    """
    Charger un modèle entraîné depuis le disque.
    
    Parameters:
    model_path (str): Le chemin vers le fichier modèle sauvegardé.
    
    Returns:
    model: Le modèle chargé.
    """
    model = joblib.load(model_path)
    return model

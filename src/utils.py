# src/utils.py

import pandas as pd
import joblib


def load_data(file_path):
    """
    Charger les données à partir d'un fichier CSV.
    
    Parameters:
    file_path (str): Le chemin vers le fichier CSV.
    
    Returns:
    DataFrame: Le DataFrame chargé.
    """
    df = pd.read_csv(file_path)
    return df


def save_data(df, file_path):
    """
    Sauvegarder un DataFrame pandas dans un fichier CSV.
    
    Parameters:
    df (DataFrame): Le DataFrame à sauvegarder.
    file_path (str): Le chemin où sauvegarder le fichier CSV.
    """
    df.to_csv(file_path, index=False)


def save_pickle(obj, file_path):
    """
    Sauvegarder un objet Python dans un fichier pickle.
    
    Parameters:
    obj: L'objet à sauvegarder.
    file_path (str): Le chemin où sauvegarder le fichier pickle.
    """
    joblib.dump(obj, file_path)


def load_pickle(file_path):
    """
    Charger un objet Python depuis un fichier pickle.
    
    Parameters:
    file_path (str): Le chemin vers le fichier pickle.
    
    Returns:
    obj: L'objet chargé.
    """
    obj = joblib.load(file_path)
    return obj

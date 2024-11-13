# imports.py

# Bibliothèques pour la manipulation des données
import pandas as pd
import numpy as np

# Bibliothèques pour la visualisation des données
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Bibliothèques pour le traitement de texte et le NLP
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Bibliothèques pour le machine learning et le traitement des données
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report, confusion_matrix, roc_curve, auc
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

# Bibliothèques pour la gestion de l'équilibre des classes
from imblearn.over_sampling import RandomOverSampler
from imblearn.under_sampling import RandomUnderSampler
from imblearn.combine import SMOTEENN

# Bibliothèques pour l'optimisation des hyperparamètres
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV

# Bibliothèques pour le déploiement de l'application (optionnel)
try:
    import streamlit as st
except ImportError:
    print("Streamlit n'est pas installé")

try:
    from flask import Flask, request, jsonify
except ImportError:
    print("Flask n'est pas installé")

try:
    import fastapi
except ImportError:
    print("FastAPI n'est pas installé")

# Initialisation des ressources nécessaires pour nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

print("Toutes les bibliothèques ont été importées avec succès.")

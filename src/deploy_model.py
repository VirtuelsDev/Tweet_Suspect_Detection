import joblib
from sklearn.linear_model import LogisticRegression
from data_preprocessing import preprocess_data

# Entraîner et sauvegarder le modèle
def train_and_save_model(data, labels, save_path="model.joblib"):
    model = LogisticRegression()
    model.fit(data, labels)
    joblib.dump(model, save_path)

if __name__ == "__main__":
    data, labels = preprocess_data("path/to/dataset.csv")
    train_and_save_model(data, labels)
    print("Modèle déployé avec succès.")

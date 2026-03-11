"""
data_utils.py - Fonctions de chargement et nettoyage des données
Projet 5 - Système de Recommandation & GAN E-commerce
"""

from datasets import load_dataset
import pandas as pd
import os

# Dossiers de sauvegarde (relatifs à la racine du projet)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DIR = os.path.join(BASE_DIR, "data", "raw")
PROCESSED_DIR = os.path.join(BASE_DIR, "data", "processed")

def get_reviews():
    """Charge les reviews depuis le CSV local"""
    path = os.path.join(RAW_DIR, "reviews_all_beauty.csv")
    return pd.read_csv(path)


def download_reviews():
    """Télécharge le dataset Amazon All_Beauty reviews depuis HuggingFace"""
    print("Téléchargement des reviews All_Beauty...")
    dataset = load_dataset(
        "McAuley-Lab/Amazon-Reviews-2023",
        "raw_review_All_Beauty",
        trust_remote_code=True
    )
    df = dataset['full'].to_pandas()
    output_path = os.path.join(RAW_DIR, "reviews_all_beauty.csv")
    df.to_csv(output_path, index=False)
    print(f"Sauvegardé : {output_path} ({df.shape[0]} lignes)")
    return df


if __name__ == "__main__":
    os.makedirs(RAW_DIR, exist_ok=True)
    os.makedirs(PROCESSED_DIR, exist_ok=True)
    download_reviews()
    print("Téléchargement terminé !")

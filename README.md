# Projet 5 — Système Complet de Recommandation et Génération d'Images

## Description
Développement d'un système de recommandation personnalisé (LSA + KNN) et d'un générateur d'images de produits (GAN) pour une entreprise e-commerce.

## Structure
```
Projet_5_Reco/
├── data/
│   ├── raw/          # Données brutes
│   └── processed/    # Données nettoyées
├── notebooks/        # Jupyter notebooks (EDA, modèles, évaluation)
├── src/              # Modules Python réutilisables
├── outputs/
│   ├── models/       # Modèles sauvegardés
│   └── figures/      # Visualisations
├── requirements.txt
└── README.md
```

## Installation
```bash
pip install -r requirements.txt
```

## Partie 1 — Système de Recommandation
- Dataset : Amazon Product Reviews
- Modèles : LSA (content-based) + KNN (collaborative filtering)
- Métriques : Precision@K, Recall@K, F1, NDCG, ROC-AUC

## Partie 2 — Génération d'Images (GAN)
- À venir

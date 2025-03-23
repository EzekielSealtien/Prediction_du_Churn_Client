# About the project

Objectif du projet :
Anticiper les départs de clients pour aider les entreprises à adapter leur stratégie de fidélisation et limiter les pertes. Le modèle permet ainsi d’identifier les clients susceptibles de quitter le service, afin d’agir en amont.
Étapes du projet :
1.	Prétraitement des données
o	Nettoyage des données manquantes
o	Encodage des variables catégorielles (Label Encoding pour les binaires, One-Hot Encoding pour les autres)
o	Séparation en X et y, puis split en jeu d’entraînement et de test
o	Feature scaling sur les variables numériques uniquement
2.	Entraînement de plusieurs modèles J’ai testé 2 différents algorithmes :
o	Random Forest
o	XGBoost
3.	Évaluation des performances
o	Accuracy, precision, recall, F1-score, ROC-AUC
o	Optimisation des hyperparamètres via GridSearchCV
o	Analyse comparative des modèles
Le modèle qui a obtenu les meilleures performances est XGBoost, avec une accuracy de 80.60 %.Random Forest a obtenu une accuracy de 80.11% et a également montré une bonne robustesse et une interprétabilité intéressante via l’analyse de l’importance des features.
4.	Explication du modèle
o	Visualisation des variables les plus influentes
o	Mise en évidence du poids de certaines variables comme : ancienneté client,frais totaux (total charges),frais mensuel(monthly charges),Internet Service (fibre optique), Type de contrat, méthode de paiement, etc.
5.	Réseau de Neurones (ANN) Pour aller plus loin, j’ai aussi implémenté un ANN avec :
o	Deux couches cachées (activation ReLU)
o	Couche de sortie sigmoid pour une classification binaire
o	Optimiseur : Adam, fonction de perte : binary_crossentropy

Stack technique :
•	Frontend : Streamlit
•	Backend : FastAPI
•	Modélisation : Scikit-learn, XGBoost,RandomForest, TensorFlow/Keras
•	CI/CD : GitHub Actions
•	Sérialisation avec Joblib
•	Hébergement sur Heroku
Code source :
Démo en ligne :


 

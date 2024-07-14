import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

data = pd.read_csv('../dataset/final_dataset.csv', parse_dates=['GAME_DATE'], dtype={'gameId' : str, 'H_teamId' : str, 'A_teamId' : str, })
data = data.round(2)
# Separation du jeu de test et d'entrainement
condition = (data['GAME_DATE'] > pd.to_datetime('2023-09-01')) & (data['GAME_DATE'] < pd.to_datetime('2024-09-01'))
# Les donnees avant septembre 2023
data_test = data[condition]
# Suppression des colonnnes qui ne sont pas nécessaires
data_test = data_test.drop(columns=['GAME_DATE','gameId', 'A_teamId', 'H_teamId', 'H_teamName', 'A_teamName', 'H_POINTS', 'A_POINTS', 'ELO_PROB','DIFF_W' ])

# Les donnees apres septembre 2023
data_train = data[~condition]
# Suppression des colonnnes qui ne sont pas nécessaires
data_train = data_train.drop(columns=['GAME_DATE','gameId', 'A_teamId', 'H_teamId', 'H_teamName', 'A_teamName', 'H_POINTS', 'A_POINTS', 'ELO_PROB', 'DIFF_W'])

X_train = data_train.drop(columns=['HOME_WON'])  # Fonctionnalités
y_train = data_train['HOME_WON']  # Cible

X_test = data_test.drop(columns=['HOME_WON'])  # Fonctionnalités
y_test = data_test['HOME_WON']

rf = RandomForestClassifier(n_estimators=100, random_state=42)

rf.fit(X_train, y_train)

from sklearn.metrics import accuracy_score, f1_score

# Faire des prédictions sur les données de test
predictions = rf.predict(X_test)

# Évaluer les performances du modèle
accuracy = accuracy_score(y_test, predictions)
print("Random Forest Accuracy:", accuracy)

# Calcul du score F1
f1 = f1_score(y_test, predictions)

print("Score F1:", f1)

feature_importances = rf.feature_importances_
print(feature_importances)

feature_importances = rf.feature_importances_
column_names = X_train.columns
importances_df = pd.DataFrame({'feature': column_names, 'importance': feature_importances})
importances_df = importances_df.sort_values('importance', ascending=False).reset_index(drop=True)
print(importances_df)
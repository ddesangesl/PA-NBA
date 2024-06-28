from sklearn.neural_network import MLPClassifier
import pandas as pd
from sklearn.metrics import confusion_matrix

from sklearn.metrics import make_scorer, accuracy_score, f1_score
from sklearn.preprocessing import StandardScaler, MinMaxScaler

data = pd.read_csv('../dataset/final_dataset.csv', parse_dates=['GAME_DATE'], dtype={'gameId' : str, 'H_teamId' : str, 'A_teamId' : str,})
data = data.round(2)

condition = (data['GAME_DATE'] > pd.to_datetime('2023-09-01')) & (data['GAME_DATE'] < pd.to_datetime('2024-09-01'))
data_test = data[condition]
X_test = data_test.drop(columns=['ELO_PROB','HOME_WON', 'GAME_DATE','gameId', 'A_teamId', 'H_teamId','H_teamId','A_teamId','H_POINTS', 'A_POINTS','H_teamName', 'A_teamName','trueShootingPercentage_L10', 'PCT_TIR_REUSSI_L10', 'effectiveFieldGoalPercentage_L10', 'NB_WIN_L10', 'PCT_3PT_L10', 'W_CONFR_D'])  # Fonctionnalités
data_train = data[~condition]
X_train  = data_test.drop(columns=['ELO_PROB','HOME_WON', 'GAME_DATE','gameId', 'A_teamId', 'H_teamId','H_teamId','A_teamId','H_POINTS', 'A_POINTS','H_teamName', 'A_teamName','trueShootingPercentage_L10', 'PCT_TIR_REUSSI_L10', 'effectiveFieldGoalPercentage_L10', 'NB_WIN_L10', 'PCT_3PT_L10', 'W_CONFR_D'])  # Fonctionnalités

#X_train = data_train.drop('HOME_WON', axis=1)  # Fonctionnalités
y_train = data_train['HOME_WON']  # Cible

#X_test = data_test.drop('HOME_WON', axis=1)  # Fonctionnalités
y_test = data_test['HOME_WON']

scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Définir les métriques de performance à calculer
scoring = {'accuracy': make_scorer(accuracy_score), 'f1': make_scorer(f1_score)}

clf = MLPClassifier(hidden_layer_sizes=(100,), activation='relu', solver='adam', max_iter=100000, random_state=50)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)  # y_test sont les étiquettes de classe réelles des données de test
f1 = f1_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

print("Accuracy:", accuracy)
print("F1-score:", f1)
print("Matrice de confusion :")
print(conf_matrix)
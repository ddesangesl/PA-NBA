from sklearn import svm
import pandas as pd
from sklearn.model_selection import cross_validate, train_test_split
from sklearn.metrics import make_scorer, accuracy_score, f1_score
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import numpy as np
from sklearn.preprocessing import OneHotEncoder

data = pd.read_csv('../dataset/final_dataset.csv', parse_dates=['GAME_DATE'], dtype={'gameId' : str, 'H_teamId' : str, 'A_teamId' : str,})
data = data.round(2)

condition = (data['GAME_DATE'] > pd.to_datetime('2023-09-01')) & (data['GAME_DATE'] < pd.to_datetime('2024-09-01'))
data_test = data[condition]
#data_test = data_test.drop(columns=['GAME_DATE','gameId', 'A_teamId', 'H_teamId'])
data_train = data[~condition]
#data_train = data_train.drop(columns=['GAME_DATE','gameId', 'A_teamId', 'H_teamId'])

#data_train = data_train.drop(columns=['GAME_DATE','gameId', 'A_teamId', 'H_teamId'])
X_train = data_train.drop(columns=['ELO_PROB','HOME_WON', 'GAME_DATE','gameId', 'A_teamId', 'H_teamId','H_teamId','A_teamId','H_POINTS', 'A_POINTS','H_teamName', 'A_teamName','trueShootingPercentage_L10', 'PCT_TIR_REUSSI_L10', 'effectiveFieldGoalPercentage_L10', 'NB_WIN_L10', 'PCT_3PT_L10', 'W_CONFR_D'])  # Fonctionnalités
y_train = data_train['HOME_WON']  # Cible

X_test = data_test.drop(columns=['ELO_PROB','HOME_WON', 'GAME_DATE','gameId', 'A_teamId', 'H_teamId','H_teamId','A_teamId','H_POINTS', 'A_POINTS','H_teamName', 'A_teamName','trueShootingPercentage_L10', 'PCT_TIR_REUSSI_L10', 'effectiveFieldGoalPercentage_L10', 'NB_WIN_L10', 'PCT_3PT_L10', 'W_CONFR_D'])  # Fonctionnalités
y_test = data_test['HOME_WON']

scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Définir les métriques de performance à calculer
scoring = {'accuracy': make_scorer(accuracy_score), 'f1': make_scorer(f1_score)}

svm_classifier = svm.SVC(kernel='sigmoid', gamma =0.0145)

svm_classifier.fit(X_train, y_train)
y_pred = svm_classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)  # y_test sont les étiquettes de classe réelles des données de test
f1 = f1_score(y_test, y_pred)

print("SVM Accuracy:", accuracy)
print("F1-score:", f1)
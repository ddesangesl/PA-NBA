import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import make_scorer, accuracy_score, f1_score, confusion_matrix
from sklearn.ensemble import AdaBoostClassifier
from data_modele import get_data_for_training

X_train, X_test, y_train, y_test, data_test, scaler = get_data_for_training()

# Définir les métriques de performance à calculer
scoring = {'accuracy': make_scorer(accuracy_score), 'f1': make_scorer(f1_score)}

ada_boost = AdaBoostClassifier(n_estimators=30)
ada_boost.fit(X_train, y_train)
y_pred = ada_boost.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)  # y_test sont les étiquettes de classe réelles des données de test
f1 = f1_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

print("Accuracy:", accuracy)
print("F1-score:", f1)
print("Matrice de confusion :")
print(conf_matrix)

#data_knn_predict = data_test[['gameId', 'GAME_DATE', 'HOME_WON', 'H_POINTS', 'A_POINTS','H_teamName', 'A_teamName']].copy()
#data_knn_predict.loc[:, 'PRED'] = y_pred
#data_knn_predict = data_knn_predict[['gameId', 'GAME_DATE', 'HOME_WON', 'PRED', 'H_POINTS', 'A_POINTS','H_teamName', 'A_teamName']]

#data_knn_predict.set_index('gameId', inplace=True)
#data_knn_predict = data_knn_predict.sort_values(by='GAME_DATE')
#data_knn_predict.transpose().to_json("../dataset/KNN_predict.json")
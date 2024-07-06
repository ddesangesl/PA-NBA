import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import make_scorer, accuracy_score, f1_score, confusion_matrix
import joblib

data = pd.read_csv('../dataset/final_dataset.csv', parse_dates=['GAME_DATE'], dtype={'gameId' : str, 'H_teamId' : str, 'A_teamId' : str,})
data = data.round(2)

condition = (data['GAME_DATE'] > pd.to_datetime('2023-09-01')) & (data['GAME_DATE'] < pd.to_datetime('2024-09-01'))
data_test = data[condition]
data_train = data[~condition]

X_train = data_train.drop(columns=['ELO_PROB', 'HOME_WON', 'GAME_DATE','gameId', 'A_teamId', 'H_teamId','H_teamId','A_teamId','H_POINTS', 'A_POINTS','H_teamName', 'A_teamName','trueShootingPercentage_L10', 'PCT_TIR_REUSSI_L10', 'effectiveFieldGoalPercentage_L10','NB_WIN_L10', 'PCT_3PT_L10', 'W_CONFR_D'])  # Fonctionnalités
y_train = data_train['HOME_WON']  # Cible

X_test = data_test.drop(columns=['ELO_PROB','HOME_WON', 'GAME_DATE','gameId', 'A_teamId', 'H_teamId','H_teamId','A_teamId','H_POINTS', 'A_POINTS','H_teamName', 'A_teamName','trueShootingPercentage_L10', 'PCT_TIR_REUSSI_L10', 'effectiveFieldGoalPercentage_L10', 'NB_WIN_L10', 'PCT_3PT_L10', 'W_CONFR_D'])  # Fonctionnalités
y_test = data_test['HOME_WON']

scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

scoring = {'accuracy': make_scorer(accuracy_score), 'f1': make_scorer(f1_score)}

knn = KNeighborsClassifier(n_neighbors=28, weights='distance', metric='minkowski', p=2)

knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)  # y_test sont les étiquettes de classe réelles des données de test
f1 = f1_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

print("K-NN Accuracy:", accuracy)
#print("F1-score:", f1)
#print("Matrice de confusion :")
#print(conf_matrix)

data_knn_predict = data_test[['gameId', 'GAME_DATE', 'HOME_WON', 'H_POINTS', 'A_POINTS','H_teamName', 'A_teamName']].copy()
data_knn_predict.loc[:, 'PRED'] = y_pred
data_knn_predict = data_knn_predict[['gameId', 'GAME_DATE', 'HOME_WON', 'PRED', 'H_POINTS', 'A_POINTS','H_teamName', 'A_teamName']]
data_knn_predict.set_index('gameId', inplace=True)
data_knn_predict = data_knn_predict.sort_values(by='GAME_DATE')
data_knn_predict.to_csv("../dataset/KNN_predict.csv")

data_knn_predict.transpose().to_json("../dataset/KNN_predict.json")
# Enregistrer le modèle
joblib_file = "KNN.pkl"
joblib.dump(knn, joblib_file)

loaded_model = joblib.load("KNN.pkl")
joblib.dump(scaler, 'scaler.pkl')

y_pred = loaded_model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)  # y_test sont les étiquettes de classe réelles des données de test
f1 = f1_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

# Afficher les prédictions
print(accuracy)
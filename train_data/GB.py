from sklearn.metrics import make_scorer, accuracy_score, f1_score, confusion_matrix
from sklearn.ensemble import GradientBoostingClassifier
import joblib
from data_modele import get_data_for_training

X_train, X_test, y_train, y_test, data_test, scaler = get_data_for_training()

scoring = {'accuracy': make_scorer(accuracy_score), 'f1': make_scorer(f1_score)}

# Definition du modele et des ses hyperparametre
gb = GradientBoostingClassifier(n_estimators=26, loss='exponential', learning_rate=0.1)
gb.fit(X_train, y_train)
y_pred = gb.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)  # y_test sont les étiquettes de classe réelles des données de test
f1 = f1_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

print("Gradient Boosting Classifier Accuracy:", accuracy)
print("F1-score:", f1)
print("Matrice de confusion :")
print(conf_matrix)

# Creation du dataframe contenant tout les information de chaque match de la saison 2023-2024 avec leur prédiciton
data_gb_predict = data_test[['gameId', 'GAME_DATE', 'HOME_WON', 'H_POINTS', 'A_POINTS', 'H_teamName', 'A_teamName']].copy()
data_gb_predict.loc[:, 'PRED'] = y_pred
data_gb_predict = data_gb_predict[['gameId', 'GAME_DATE', 'HOME_WON', 'PRED', 'H_POINTS', 'A_POINTS', 'H_teamName', 'A_teamName']]
data_gb_predict.set_index('gameId', inplace=True)
data_gb_predict = data_gb_predict.sort_values(by='GAME_DATE')

# Enregistrement du dataframe dans un CSV pour l'analyse des résultat
data_gb_predict.to_csv('../dataset/GB_predict.csv')

# Enregistrement du dataframe dans un JSON afin d'afficher les prédiction de la saison 2023-24 dans l'application web
data_gb_predict.transpose().to_json("../dataset/GB_predict.json")

# Enregistrement du modèle
joblib_file = "../modele/GB.pkl"
joblib.dump(gb, joblib_file)
joblib.dump(scaler, '../modele/GB_scaler.pkl')
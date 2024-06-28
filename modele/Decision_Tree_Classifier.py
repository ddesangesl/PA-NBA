from sklearn.datasets import load_iris
from sklearn.model_selection import cross_validate
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
from sklearn.metrics import make_scorer, accuracy_score, f1_score
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Charger votre jeu de données

data = pd.read_csv('../dataset/final_dataset.csv', parse_dates=['GAME_DATE'], dtype={'gameId' : str, 'H_teamId' : str, 'A_teamId' : str,})

data.drop(columns=['ELO_PROB', 'GAME_DATE','gameId', 'A_teamId', 'H_teamId','H_teamId','A_teamId','H_POINTS', 'A_POINTS','H_teamName', 'A_teamName','trueShootingPercentage_L10', 'PCT_TIR_REUSSI_L10', 'effectiveFieldGoalPercentage_L10','NB_WIN_L10', 'PCT_3PT_L10', 'W_CONFR_D'], inplace=True)
#X_train = data_train.drop(columns=['ELO_PROB', 'HOME_WON', 'GAME_DATE','gameId', 'A_teamId', 'H_teamId','H_teamId','A_teamId','H_POINTS', 'A_POINTS','H_teamName', 'A_teamName','trueShootingPercentage_L10', 'PCT_TIR_REUSSI_L10', 'effectiveFieldGoalPercentage_L10','NB_WIN_L10', 'PCT_3PT_L10', 'W_CONFR_D'])  # Fonctionnalités

# Séparer les fonctionnalités (X) de la cible (y)
X = data.drop('HOME_WON', axis=1)  # Fonctionnalités
y = data['HOME_WON']  # Cible

scaler = MinMaxScaler()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X = scaler.fit_transform(X)
scoring = {'accuracy': make_scorer(accuracy_score), 'f1': make_scorer(f1_score)}

model = DecisionTreeClassifier(
    criterion='gini',       # Métrique utilisée pour mesurer la qualité de la division (gini ou entropy)
    max_depth=4,            # Profondeur maximale de l'arbre (3 pour cet exemple, vous pouvez ajuster)
    min_samples_split=5,    # Nombre minimal d'échantillons requis pour diviser un nœud interne
    min_samples_leaf=2,     # Nombre minimal d'échantillons requis pour être à un nœud feuille
    max_features=10   # Nombre de caractéristiques à considérer lors de la recherche de la meilleure division
)

tree =model.fit(X_train, y_train)
cv_results = cross_validate(tree, X, y, cv=5, scoring=scoring)

# Afficher les scores de performance pour chaque fold
print("Scores de validation croisée - Accuracy : ", cv_results['test_accuracy'])
print("Scores de validation croisée - F1 : ", cv_results['test_f1'])

# Calculer la moyenne des scores de performance
mean_accuracy = cv_results['test_accuracy'].mean()
mean_f1 = cv_results['test_f1'].mean()
print("Accuracy moyenne avec validation croisée : {:.2f}%".format(mean_accuracy * 100))
print("F1 moyenne avec validation croisée : {:.2f}".format(mean_f1))

predictions = model.predict(X_test)

# Calculer la précision du modèle
accuracy = accuracy_score(y_test, predictions)
print("Précision du modèle :", accuracy)
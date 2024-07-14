import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import cross_validate
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
from sklearn.metrics import make_scorer, accuracy_score, f1_score
from sklearn.preprocessing import StandardScaler, MinMaxScaler

df = pd.read_csv('../dataset/final_dataset.csv', parse_dates=['GAME_DATE'], dtype={'gameId' : str, 'H_teamId' : str, 'A_teamId' : str, })


df = df.apply(pd.to_numeric, errors='coerce')

# Calculer la moyenne mobile des dernières 10 valeurs pour chaque colonne
rolling_avg_cols = df.columns[1:]  # Toutes les colonnes sauf 'HOME_WON'
for col in rolling_avg_cols:
    df[col + '_RollingAvg'] = df[col].rolling(window=10, min_periods=1).mean()

# Calculer la différence entre la valeur actuelle et la moyenne mobile des dernières 10 valeurs
for col in rolling_avg_cols:
    df[col + '_DiffFromRollingAvg'] = df[col] - df[col + '_RollingAvg']

# Supprimer les colonnes intermédiaires si nécessaire
# df.drop(rolling_avg_cols, axis=1, inplace=True)

# Afficher les nouvelles caractéristiques
print(df.head())

# Convertir de nouveau en liste
training_data_with_features = df.values.tolist()

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Séparation des caractéristiques et de la cible
X = df.drop('HOME_WON', axis=1)  # Utiliser toutes les colonnes sauf 'HOME_WON' comme caractéristiques
y = df['HOME_WON']  # La colonne 'HOME_WON' est la cible

# Division des données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scoring = {'accuracy': make_scorer(accuracy_score), 'f1': make_scorer(f1_score)}

# Création du modèle avec les nouvelles caractéristiques
model = DecisionTreeClassifier(
    criterion='gini',        # Métrique utilisée pour mesurer la qualité de la division (gini ou entropy)
    max_depth=4,             # Profondeur maximale de l'arbre (3 pour cet exemple, vous pouvez ajuster)
    min_samples_split=5,     # Nombre minimal d'échantillons requis pour diviser un nœud interne
    min_samples_leaf=2,      # Nombre minimal d'échantillons requis pour être à un nœud feuille
    max_features=None       # Utiliser toutes les caractéristiques disponibles
)

# Entraînement du modèle
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

# Prédiction sur l'ensemble de test
y_pred = model.predict(X_test)
# Calcul de l'accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Vous pouvez également imprimer d'autres métriques comme la matrice de confusion
from sklearn.metrics import confusion_matrix
conf_matrix = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(conf_matrix)

# Affichage de l'arbre de décision
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

plt.figure(figsize=(20, 10))
plot_tree(model, feature_names=X.columns, class_names=['HOME_LOST', 'HOME_WON'], filled=True, fontsize=10)
plt.show()
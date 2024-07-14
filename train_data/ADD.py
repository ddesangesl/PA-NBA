from sklearn.metrics import confusion_matrix
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
from sklearn.metrics import make_scorer, accuracy_score, f1_score
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from data_modele import get_data_for_training

X_train, X_test, y_train, y_test, data_test, scaler = get_data_for_training()

scoring = {'accuracy': make_scorer(accuracy_score), 'f1': make_scorer(f1_score)}

model = DecisionTreeClassifier(
    criterion='gini',       # Métrique utilisée pour mesurer la qualité de la division (gini ou entropy)
    max_depth=2,            # Profondeur maximale de l'arbre (3 pour cet exemple, vous pouvez ajuster)
    min_samples_split=5,    # Nombre minimal d'échantillons requis pour diviser un nœud interne
    min_samples_leaf=2,     # Nombre minimal d'échantillons requis pour être à un nœud feuille
    max_features=5 # Nombre de caractéristiques à considérer lors de la recherche de la meilleure division
)

tree =model.fit(X_train, y_train)

y_pred = tree.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)  # y_test sont les étiquettes de classe réelles des données de test
f1 = f1_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

print("Decision Tree Classifier Accuracy:", accuracy)
print("F1-score:", f1)
print("Matrice de confusion :")
print(conf_matrix)
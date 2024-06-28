#%%
import pandas as pd
from tensorflow.keras import layers, models
from sklearn.metrics import make_scorer, accuracy_score, f1_score
from sklearn.preprocessing import StandardScaler, MinMaxScaler

data = pd.read_csv('../dataset/final_dataset.csv', parse_dates=['GAME_DATE'], dtype={'gameId' : str, 'H_teamId' : str, 'A_teamId' : str,})
data = data.round(2)

condition = (data['GAME_DATE'] > pd.to_datetime('2023-09-01')) & (data['GAME_DATE'] < pd.to_datetime('2024-09-01'))
data_test = data[condition]
data_test = data_test.drop(columns=['GAME_DATE', 'gameId', 'A_teamId', 'H_teamId'])
data_train = data[~condition]
data_train = data_train.drop(columns=['GAME_DATE', 'gameId', 'A_teamId', 'H_teamId'])
X_train = data_train.drop('HOME_WON', axis=1)  # Fonctionnalités
y_train = data_train['HOME_WON']  # Cible

X_test = data_test.drop('HOME_WON', axis=1)  # Fonctionnalités
y_test = data_test['HOME_WON']

scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.fit_transform(X_test)
# Définir les métriques de performance à calculer
scoring = {'accuracy': make_scorer(accuracy_score), 'f1': make_scorer(f1_score)}

# Création du modèle PMC
def create_mlp(input_shape, num_classes):
    model = models.Sequential([
        layers.Dense(65, activation='relu', input_shape=input_shape),
        layers.Dense(65, activation='relu'),
        layers.Dense(num_classes, activation='softmax')
    ])
    return model

# Création du modèle
model = create_mlp(input_shape=X_train[0].shape, num_classes=2)

# Compilation du modèle
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Entraînement du modèle
history = model.fit(X_train, y_train, epochs=10, validation_data=(X_test, y_test))

# Évaluation du modèle
test_loss, test_acc = model.evaluate(X_test, y_test)
print('Test accuracy:', test_acc)
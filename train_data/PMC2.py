#%%
import pandas as pd
from tensorflow.keras import layers, models
from sklearn.metrics import make_scorer, accuracy_score, f1_score
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from data_modele import get_data_for_training

X_train, X_test, y_train, y_test, data_test, scaler = get_data_for_training()

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
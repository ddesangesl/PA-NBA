from sklearn import svm
import pandas as pd
from sklearn.metrics import make_scorer, accuracy_score, f1_score
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from data_modele import get_data_for_training

X_train, X_test, y_train, y_test, data_test, scaler = get_data_for_training()

scoring = {'accuracy': make_scorer(accuracy_score), 'f1': make_scorer(f1_score)}

# Definition du modele et des ses hyperparametre
svm_classifier = svm.SVC(kernel='sigmoid', gamma =0.0145)

svm_classifier.fit(X_train, y_train)
y_pred = svm_classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print("SVM Accuracy:", accuracy)
print("F1-score:", f1)
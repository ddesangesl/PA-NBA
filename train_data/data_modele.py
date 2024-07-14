import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import make_scorer, accuracy_score, f1_score

def get_data_for_training() :
    data = pd.read_csv('../dataset/final_dataset.csv', parse_dates=['GAME_DATE'], dtype={'gameId' : str, 'H_teamId' : str, 'A_teamId' : str, })
    # Arrondissement des valeurs du dataframe à deux chiffes apres la virgule
    data = data.round(2)

    # Separation du jeu de test et d'entrainement
    condition = (data['GAME_DATE'] > pd.to_datetime('2023-09-01')) & (data['GAME_DATE'] < pd.to_datetime('2024-09-01'))
    # Les donnees avant septembre 2023
    data_test = data[condition]

    # Les donnees apres septembre 2023
    data_train = data[~condition]

    # Suppression des colonnnes qui ne sont pas nécessaires
    X_train = data_train.drop(columns=[ 'HOME_WON', 'GAME_DATE','gameId', 'A_teamId', 'H_teamId','H_teamId','A_teamId','H_POINTS', 'A_POINTS','H_teamName', 'A_teamName', 'estimatedUsagePercentage_L10', 'trueShootingPercentage_L10', 'effectiveFieldGoalPercentage_L10', 'reboundPercentage_L10', 'NB_WIN_L10', 'PCT_TIR_REUSSI_L10', 'PIE_L10', 'PCT_3PT_L10', 'PCT_LANCER_FRANC_L10', 'pace_L10'])  # Fonctionnalités
    y_train = data_train['HOME_WON']  # Cible

    # Suppression des colonnnes qui ne sont pas nécessaires
    X_test = data_test.drop(columns=['HOME_WON', 'GAME_DATE','gameId', 'A_teamId', 'H_teamId','H_teamId','A_teamId','H_POINTS', 'A_POINTS','H_teamName', 'A_teamName', 'estimatedUsagePercentage_L10', 'trueShootingPercentage_L10', 'effectiveFieldGoalPercentage_L10', 'reboundPercentage_L10', 'NB_WIN_L10', 'PCT_TIR_REUSSI_L10', 'PIE_L10', 'PCT_3PT_L10', 'PCT_LANCER_FRANC_L10', 'pace_L10' ])  # Fonctionnalités
    y_test = data_test['HOME_WON']


    scaler = MinMaxScaler()
    X_train = scaler.fit_transform(X_train)

    X_test = scaler.transform(X_test)

    return X_train, X_test, y_train, y_test, data_test, scaler


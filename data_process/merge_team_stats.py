import pandas as pd

#Fonction qui fait la fusion du dataset des statistique classique et du dataset des statistique avancé
def  merge_team_stats():
    print('merge_team_stats...')
    team_adv_stats = pd.read_csv('../dataset/team_adv_stats.csv', dtype={'teamId': str, 'gameId': str})
    team_stat = pd.read_csv('../dataset/team_stat.csv', dtype={'Team_ID': str, 'Game_ID': str})

    team_stat = team_stat.rename(columns={'Team_ID': 'teamId', 'Game_ID': 'gameId'})

    team_stat.columns = ['teamId', 'gameId', 'GAME_DATE', 'DUEL', 'WL', 'NB_VICTOIRE',
                         'NB_DEFAITE', 'PCT_VICTOIRE', 'DUREE_MATCH', 'TIR REUSSI', 'TIR TENTE',
                         'PCT_TIR_REUSSI', '3PTS_REUSSI', '3PTS_TENTE', 'PCT_3PTS',
                         'LANCER_FRANC_REUSSI', 'LANCER_FRANC_TENTE', 'PCT_LANCER_FRANC',
                         'REBOND_OFF', 'REBOND_DEF', 'REBOND', 'PASSE_D', 'INTERCEPTION',
                         'TIR_CONTRE', 'BALLON_PERDU', 'FAUTES', 'TOTAL_POINTS']

    merged_df = pd.merge(team_stat, team_adv_stats, on=['gameId', 'teamId'])

    # Convertir la colonne 'GAME_DATE' en format de date
    merged_df['GAME_DATE'] = pd.to_datetime(merged_df['GAME_DATE'], format='%b %d, %Y')

    # Trie le DataFrame en fonction de la date
    df_sorted = merged_df.sort_values(by='GAME_DATE')

    # Supprime les données de la période COVID
    df_sorted = df_sorted.loc[(df_sorted["GAME_DATE"] < pd.to_datetime('2020-05-01')) | (df_sorted["GAME_DATE"] > pd.to_datetime('2021-09-01'))]
    return df_sorted
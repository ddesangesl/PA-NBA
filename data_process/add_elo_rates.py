import pandas as pd


def add_elo_rates(df_stat_flatten):
    print("adding elo rates...")
    data_type = {"gameId": str, "teamId": str, "H_teamId": str, "A_teamId": str, "W_CONFR_D": int}
    nba_elo = pd.read_csv('../dataset/nba_elo.csv', dtype=data_type)
    nba_elo_copy= nba_elo.copy()

    # Liste des noms des colonnes à supprimer
    columns_to_drop = ['season', 'neutral', 'playoff', 'team2', 'elo1_post', 'elo2_post', 'score1', 'score2',
                       'is_home']

    nba_elo_copy_drop = nba_elo_copy.drop(columns=columns_to_drop)
    # Renomme les équipe qui ne sont pas noter de la meme maniere que celles de la dataset des stattistique classique et avance
    nba_elo_copy_drop['team1'] = nba_elo_copy_drop['team1'].replace({'PHO': 'PHX', 'BRK': 'BKN', 'CHO': 'CHA'})


    df_stat_flatten['team1'] = df_stat_flatten['DUEL'].str.split(' vs. ').str[0]
    new_column_names = {'date': 'GAME_DATE'}
    nba_elo_copy_drop_rename = nba_elo_copy_drop.rename(columns=new_column_names)
    nba_elo_copy_drop_rename['GAME_DATE'] = pd.to_datetime(nba_elo_copy_drop_rename['GAME_DATE'])
    df_stat_flatten = pd.merge(df_stat_flatten, nba_elo_copy_drop_rename, on=['GAME_DATE', 'team1'])

    new_column_names = {'elo1_pre': 'H_ELO', 'elo2_pre': 'A_ELO', 'elo_prob1': 'H_ELO_PROB', 'elo_prob2': 'A_ELO_PROB'}
    df_stat_flatten = df_stat_flatten.rename(columns=new_column_names)
    return df_stat_flatten

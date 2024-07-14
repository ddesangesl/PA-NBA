import numpy as np
import pandas as pd


def get_last_perf(df_stat):
    print('get_last_perf...')
    nb_games = "10"

    df_game_info = df_stat[["TOTAL_POINTS", "DUEL", 'GAME_DATE']].copy()
    df_game_info.loc[:, 'teamName'] = df_stat['teamCity'] + " " + df_stat['teamName']

    # Retourne la différence du bilan de la saison entre l'équipe à domicile et à l'exterieur
    def get_w_diff(team_stats, index):
        if index == 0 or team_stats['NB_VICTOIRE'][index - 1] + team_stats['NB_DEFAITE'][index - 1] == 82:
            return 0
        else:
            return team_stats['NB_VICTOIRE'][index - 1] - team_stats['NB_DEFAITE'][index - 1]


    # Définition des colonne de la dataframe contenant la moyenne des 10 derniere performance avant chaque match
    df_stat_last_perf = pd.DataFrame(
        columns=['gameId', 'teamId', 'GAME_DATE', 'DUEL', 'WL', 'DIFF_W', 'NB_WIN_L' + nb_games, "POINTS_L" + nb_games,
                 'PCT_TIR_REUSSI_L' + nb_games, 'PCT_3PTS_L' + nb_games,
                 'PCT_LANCER_FRANC_L' + nb_games, "PASSE_D_L" + nb_games, "REBOND_L" + nb_games,
                 "REBOND_OFF_L" + nb_games, "REBOND_DEF_L" + nb_games, "INTERCEPTION_L" + nb_games,
                 "TIR_CONTREE_L" + nb_games, "BALLON_PERDU_L" + nb_games, "FAUTES_L" + nb_games,
                 'estimatedOffensiveRating_L' + nb_games, 'offensiveRating_L' + nb_games,
                 'estimatedDefensiveRating_L' + nb_games,
                 'defensiveRating_L' + nb_games, 'estimatedNetRating_L' + nb_games, 'netRating_L' + nb_games,
                 'assistPercentage_L' + nb_games,
                 'assistToTurnover_L' + nb_games, 'assistRatio_L' + nb_games,
                 'estimatedTeamTurnoverPercentage_L' + nb_games, 'turnoverRatio_L' + nb_games,
                 'effectiveFieldGoalPercentage_L' + nb_games, 'trueShootingPercentage_L' + nb_games,
                 'estimatedPace_L' + nb_games, 'pace_L' + nb_games,
                 'pacePer40_L' + nb_games, 'PIE_L' + nb_games, "offensiveReboundPercentage_L" + nb_games,
                 "defensiveReboundPercentage_L" + nb_games, "reboundPercentage_L" + nb_games,
                 "estimatedUsagePercentage_L" + nb_games, "possesions_L" + nb_games])

    # Crée une ligne contenant les moyenne des stats des 10 dernier performance d'une équipe avant chacun des ses match
    for team in list(set(df_stat['teamId'].tolist())):
        team_stats = df_stat[df_stat['teamId'] == team]
        team_stats.reset_index(drop=True, inplace=True)
        index = 0
        while index < len(team_stats):
            df_last_10_games = team_stats.iloc[max(0, index - int(nb_games)):index]
            df_last_10_games.reset_index(drop=True, inplace=True)
            new_row = {"gameId": team_stats['gameId'][index],
                       "teamId": team_stats['teamId'][index],
                       "GAME_DATE": team_stats['GAME_DATE'][index],
                       "DUEL": team_stats['DUEL'][index],
                       "WL": team_stats['WL'][index],
                       #"DIFF_W" : get_w_diff(team_stats, index),
                       "NB_WIN_L" + nb_games: (df_last_10_games['WL'] == 'W').sum() / int(nb_games),
                       "POINTS_L" + nb_games: df_last_10_games['TOTAL_POINTS'].mean(),
                       "PCT_TIR_REUSSI_L" + nb_games: df_last_10_games['PCT_TIR_REUSSI'].mean(),
                       "PCT_3PTS_L" + nb_games: df_last_10_games['PCT_3PTS'].mean(),
                       "PCT_LANCER_FRANC_L" + nb_games: df_last_10_games['PCT_LANCER_FRANC'].mean(),
                       "PASSE_D_L" + nb_games: df_last_10_games['PASSE_D'].mean(),
                       "REBOND_L" + nb_games: df_last_10_games['REBOND'].mean(),
                       "REBOND_OFF_L" + nb_games: df_last_10_games['REBOND_OFF'].mean(),
                       "REBOND_DEF_L" + nb_games: df_last_10_games['REBOND_DEF'].mean(),
                       "INTERCEPTION_L" + nb_games: df_last_10_games['INTERCEPTION'].mean(),
                       "TIR_CONTREE_L" + nb_games: df_last_10_games['TIR_CONTRE'].mean(),
                       "BALLON_PERDU_L" + nb_games: df_last_10_games['BALLON_PERDU'].mean(),
                       "FAUTES_L" + nb_games: df_last_10_games['FAUTES'].mean(),
                       "estimatedOffensiveRating_L" + nb_games: df_last_10_games['estimatedOffensiveRating'].mean(),
                       "offensiveRating_L" + nb_games: df_last_10_games['offensiveRating'].mean(),
                       "estimatedDefensiveRating_L" + nb_games: df_last_10_games['estimatedDefensiveRating'].mean(),
                       "defensiveRating_L" + nb_games: df_last_10_games['defensiveRating'].mean(),
                       "estimatedNetRating_L" + nb_games: df_last_10_games['estimatedNetRating'].mean(),
                       "netRating_L" + nb_games: df_last_10_games['netRating'].mean(),
                       "assistPercentage_L" + nb_games: df_last_10_games['assistPercentage'].mean(),
                       "assistToTurnover_L" + nb_games: df_last_10_games['assistToTurnover'].mean(),
                       "assistRatio_L" + nb_games: df_last_10_games['assistRatio'].mean(),
                       "offensiveReboundPercentage_L" + nb_games: df_last_10_games['offensiveReboundPercentage'].mean(),
                       "defensiveReboundPercentage_L" + nb_games: df_last_10_games['defensiveReboundPercentage'].mean(),
                       "reboundPercentage_L" + nb_games: df_last_10_games['reboundPercentage'].mean(),
                       "estimatedTeamTurnoverPercentage_L" + nb_games: df_last_10_games['estimatedTeamTurnoverPercentage'].mean(),
                       "turnoverRatio_L" + nb_games: df_last_10_games['turnoverRatio'].mean(),
                       "effectiveFieldGoalPercentage_L" + nb_games: df_last_10_games['effectiveFieldGoalPercentage'].mean(),
                       "trueShootingPercentage_L" + nb_games: df_last_10_games['trueShootingPercentage'].mean(),
                       "estimatedUsagePercentage_L" + nb_games: df_last_10_games['estimatedUsagePercentage'].mean(),
                       "estimatedPace_L" + nb_games: df_last_10_games['estimatedPace'].mean(),
                       "pace_L" + nb_games: df_last_10_games['pace'].mean(),
                       "pacePer40_L" + nb_games: df_last_10_games['pacePer40'].mean(),
                       "possessions_L" + nb_games: df_last_10_games['possessions'].mean(),
                       "PIE_L" + nb_games: df_last_10_games['PIE'].mean()}
            if index == 0 or team_stats['NB_VICTOIRE'][index - 1] + team_stats['NB_DEFAITE'][index - 1] == 82:
                new_row['DIFF_W'] = 0
            else:
                new_row['DIFF_W'] = team_stats['NB_VICTOIRE'][index - 1] - team_stats['NB_DEFAITE'][index - 1]
            df_stat_last_perf.loc[len(df_stat_last_perf)] = new_row
            index += 1

    df_stat_last_perf = pd.merge(df_stat_last_perf, df_game_info, on=['DUEL', 'GAME_DATE'])

    # Pour chaque match la différence de victoire en confrontation directe entre l'équipe à domicile et l'équipe à l'exterieur sur les 2 dernière années
    df_stat_last_perf['W_CONFR_D'] = np.nan
    df_stat_last_perf['GAME_DATE'] = pd.to_datetime(df_stat_last_perf['GAME_DATE'])
    for team in list(set(df_stat['teamId'].tolist())):
        game_list_one_year_before = df_stat_last_perf[df_stat_last_perf['teamId'] == team].reset_index()
        for index, game in game_list_one_year_before.iterrows():
            adv = game['DUEL'].split()[2]
            game_list_against_adv = game_list_one_year_before[
                (game_list_one_year_before['GAME_DATE'] < game['GAME_DATE']) & (
                            game_list_one_year_before['GAME_DATE'] > (game['GAME_DATE'] - pd.DateOffset(years=2))) & (
                    game_list_one_year_before['DUEL'].str.contains(adv))]
            df_stat_last_perf.loc[game['index'], 'W_CONFR_D'] = (game_list_against_adv['WL'] == "W").sum()

    df_stat_last_perf = df_stat_last_perf.sort_values(by='gameId')
    df_stat_last_perf.reset_index(drop=True, inplace=True)

    # Met les statistique de l'équipe à domicile avant celle à l'exterieur dans la dataset (certain ne le sont pas de base),
    # ce qui sera utile pour l'aplatissement du dataset
    for game_id in list(set(df_stat_last_perf['gameId'].tolist())):
        df_game = df_stat_last_perf[df_stat_last_perf['gameId'] == game_id]
        df_game.reset_index(inplace=True)
        if '@' in df_game['DUEL'].values[0]:
            df_stat_last_perf.loc[df_game['index'].values[0]] = df_game.loc[1]
            df_stat_last_perf.loc[df_game['index'].values[1]] = df_game.loc[0]
    return df_stat_last_perf

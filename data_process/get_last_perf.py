import numpy as np
import pandas as pd


def get_last_perf(df_stat):
    print('get_last_perf...')
    data_type = {"gameId": str, "teamId": str}
    #df_stat = pd.read_csv('../dataset/merged_team_stats.csv', dtype=data_type)
    nb_games = "10"

    df_game_info = df_stat[["TOTAL_POINTS", "DUEL", 'GAME_DATE']].copy()
    df_game_info.loc[:, 'teamName'] = df_stat['teamCity'] + " " + df_stat['teamName']

    df_stat_last_perf = pd.DataFrame(
        columns=['gameId', 'teamId', 'GAME_DATE', 'DUEL', 'WL', 'NB_WIN_L' + nb_games, 'PCT_TIR_REUSSI_L' + nb_games,
                 'PCT_3PTS_L' + nb_games,
                 'PCT_LANCER_FRANC_L' + nb_games, 'estimatedOffensiveRating_L' + nb_games,
                 'offensiveRating_L' + nb_games,
                 'estimatedDefensiveRating_L' + nb_games,
                 'defensiveRating_L' + nb_games, 'estimatedNetRating_L' + nb_games, 'netRating_L' + nb_games,
                 'assistPercentage_L' + nb_games,
                 'assistToTurnover_L' + nb_games, 'assistRatio_L' + nb_games,
                 'estimatedTeamTurnoverPercentage_L' + nb_games, 'turnoverRatio_L' + nb_games,
                 'effectiveFieldGoalPercentage_L' + nb_games, 'trueShootingPercentage_L' + nb_games,
                 'estimatedPace_L' + nb_games, 'pace_L' + nb_games,
                 'pacePer40_L' + nb_games, 'PIE_L' + nb_games])

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
                       "NB_WIN_L" + nb_games: (df_last_10_games['WL'] == 'W').sum() / int(nb_games),
                       "PCT_TIR_REUSSI_L" + nb_games: df_last_10_games['PCT_TIR_REUSSI'].mean(),
                       "PCT_3PTS_L" + nb_games: df_last_10_games['PCT_3PTS'].mean(),
                       "PCT_LANCER_FRANC_L" + nb_games: df_last_10_games['PCT_LANCER_FRANC'].mean(),
                       "estimatedOffensiveRating_L" + nb_games: df_last_10_games['estimatedOffensiveRating'].mean(),
                       "offensiveRating_L" + nb_games: df_last_10_games['offensiveRating'].mean(),
                       "estimatedDefensiveRating_L" + nb_games: df_last_10_games['estimatedDefensiveRating'].mean(),
                       "defensiveRating_L" + nb_games: df_last_10_games['defensiveRating'].mean(),
                       "estimatedNetRating_L" + nb_games: df_last_10_games['estimatedNetRating'].mean(),
                       "netRating_L" + nb_games: df_last_10_games['netRating'].mean(),
                       "assistPercentage_L" + nb_games: df_last_10_games['assistPercentage'].mean(),
                       "assistToTurnover_L" + nb_games: df_last_10_games['assistToTurnover'].mean(),
                       "assistRatio_L" + nb_games: df_last_10_games['assistRatio'].mean(),
                       "estimatedTeamTurnoverPercentage_L" + nb_games: df_last_10_games[
                           'estimatedTeamTurnoverPercentage'].mean(),
                       "turnoverRatio_L" + nb_games: df_last_10_games['turnoverRatio'].mean(),
                       "effectiveFieldGoalPercentage_L" + nb_games: df_last_10_games[
                           'effectiveFieldGoalPercentage'].mean(),
                       "trueShootingPercentage_L" + nb_games: df_last_10_games['trueShootingPercentage'].mean(),
                       "estimatedPace_L" + nb_games: df_last_10_games['estimatedPace'].mean(),
                       "pace_L" + nb_games: df_last_10_games['pace'].mean(),
                       "pacePer40_L" + nb_games: df_last_10_games['pacePer40'].mean(),
                       "PIE_L" + nb_games: df_last_10_games['PIE'].mean()}
            df_stat_last_perf.loc[len(df_stat_last_perf)] = new_row
            index += 1

    df_stat_last_perf = pd.merge(df_stat_last_perf, df_game_info, on=['DUEL', 'GAME_DATE'])

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

    for game_id in list(set(df_stat_last_perf['gameId'].tolist())):
        df_game = df_stat_last_perf[df_stat_last_perf['gameId'] == game_id]
        df_game.reset_index(inplace=True)
        if '@' in df_game['DUEL'].values[0]:
            df_stat_last_perf.loc[df_game['index'].values[0]] = df_game.loc[1]
            df_stat_last_perf.loc[df_game['index'].values[1]] = df_game.loc[0]
    return df_stat_last_perf

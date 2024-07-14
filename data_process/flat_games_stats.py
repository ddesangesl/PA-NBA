import pandas as pd

# Met les performances des équipe à domcile et des équipe à  l'exterieur sur la même ligne
def flat_games_stats(df_stat_last_perf):
    print("flat_games_stats...")
    nb_games = "10"

    data_type = {"gameId": str, "teamId": str, "W_CONFR_D": int}
    #df_stat_last_perf = pd.read_csv('../dataset/team_stat_last_' + nb_games + '.csv', dtype=data_type)

    # Fait la différence des statistique des 10 derniere performance de l'equipe a domicile et de l'eqipe a l'exterieur
    df_stat_last_perf['col'] = df_stat_last_perf.groupby('gameId').cumcount() + 1
    df_stat_flatten = df_stat_last_perf.pivot_table(index='gameId',
                                                    columns=df_stat_last_perf.groupby('gameId').cumcount() + 1,
                                                    values=['teamId', 'GAME_DATE', 'DUEL', 'WL', 'DIFF_W',
                                                            'NB_WIN_L' + nb_games, "POINTS_L" + nb_games,
                                                            'PCT_TIR_REUSSI_L' + nb_games, 'PCT_3PTS_L' + nb_games,
                                                            'PCT_LANCER_FRANC_L' + nb_games, "PASSE_D_L" + nb_games,
                                                            "REBOND_L" + nb_games, "REBOND_OFF_L" + nb_games,
                                                            "REBOND_DEF_L" + nb_games, "INTERCEPTION_L" + nb_games,
                                                            "TIR_CONTREE_L" + nb_games, "BALLON_PERDU_L" + nb_games,
                                                            "FAUTES_L" + nb_games,
                                                            'estimatedOffensiveRating_L' + nb_games,
                                                            'offensiveRating_L' + nb_games,
                                                            'estimatedDefensiveRating_L' + nb_games,
                                                            'defensiveRating_L' + nb_games,
                                                            'estimatedNetRating_L' + nb_games, 'netRating_L' + nb_games,
                                                            'assistPercentage_L' + nb_games,
                                                            'assistToTurnover_L' + nb_games, 'assistRatio_L' + nb_games,
                                                            'estimatedTeamTurnoverPercentage_L' + nb_games,
                                                            'turnoverRatio_L' + nb_games,
                                                            'effectiveFieldGoalPercentage_L' + nb_games,
                                                            'trueShootingPercentage_L' + nb_games,
                                                            'estimatedPace_L' + nb_games, 'pace_L' + nb_games,
                                                            'pacePer40_L' + nb_games, 'PIE_L' + nb_games,
                                                            "offensiveReboundPercentage_L" + nb_games,
                                                            "defensiveReboundPercentage_L" + nb_games,
                                                            "reboundPercentage_L" + nb_games,
                                                            "estimatedUsagePercentage_L" + nb_games,
                                                            "possesions_L" + nb_games, 'TOTAL_POINTS', 'teamName',
                                                            'W_CONFR_D'], aggfunc='first')

    df_stat_flatten.columns = [f'col{col[1]}' for col in df_stat_flatten.columns]

    df_stat_flatten = df_stat_flatten.reset_index()

    # Définition des nom des colonne du dataframe
    df_stat_flatten.columns = ['gameId',
                               'H_BALLON_PERDU_L' + nb_games, 'A_BALLON_PERDU_L' + nb_games,
                               'H_DIFF_W', 'A_DIFF_W',
                               'H_DUEL', 'A_DUEL',
                               'H_FAUTES_L' + nb_games, 'A_FAUTES_L' + nb_games,
                               'H_GAME_DATE', 'A_GAME_DATE',
                               'H_INTERCEPTIONS_L' + nb_games, 'A_INTERCEPTIONS_L' + nb_games,
                               'H_NB_WIN_L' + nb_games, 'A_NB_WIN_L' + nb_games,
                               'H_PASSE_D_L' + nb_games, 'A_PASSE_D_L' + nb_games,
                               'H_PCT_3PT_L' + nb_games, 'A_PCT_3PT_L' + nb_games, 'H_PCT_LANCER_FRANC_L' + nb_games,
                               'A_PCT_LANCER_FRANC_L' + nb_games, 'H_PCT_TIR_REUSSI_L' + nb_games,
                               'A_PCT_TIR_REUSSI_L' + nb_games, 'H_PIE_L' + nb_games, 'A_PIE_L' + nb_games,
                               'H_AVG_POINTS' + nb_games, 'A_AVG_POINTS' + nb_games,
                               'H_REBOND_DEF' + nb_games, 'A_REBOND_DEF' + nb_games,
                               'H_REBOND' + nb_games, 'A_REBOND' + nb_games,
                               'H_REBOND_OFF' + nb_games, 'A_REBOND_OFF' + nb_games,
                               'H_TIR_CONTREE' + nb_games, 'A_TIR_CONTREE' + nb_games,
                               'H_POINTS', 'A_POINTS', 'H_WL', 'A_WL', 'H_W_CONFR_D', 'A_W_CONFR_D',
                               'H_assistPercentage_L' + nb_games, 'A_assistPercentage_L' + nb_games,
                               'H_assistRatio_L' + nb_games, 'A_assistRatio_L' + nb_games,
                               'H_assistToTurnover_L' + nb_games, 'A_assistToTurnover_L' + nb_games,
                               'H_defensiveRating_L' + nb_games, 'A_defensiveRating_L' + nb_games,
                               'H_defensiveReboundPercentage_L' + nb_games, 'A_defensiveReboundPercentage_L' + nb_games,
                               'H_effectiveFieldGoalPercentage_L' + nb_games,
                               'A_effectiveFieldGoalPercentage_L' + nb_games, 'H_estimatedDefensiveRating_L' + nb_games,
                               'A_estimatedDefensiveRating_L' + nb_games, 'H_estimatedNetRating_L' + nb_games,
                               'A_estimatedNetRating_L' + nb_games, 'H_estimatedOffensiveRating_L' + nb_games,
                               'A_estimatedOffensiveRating_L' + nb_games, 'H_estimatedPace_L' + nb_games,
                               'A_estimatedPace_L' + nb_games, 'H_estimatedTeamTurnoverPercentage_L' + nb_games,
                               'A_estimatedTeamTurnoverPercentage_L' + nb_games,
                               'H_estimatedUsagePercentage_L' + nb_games, 'A_estimatedUsagePercentage_L' + nb_games,
                               'H_netRating_L' + nb_games, 'A_netRating_L' + nb_games, 'H_offensiveRating_L' + nb_games,
                               'A_offensiveRating_L' + nb_games,
                               'H_offensiveReboundPercentage_L' + nb_games, 'A_offensiveReboundPercentage_L' + nb_games,
                               'H_pacePer40_L' + nb_games, 'A_pacePer40_L' + nb_games, 'H_pace_L' + nb_games,
                               'A_pace_L' + nb_games,
                               'H_reboundPercentage_L' + nb_games, 'A_reboundPercentage_L' + nb_games,
                               'H_teamId', 'A_teamId', 'H_teamName', 'A_teamName',
                               'H_trueShootingPercentage_L' + nb_games, 'A_trueShootingPercentage_L' + nb_games,
                               'H_turnoverRatio_L' + nb_games, 'A_turnoverRatio_L' + nb_games]

    df_stat_flatten = df_stat_flatten.drop('A_DUEL', axis=1)
    df_stat_flatten = df_stat_flatten.drop('A_GAME_DATE', axis=1)
    df_stat_flatten = df_stat_flatten.drop('A_WL', axis=1)
    df_stat_flatten = df_stat_flatten.rename(columns={'H_DUEL': 'DUEL', 'H_GAME_DATE': 'GAME_DATE', 'H_WL': 'HOME_WON'})


    df_stat_flatten['HOME_WON'] = df_stat_flatten['HOME_WON'].replace('W', 1)
    df_stat_flatten['HOME_WON'] = df_stat_flatten['HOME_WON'].replace('L', 0)
    return df_stat_flatten

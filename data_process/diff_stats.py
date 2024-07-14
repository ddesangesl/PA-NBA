import pandas as pd


def diff_stats(df_stat_flatten):
    print("diff_stats...")
    nb_games = "10"

    # Rearange l'odre des colonnes
    new_order = ['gameId', 'DUEL', 'GAME_DATE', 'H_POINTS', 'A_POINTS', 'H_teamName', 'A_teamName', 'HOME_WON',
                 'H_DIFF_W', 'A_DIFF_W', 'H_ELO', 'A_ELO', 'H_ELO_PROB', 'A_ELO_PROB', 'H_BALLON_PERDU_L' + nb_games,
                 'A_BALLON_PERDU_L' + nb_games, 'H_AVG_POINTS' + nb_games, 'A_AVG_POINTS' + nb_games,
                 'H_INTERCEPTIONS_L' + nb_games, 'A_INTERCEPTIONS_L' + nb_games, 'H_W_CONFR_D', 'A_W_CONFR_D',
                 'H_NB_WIN_L' + nb_games, 'A_NB_WIN_L' + nb_games, 'H_PASSE_D_L' + nb_games, 'A_PASSE_D_L' + nb_games,
                 'H_PCT_3PT_L' + nb_games,
                 'A_PCT_3PT_L' + nb_games, 'H_PCT_LANCER_FRANC_L' + nb_games, 'A_PCT_LANCER_FRANC_L' + nb_games,
                 'H_REBOND_DEF' + nb_games, 'A_REBOND_DEF' + nb_games,

                 'H_REBOND' + nb_games, 'A_REBOND' + nb_games, 'H_REBOND_OFF' + nb_games, 'A_REBOND_OFF' + nb_games,
                 'H_TIR_CONTREE' + nb_games, 'A_TIR_CONTREE' + nb_games,
                 'H_PCT_TIR_REUSSI_L' + nb_games, 'A_PCT_TIR_REUSSI_L' + nb_games, 'H_PIE_L' + nb_games,
                 'A_PIE_L' + nb_games, 'H_assistPercentage_L' + nb_games,
                 'A_assistPercentage_L' + nb_games, 'H_assistRatio_L' + nb_games, 'A_assistRatio_L' + nb_games,
                 'H_assistToTurnover_L' + nb_games, 'A_assistToTurnover_L' + nb_games,
                 'H_defensiveRating_L' + nb_games, 'A_defensiveRating_L' + nb_games,
                 'H_effectiveFieldGoalPercentage_L' + nb_games,
                 'A_effectiveFieldGoalPercentage_L' + nb_games, 'H_defensiveReboundPercentage_L' + nb_games,
                 'A_defensiveReboundPercentage_L' + nb_games, 'H_estimatedDefensiveRating_L' + nb_games,
                 'A_estimatedDefensiveRating_L' + nb_games, 'H_estimatedNetRating_L' + nb_games,
                 'A_estimatedNetRating_L' + nb_games, 'H_estimatedOffensiveRating_L' + nb_games,
                 'A_estimatedOffensiveRating_L' + nb_games, 'H_estimatedPace_L' + nb_games,
                 'A_estimatedPace_L' + nb_games, 'H_estimatedTeamTurnoverPercentage_L' + nb_games,
                 'A_estimatedTeamTurnoverPercentage_L' + nb_games, 'H_netRating_L' + nb_games,
                 'A_netRating_L' + nb_games, 'H_offensiveRating_L' + nb_games, 'A_offensiveRating_L' + nb_games,
                 'H_reboundPercentage_L' + nb_games, 'A_reboundPercentage_L' + nb_games,
                 'H_estimatedUsagePercentage_L' + nb_games, 'A_estimatedUsagePercentage_L' + nb_games,
                 'H_pacePer40_L' + nb_games, 'A_pacePer40_L' + nb_games, 'H_pace_L' + nb_games, 'A_pace_L' + nb_games,
                 'H_offensiveReboundPercentage_L' + nb_games, 'A_offensiveReboundPercentage_L' + nb_games,
                 'H_teamId', 'A_teamId', 'H_trueShootingPercentage_L' + nb_games,
                 'A_trueShootingPercentage_L' + nb_games, 'H_turnoverRatio_L' + nb_games,
                 'A_turnoverRatio_L' + nb_games, 'team1']

    # Réorganise les colonnes
    df_stat_flatten = df_stat_flatten.reindex(columns=new_order)
    df_stat_flatten = df_stat_flatten.drop(columns=['team1'])

    #Supprime les ligne contanant des valeurs null
    df_stat_flatten = df_stat_flatten.dropna()

    df_stat_flatten = df_stat_flatten.drop(columns=['DUEL'])
    colonne_a_supprimer = df_stat_flatten.columns[7:].tolist()

    # Boucle sur chaque paire de colonnes (ex : H_POINTS et A_POINTS) pour calculer la différence
    i = 0
    for colonne in colonne_a_supprimer:

        if colonne != "H_teamId" and colonne != "A_teamId":
            # Extraire le préfixe de la colonne ('H_' ou 'A_')
            prefixe = colonne[0:2]
            # Extraire le nom de la colonne sans le préfixe
            nom_colonne = colonne[2:]
            # Créer une nouvelle colonne pour stocker la différence
            df_stat_flatten[f'{nom_colonne}'] = df_stat_flatten.apply(
                lambda row: row[f'H_{nom_colonne}'] - row[f'A_{nom_colonne}'], axis=1)
        i = i + 1
    colonne_a_supprimer.remove("A_teamId")
    colonne_a_supprimer.remove("H_teamId")
    df_stat_flatten = df_stat_flatten.drop(columns=colonne_a_supprimer)

    return df_stat_flatten

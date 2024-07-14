from nba_api.stats.endpoints import playergamelog
from nba_api.stats.endpoints import teamgamelog
from nba_api.stats.endpoints import boxscoreadvancedv3
import pandas as pd


# Extrait les stats des équipes et renvoie la dataframe des données
def get_df_player_stat(dict_player):
    # Définition de la grande dataframe qui sera retourner
    df_player_stat = pd.DataFrame()
    for player_id in dict_player: # Pour chaque joueurs
        for season in range(14, 25): # De la saison 2013-14 à la saison 2023-24
            # Extrait les stats de l'équipe sur une année
            stats_per_game = playergamelog.PlayerGameLog(player_id=player_id, season="200"+str(season - 1)+'-'+"0"+str(season))
            # Transformation des données en dataframe
            df_player_stat_temp = stats_per_game.get_data_frames()[0]
            # Ajout des données dans la grande dataframe
            df_player_stat = pd.concat([df_player_stat, df_player_stat_temp], ignore_index=True)
    return df_player_stat

# Extrait les stats des équipes et renvoie la dataframe des données
def get_df_team_stat(dict_team):
    # Définition de la grande dataframe qui sera retourné
    df_team_stat = pd.DataFrame()
    for team_id in dict_team: # Pour chaque équipe
        for season in range(11, 14): # De la saison 2013-14 à la saison 2023-24
            # Extrait les stats de l'équipe sur une année
            stats_team_per_game = teamgamelog.TeamGameLog(team_id=team_id, season="20"+str(season - 1)+'-'+str(season))
            # Transformation des données en dataframe
            df_team_stat_temp = stats_team_per_game.get_data_frames()[0]
            # Ajout des données dans la grande dataframe
            df_team_stat = pd.concat([df_team_stat, df_team_stat_temp], ignore_index=True)
    return df_team_stat

# Extrait les stats avancées des équipes et renvoie la dataframe des données
def get_df_team_adv_stats(list_game_id):
    df_team_adv_stat = pd.DataFrame()
    i = 0
    print(len(list_game_id))
    while i < len(list_game_id):
        avance = float("{:.2f}".format((i + 1) / len(list_game_id) * 100))
        print("Extraction :", avance, "%")
        adv_stats_game = boxscoreadvancedv3.BoxScoreAdvancedV3(list_game_id[i])
        df_game_adv_stat = adv_stats_game.get_data_frames()[1]
        df_team_adv_stat = pd.concat([df_team_adv_stat, df_game_adv_stat], ignore_index=True)
        i += 1
        df_team_adv_stat.to_csv("../dataset/team_adv_stat.csv", index=False)
    #df_team_adv_stat.to_csv("../dataset/team_adv_stat_temp.csv", index=False)


# Charger les fichiers CSV en dataframes
team_stat_df = pd.read_csv("../dataset/team_stat.csv", dtype={"Game_ID" : str})
team_adv_stat_df = pd.read_csv("../dataset/team_adv_stats.csv", dtype={"gameId" : str})

# Créer une liste de tous les game_id dans les deux dataframes
all_game_ids = set(team_stat_df['Game_ID']).union(set(team_adv_stat_df['gameId']))

# Créer une liste des game_id qui ne sont pas dans les deux dataframes
game_ids_not_in_both = []
for game_id in all_game_ids:
    if game_id not in team_stat_df['Game_ID'].values or game_id not in team_adv_stat_df['gameId'].values:
        game_ids_not_in_both.append(game_id)


df_team_adv_stats_team = get_df_team_adv_stats(game_ids_not_in_both)


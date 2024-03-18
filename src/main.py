from nba_api.stats.endpoints import playergamelog
from nba_api.stats.endpoints import teamgamelog
from nba_api.stats.endpoints import boxscoreadvancedv3
import pandas as pd


dict_player = {
    '203999' : "Jokic",
    '1966' : "Lebron",
    '3975' : "Curry",
    '201142' : "KD",
    '203507' : "Giannis",
    '203954' : "Embiid",
    '3992' : "Harden",
    '201566' : "Westbrook",
    '202331' : "PG",
    '1626164' : "Booker",
    '1626157' : "KAT",
    '203897' : "Lavine",
    '202691' : "Klay Thompson",
    "1628369" : "Jayson Tatum",
    "202710" : "Butler"
}

dict_team = {
    '1610612747' : "Lakers",
    '1610612744' : "Warriors",
    '1610612738' : "Celtics",
    '1610612739' : "Cavaliers",
    '1610612749' : "Bucks",
    '1610612752' : "Knicks",
    '1610612753' : "Magic",
    '1610612748' : "Heat",
    '1610612755' : "76ers",
    '1610612754' : "Pacers",
    '1610612741' : "Bulls",
    '1610612737' : "Hawks",
    '1610612751' : "Nets",
    '1610612761' : "Raptors",
    '1610612766' : "Hornets",
    '1610612765' : "Pistons",
    '1610612764' : "Wizards",
    '1610612760' : "Thunder",
    '1610612750' : "Wolves",
    '1610612743' : "Nuggets",
    '1610612746' : "Clippers",
    '1610612740' : "Pelicans",
    '1610612756' : "Suns",
    '1610612758' : "kings",
    '1610612742' : "Mavs",
    '1610612745' : "Rockets",
    '1610612762' : "Jazz",
    '1610612763' : "Grizzlies",
    '1610612757' : "Blazers",
    '1610612759' : "Spurs",
}

# Extrait les stats des équipes et renvoie la dataframe des données
def get_df_player_stat(dict_player):
    # Définition de la grande dataframe qui sera retourner
    df_player_stat = pd.DataFrame()
    for player_id in dict_player: # Pour chaque joueurs
        for season in range(14, 25): # De la saison 2013-14 à la saison 2023-24
            # Extrait les stats de l'équipe sur une année
            stats_per_game = playergamelog.PlayerGameLog(player_id=player_id, season="20"+str(season - 1)+'-'+str(season))
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
        for season in range(14, 25): # De la saison 2013-14 à la saison 2023-24
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
    while i < len(list_game_id):
        avance = float("{:.2f}".format(i + 1 / len(list_game_id) * 100))
        print("Extraction :", avance, "%")
        adv_stats_game = boxscoreadvancedv3.BoxScoreAdvancedV3(list_game_id[i])
        df_game_adv_stat = adv_stats_game.get_data_frames()[1]
        df_team_adv_stat = pd.concat([df_team_adv_stat, df_game_adv_stat], ignore_index=True)
        i += 1
    df_team_adv_stat.to_csv("11701 - 13000.csv", index=False)


#df_player_stat = get_df_player_stat(dict_player)
# Enregistrement des données dans le CSV
#df_player_stat.to_csv("player_stat.csv", index=False)

#df_team_stat = get_df_team_stat(dict_team)
# Enregistrement des données dans le CSV
#df_team_stat.to_csv("team_stat_celtic.csv", index=False)

#with open('list_game_id.txt', 'r') as f:
    # Lire chaque ligne du fichier et stocker dans une liste
#    liste = f.readlines()

# Supprimer les caractères de saut de ligne ("\n") de chaque élément de la liste
#list_game_id = [element.strip() for element in liste]

#df_team_adv_stats_team = get_df_team_adv_stats(list_game_id)
#df_team_adv_stats_team.to_csv("team_adv_stat.csv", index=False)


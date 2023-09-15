import pandas as pd
import numpy as np

ipl_matches = pd.read_csv('https://raw.githubusercontent.com/akashpagi/PANDAS-LIBRARY-FOR-DATA-SCIENCE/main/DATASETS/S17/IPL_Matches_2008_2022.csv')
ipl_matches.head()

def teamAPI():
    # Add Team1 and Team2 and convert into list
    teams = list(set(list(ipl_matches['Team1']) + list(ipl_matches['Team2'])))
    team_dict = {
        'teams': teams
    }
    return team_dict

def teamVsteamAPI(team1, team2):
    valid_teams = list(set(list(ipl_matches['Team1']) + list(ipl_matches['Team2'])))
    if team1 in valid_teams and team2 in valid_teams:
        temp_df = ipl_matches[(ipl_matches['Team1'] == team1) & (ipl_matches['Team2'] == team2) | (ipl_matches['Team1'] == team2) & (ipl_matches['Team2'] == team1)]
        total_matches = temp_df.shape[0]
        matches_won_team1 = temp_df['WinningTeam'].value_counts()[team1]
        matches_won_team2 = temp_df['WinningTeam'].value_counts()[team2]
        draws = total_matches - (matches_won_team1 + matches_won_team2)
        
        response = {
            'total_matches': str(total_matches),
            team1: str(matches_won_team1),
            team2: str(matches_won_team2),
            'no. of draws matches': str(draws),
        }
        return response
    else:
        return {'Meassage':'Invalid team names'}
    
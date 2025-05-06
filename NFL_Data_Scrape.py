import numpy as np
import pandas as pd
import random
import time
import lxml

# Create list of seasons to loop through
seasons = [str(season) for season in range(2014,2024)]
print(f"number of seasons = {len(seasons)}")

#Create the list of teams
teams = ['crd','atl', 'rav', 'buf', 'car', 'chi','cin', 'cle', 'dal', 'den', 'det', 'gnb', 'htx', 'clt', 'jax', 'kan',
         'sdg', 'ram', 'rai', 'mia', 'min', 'nwe', 'nor', 'nyg', 'nyj', 'phi', 'pit', 'sea', 'sfo', 'tam', 'oti', 'was']

print(f"Number of teams: {len(teams)}")

# Initialize Dataframe for looping
nfl_df = pd.DataFrame()

#Iterate through seasons
for season in seasons:
    #Iterate through teams
    for team in teams:
        #grab pro-football reference URL
        url = 'https://www.pro-football-reference.com/teams/' + team + '/' + season + '/gamelog/'
        print(url)

        #get offensive stats
        off_df = pd.read_html(url, header=1, attrs={'id':'gamelog' + season})[0]

        #get defensive stats
        def_df = pd.read_html(url, header=1, attrs={'id': 'gamelog_opp' + season})[0]

        #Concatenate offense defense data
        team_df = pd.concat([off_df,def_df], axis = 1)

        #Insert Season as new column
        team_df.insert(loc=0,column='Season', value = season)

        #Insert Team as new column
        team_df.insert(loc=2, column='Team', value =team.upper())

        #Concat team gamelog to the agg. dataframe
        nfl_df = pd.concat([nfl_df,team_df], ignore_index=True)

        #Pause to abide by website rules
        time.sleep(random.randint(7,8))

print(nfl_df)

#Save to CSV
nfl_df.to_csv('nfl_gamelogs_2014-2023.csv', index =False)






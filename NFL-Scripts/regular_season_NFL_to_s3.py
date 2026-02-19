import boto3
import numpy as np
import pandas as pd
import random
import time
import lxml
import html5lib 
import bs4
import io



## AWS Variables 
client = boto3.client('s3')
BUCKET_NAME = 'YOUR BUCKET NAME HERE'
PREFIX = 'PREFIX HERE FOR PARTIONING' 

## Initialize Looping -- Define the Amount of Seasons and The Teams to loop through 
seasons = [str(season) for season in range(2014,2025)]

teams = ['crd','atl', 'rav', 'buf', 'car', 'chi','cin', 'cle', 'dal', 'den', 'det', 'gnb', 'htx', 'clt', 'jax', 'kan',
         'sdg', 'ram', 'rai', 'mia', 'min', 'nwe', 'nor', 'nyg', 'nyj', 'phi', 'pit', 'sea', 'sfo', 'tam', 'oti', 'was']

##  Dictionary to assist in renaming columns 
rename_dict = {
    'Unnamed: 5': 'Home','Rslt': 'Win','Pts': 'Team_Pts','PtsO': 'Opp_Pts','Cmp': 'pCmp','Att': 'pAtt','Cmp%': 'pCmp%','Yds': 'pYds','TD': 'pTD','Y/A': 'pY/A','AY/A': 'pAY/A','Rate': 'pRate',
    'Yds.1': 'SkYds','Att.1': 'rAtt','Yds.2': 'rYds','TD.1': 'rTD','Y/A.1': 'rY/A','Yds.3': 'PntYds','Pass': 'fdPass','Rsh': 'fdRush','Pen': 'fdPen','Pen.1': 'Pen',
    'Yds.4': 'PenYds','ToP':'ToP_min'
}

## Define your functions 

#### This function will be used to clean the time of possession data 
def parse_top(top_str):
    try:
        parts = top_str.strip().split(":")
        if len(parts) == 3:
            # Format: MM:SS:00 — drop the last part
            top_str = f"{parts[0]}:{parts[1]}"
        return pd.to_timedelta("00:" + top_str).total_seconds() / 60  # "00:MM:SS"
    except:
        return None  # or np.nan

def clean_df(df):
    df = df.rename(columns=rename_dict)
    df = df[:-1]
    df['Home'] = df['Home'].apply(lambda x: 0 if x == '@' else 1)
    df['OT'] = df['OT'].apply(lambda x: 1 if x == 'OT' else 0)
    df['Win'] = df['Win'].apply(lambda x: 1 if x == 'W' else 0)
    df['ToP_min'] = df['ToP_min'].apply(parse_top)
    df['ToP_min'] = df['ToP_min'].astype(float)
    df['ToP_min'] = df['ToP_min'].round(2)
    df.insert(loc=0,column='Season', value = season)
    df.insert(loc=2, column='Team', value = team.upper())
    return df


#### Loop through the teams and seasons -- Save to your S3 Bucket

for season in seasons:
    #Iterate through teams
    for team in teams:
        # Print the team and season being processed
        print(f"Processing team: {team} for season: {season}")
       
        #grab pro-football reference URL
        url = 'https://www.pro-football-reference.com/teams/' + team + '/' + season + '/gamelog/'
        
        #Create DataFrame from HTML table
        # Use the table ID to find the correct table 
        table_id = "table_pfr_team-year_game-logs_team-year-regular-season-game-log"
        df = pd.read_html(url, header=1, attrs={'id':table_id})[0]

        #Clean the DataFrame
        df = clean_df(df)

        # Create CSV in string buffer
        csv_str_buffer = io.StringIO()
        df.to_csv(csv_str_buffer, index=False)

        # Convert to bytes
        csv_bytes_buffer = io.BytesIO(csv_str_buffer.getvalue().encode("utf-8"))
        csv_bytes_buffer.seek(0)

        # Upload to S3 
        client.upload_fileobj( csv_bytes_buffer, BUCKET_NAME, PREFIX + f'season={season} /team={team}/{season}_{team}_data.csv')
        
        # Print confirmation
        print(f"Uploaded team_{team}_{season}.csv to S3 bucket {BUCKET_NAME} with prefix {PREFIX}")

        # Sleep for a random time between 4 and 6 seconds to abide by the website's terms of service
        sleep_time = random.randint(4, 6)
        time.sleep(sleep_time)
        print(f"Paused for {sleep_time} seconds to respect website's terms of service.")

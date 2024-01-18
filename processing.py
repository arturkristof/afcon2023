import requests
import json
import pandas as pd
import numpy as np 
from itertools import groupby

DATA_FOLDER = './data/'
OUTPUT_FOLDER = './src/'
NAMES = ['Kwiatek', 'Filip', 'Komar', 'Artur', 'Mati', 'Plech', 'Lesiu', 'Komar jr']
SHEETS_FILE_KEY = "1ZOZOwm_V-b2YwLNAHaKKdIhfZ4oR5wiqfr699nv7amA"

def refresh_data(key: str, sheet: str, output_filename: str):
    path = DATA_FOLDER + output_filename
    
    response = requests.get(f'https://docs.google.com/spreadsheets/d/{key}/gviz/tq?tqx=out:csv&sheet={sheet}')
    assert response.status_code == 200, 'Wrong status code'
    
    with open(path, "wb") as file:   
        file.write(response.content)

def refresh_prediction_data():
    refresh_data(SHEETS_FILE_KEY, "Mecze", "typy.csv")

def refresh_standings_data():
    refresh_data(SHEETS_FILE_KEY, "Standings", "standings.csv")


def read_prediction_data():
    path = DATA_FOLDER + "typy.csv"
    typy_df = pd.read_csv(path, nrows=66)
    typy_df = typy_df[typy_df['Mati Points'].notnull()]
    return typy_df

def read_standings_data():
    path = DATA_FOLDER + "standings.csv"
    standings_df = pd.read_csv(path, nrows=3)
    standings_df = standings_df[['Rank', 'Striker', 'Goals']]
    
    return standings_df

def get_leaders(df: pd.DataFrame):
    results = df[[f"{name} Points" for name in NAMES]]
    results = results.set_axis(NAMES, axis=1)
    results = results.T
    results = results.iloc[:, 52]
    results = results.sort_values(ascending=False)

    res = []
    for x in results.index:
        res.append({'name': x, 'points': results[x]})
    return res

def get_longest_pizda_streak(points):
    lst = []
    for n,c in groupby(points):
       num,count = n,sum(1 for i in c)
       lst.append((num,count))

    streak = max([y for x,y in lst if x == 0])
    return streak

def get_pizda_streaks(df: pd.DataFrame):
    pizda_df = df.iloc[:-1]
    pizda_df["Date"] = pd.to_datetime(pizda_df["Date"], dayfirst=True)
    pizda_df = pizda_df[pizda_df["Date"] < np.datetime64('now') - np.timedelta64(2, 'h')]
    point_columns = [f'{name} Points' for name in NAMES]
    pizda_df = pizda_df[point_columns]
    pizda_streak_dict = {f"{name}" : get_longest_pizda_streak(pizda_df[f"{name} Points"]) for name in NAMES}

    return sorted_dict(pizda_streak_dict)

def get_games_data(df: pd.DataFrame):
    games_df = df.iloc[:-1]
    games_df["Date"] = pd.to_datetime(games_df["Date"], dayfirst=True)
    games_df = games_df[games_df["Date"] > np.datetime64('now') - np.timedelta64(3, 'h')]
    games_df = rename_cols(games_df)
    games_df['Date'] = games_df['Date'].astype(str)

    return list(games_df.T.to_dict().values())
    
def rename_cols(df: pd.DataFrame):
    return df.rename(columns={
        'Kwiatek Result': 'Kwiatek Home',
        'Unnamed: 8': 'Kwiatek Away',
        'Filip Result': 'Filip Home',
        'Unnamed: 11': 'Filip Away',
        'Komar Result': 'Komar Home',
        'Unnamed: 14': 'Komar Away',
        'Artur Result': 'Artur Home',
        'Unnamed: 17': 'Artur Away',
        'Mati Result': 'Mati Home',
        'Unnamed: 20': 'Mati Away',
        'Plech Result': 'Plech Home',
        'Unnamed: 23': 'Plech Away',
        'Lesiu Result': 'Lesiu Home',
        'Unnamed: 26': 'Lesiu Away',
        'Komar jr Result': 'Komar jr Home',
        'Unnamed: 29': 'Komar jr Away',
    })

def sorted_dict(d: dict, ascending=False):    
    res = pd.Series(d)
    res = res.sort_values(ascending=ascending)
    res = res.to_frame()
    res['points'] = res[0]
    res['name'] = res.index
    res = res[['name','points']]

    return list(res.T.to_dict().values())
    
def get_snipers(df):
    sniper_df = df.iloc[:-1]
    sniper_df["Date"] = pd.to_datetime(sniper_df["Date"], dayfirst=True)
    sniper_df = sniper_df[sniper_df["Date"] < np.datetime64('now') - np.timedelta64(2, 'h')]
    sniper_df = sniper_df[[f"{name} Points" for name in NAMES]]
    snipers_dict = {}
    snipers_dict = {f"{name}" : (sniper_df[f"{name} Points"].value_counts().get(3, 0) + sniper_df[f"{name} Points"].value_counts().get(4, 0)) for name in NAMES}
    
    return sorted_dict(snipers_dict)

def get_top_scorers(df):
    res = df.sort_values(by=['Rank'])
    res = res[['Striker', 'Goals']]
    res = res.rename(columns={'Striker': 'name', 'Goals': 'points'})
    return list(res.T.to_dict().values())


refresh_prediction_data()
data_df = read_prediction_data()
data_df = data_df.replace({np.nan: None})
db = {}

db['leaders'] = get_leaders(data_df)
db['pizda_streaks'] = get_pizda_streaks(data_df)
db['games'] = get_games_data(data_df)
db['snipers'] = get_snipers(data_df)

refresh_standings_data()
standings_df = read_standings_data()
db['top_scorers'] = get_top_scorers(standings_df)

with open(OUTPUT_FOLDER + "db.json", "w") as outfile: 
    json.dump(db, outfile)




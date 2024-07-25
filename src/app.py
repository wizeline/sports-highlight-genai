# app.py

from services.mlb_api import MLBAPI
from handlers.data_management import process_game_playbyplay_data, process_highlight_moments
from config import Config
from utils.file_export import save_to_csv, save_to_excel, save_to_json
import pandas as pd

def run_data_processing():
    api = MLBAPI(auth_key=Config.MLB_API_KEY)

    gamePk = 746133
    print("Fetching and processing game play-by-play data...")
    game_playbyplay_data = api.get_games_playbyplay(gamePk)
    processed_game_data = process_game_playbyplay_data(game_playbyplay_data)
    print("Processed Game Play-by-Play Data:")
    print(processed_game_data)

    if processed_game_data.empty:
        print("No game play-by-play data to save.")
    else:
        game_df = pd.DataFrame(processed_game_data)

        save_to_csv(game_df, 'game_playbyplay_data.csv')
        save_to_excel(game_df, 'game_playbyplay_data.xlsx')
        save_to_json(game_df, 'game_playbyplay_data.json')

    print("Processing highlight moments from the game play-by-play data...")
    highlight_moments_df = process_highlight_moments(game_playbyplay_data)
    print("Processed Highlight Moments Data:")
    print(highlight_moments_df)

    if highlight_moments_df.empty:
        print("No highlight moments data to save.")
    else:
        save_to_csv(highlight_moments_df, 'highlight_moments.csv')
        save_to_excel(highlight_moments_df, 'highlight_moments.xlsx')
        save_to_json(highlight_moments_df, 'highlight_moments.json')

if __name__ == '__main__':
    run_data_processing()

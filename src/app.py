from services.mlb_api import MLBAPI
from handlers.data_management import process_game_playbyplay_data
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

if __name__ == '__main__':
    run_data_processing()

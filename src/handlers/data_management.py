import pandas as pd
import json
import os

# Ensure output directory exists
output_dir = 'output_files'
os.makedirs(output_dir, exist_ok=True)

def load_json_data(filename):
    with open(filename) as f:
        return json.load(f)

def process_player_data(data):
    if 'body' in data:
        data = data['body']
    if not data or not isinstance(data, list):
        print("No player data or data is not in expected format.")
        return pd.DataFrame()

    df = pd.DataFrame(data)

    if 'active' in df.columns:
        filtered_df = df[df['active'] == True]
    else:
        print("Column 'active' not found in player data.")
        filtered_df = pd.DataFrame()

    return filtered_df

def process_game_playbyplay_data(data):
    if 'body' in data:
        data = data['body']
    if not data or not isinstance(data, list):
        print("No game play-by-play data or data is not in expected format.")
        return pd.DataFrame()

    df = pd.DataFrame(data)
    return df

def process_highlight_moments(data):
    if 'body' in data:
        games = data['body']
    else:
        print("No game data found.")
        return pd.DataFrame() 

    highlight_moments = []

    for game in games:
        result = game.get('result', {})
        about = game.get('about', {})

        game_event = {
            'description': result.get('description', ''),
            'startTime': about.get('startTime', ''),
            'endTime': about.get('endTime', ''),
            'captivating_index': about.get('captivatingIndex', 0),
        }

        # Process highlight moments
        if game_event['captivating_index'] > 30:
            highlight_moments.append(game_event)
            print(f"Added highlight moment: {game_event}")

    # Convert list of highlight moments to DataFrame
    df_highlight_moments = pd.DataFrame(highlight_moments)

    # Create separate DataFrames for description, startTime, and endTime
    df_description = df_highlight_moments[['description']]
    df_startTime = df_highlight_moments[['startTime']]
    df_endTime = df_highlight_moments[['endTime']]

    # Print and save the highlight moments DataFrame
    print("Highlight Moments DataFrame:")
    print(df_highlight_moments)

    # Save each DataFrame in multiple formats
    for df, name in zip([df_description, df_startTime, df_endTime], ['description', 'startTime', 'endTime']):
        print(f"Saving {name} data...")
        if not df.empty:
            df.to_csv(os.path.join(output_dir, f'{name}.csv'), index=False)
            df.to_excel(os.path.join(output_dir, f'{name}.xlsx'), index=False)
            df.to_json(os.path.join(output_dir, f'{name}.json'), orient='records', lines=True)
        else:
            print(f"No {name} data to save.")

    return df_highlight_moments

# Main function to run the processing
if __name__ == "__main__":
    # Load and process player data
    player_data = load_json_data('player_data.json')
    processed_player_data = process_player_data(player_data)
    print("Processed Player Data:")
    print(processed_player_data)

    # Load and process game play-by-play data
    game_playbyplay_data = load_json_data('game_playbyplay_data.json')
    processed_game_data = process_game_playbyplay_data(game_playbyplay_data)
    print("Processed Game Data:")
    print(processed_game_data)

    # Load and process highlight moments data
    highlight_moments_df = process_highlight_moments(game_playbyplay_data)
    print("Processed Highlight Moments Data:")
    print(highlight_moments_df)

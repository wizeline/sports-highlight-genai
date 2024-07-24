import pandas as pd
import json
import openpyxl

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

def process_data(data):

    if 'body' in data:
        games = data['body']
    else:
        print("No game data found.")
        return

    df_game_events = pd.DataFrame()
    df_pitch_data = pd.DataFrame()
    df_hit_data = pd.DataFrame()

    for game in games:
        result = game.get('result', {})
        about = game.get('about', {})
        play_events = game.get('playEvents', [])

        game_event = {
            'event_type': result.get('eventType', ''),
            'description': result.get('description', ''),
            'inning': about.get('inning', ''),
            'half_inning': about.get('halfInning', ''),
            'start_time': about.get('startTime', ''),
            'end_time': about.get('endTime', ''),
        }

        df_game_events = df_game_events.append(game_event, ignore_index=True)

        for play_event in play_events:
            pitch_data = play_event.get('pitchData', {})
            hit_data = play_event.get('hitData', {})

            pitch_event = {
                'pitch_start_speed': pitch_data.get('startSpeed', ''),
                'pitch_end_speed': pitch_data.get('endSpeed', ''),
                'pitch_type': pitch_data.get('type', {}).get('description', ''),
                'pitch_coordinates': pitch_data.get('coordinates', {}),
            }

            hit_event = {
                'hit_launch_angle': hit_data.get('launchAngle', ''),
                'hit_distance': hit_data.get('totalDistance', ''),
                'hit_trajectory': hit_data.get('trajectory', ''),
            }

            df_pitch_data = df_pitch_data.append(pitch_event, ignore_index=True)
            df_hit_data = df_hit_data.append(hit_event, ignore_index=True)

    df_game_events.to_csv('game_events.csv', index=False)
    df_pitch_data.to_csv('pitch_data.csv', index=False)
    df_hit_data.to_csv('hit_data.csv', index=False)

    df_game_events.to_excel('game_events.xlsx', index=False)
    df_pitch_data.to_excel('pitch_data.xlsx', index=False)
    df_hit_data.to_excel('hit_data.xlsx', index=False)

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

    # Load and process game events data
    game_events_data = load_json_data('data.json')
    process_data(game_events_data)

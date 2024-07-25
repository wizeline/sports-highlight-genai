# app.py

from services.mlb_api import MLBAPI
from handlers.data_management import process_game_playbyplay_data, process_highlight_moments
from handlers.manage_files_s3 import download_file,upload_file
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

def run_video_processing():
    
    print("Processing highlight moments from the game play-by-play data...")
    highlight_moments_df = process_highlight_moments(game_playbyplay_data)
    print("Processed Highlight Moments Data:")
    print(highlight_moments_df)

    if highlight_moments_df.empty:
        print("No highlight moments data to save.")
    else:
        download_file('wc-highlights-videostorage','matchvideo.mp4','video1.mp4')
        highlights=[highlight_moments_df[0],highlight_moments_df[1],hightlight_moments_def[2]]
        for index, highlight in enumerate.highlights:
            if(index<3)
                clipName='video'+index
            else    
                clipName='final'
            #convert timestamps to duration
            #gameStartTime for demo 2024-07-03T02:10:00Z
            gameStartTime="2024-07-03T02:10:00Z"
            eventStartTime=highlight[['startTime']]
            eventEndTime=highlight[['endTime']]
            dt1 = datetime.fromisoformat(gameStartTime.replace("Z", "+00:00"))
            dt2 = datetime.fromisoformat(eventStartTime.replace("Z", "+00:00"))
            dt3=datetime.fromisoformat(eventEndTime.replace("Z", "+00:00"))
            # Calculate the difference between the two datetime objects
            clipStartTime = dt2-dt1
            clipEndTime= dt3-dt1
            # Get the total elapsed seconds
            elapsed_seconds = time_difference.total_seconds()
            create_clip_from_video('video1.mp4',clipStarTime,clipEndTime,(clipName+'.mp4'))
            subtitles = [
                {'start_time': 0.0, 'end_time': (clipEndTime-clipStarTime), 'text': highlight[['description']]}],
            create_srt(subtitles,(clipName+'.srt'))
            uploadFile(clipName+'.srt')
            uploadFile(clipName+'.mp4')

        save_to_csv(highlight_moments_df, 'highlight_moments.csv')
        save_to_excel(highlight_moments_df, 'highlight_moments.xlsx')
        save_to_json(highlight_moments_df, 'highlight_moments.json')

if __name__ == '__main__':
    run_data_processing()

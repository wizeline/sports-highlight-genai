# src/app.py

from services.mlb_api import MLBAPI
from handlers.data_management import (
    process_player_data, process_free_agent_data, process_schedule_data,
    process_team_data, process_team_history_data, process_team_coaches_data,
    process_team_personnel_data, process_team_affiliates_data, process_team_roster_data
)
from config import Config

def run_data_processing():
    api = MLBAPI(auth_key=Config.MLB_API_KEY)
    
    # Process player data
    person_ids = [660271]  # Reemplaza con IDs de jugadores reales como una lista de enteros
    print("Fetching and processing player data...")
    player_data = api.get_players(person_ids)
    processed_player_data = process_player_data(player_data)
    print("Processed Player Data:")
    print(processed_player_data)

    # Process free agent data
    season_id = 2024  # Reemplaza con un ID de temporada real
    print("Fetching and processing free agent data...")
    free_agent_data = api.get_free_agents(season_id)
    processed_free_agent_data = process_free_agent_data(free_agent_data)
    print("Processed Free Agent Data:")
    print(processed_free_agent_data)

    # Process schedule data
    date = '2024-07-02'  # Reemplaza con una fecha real
    print("Fetching and processing schedule data...")
    schedule_data = api.get_schedule(date)
    processed_schedule_data = process_schedule_data(schedule_data)
    print("Processed Schedule Data:")
    print(processed_schedule_data)

    # Process team data
    team_id = 119  # Reemplaza con un ID de equipo real
    print("Fetching and processing team data...")
    team_data = api.get_teams(team_id)
    processed_team_data = process_team_data(team_data)
    print("Processed Team Data:")
    print(processed_team_data)

    # Process team history data
    team_ids = [119]  # Reemplaza con IDs de equipos reales como una lista de enteros
    print("Fetching and processing team history data...")
    team_history_data = api.get_teams_history(team_ids)
    processed_team_history_data = process_team_history_data(team_history_data)
    print("Processed Team History Data:")
    print(processed_team_history_data)

    # Process team coaches data
    print("Fetching and processing team coaches data...")
    team_coaches_data = api.get_teams_coaches(team_ids)
    processed_team_coaches_data = process_team_coaches_data(team_coaches_data)
    print("Processed Team Coaches Data:")
    print(processed_team_coaches_data)

    # Process team personnel data
    print("Fetching and processing team personnel data...")
    team_personnel_data = api.get_teams_personnel(team_ids)
    processed_team_personnel_data = process_team_personnel_data(team_personnel_data)
    print("Processed Team Personnel Data:")
    print(processed_team_personnel_data)

    # Process team affiliates data
    print("Fetching and processing team affiliates data...")
    team_affiliates_data = api.get_teams_affiliates(team_ids)
    processed_team_affiliates_data = process_team_affiliates_data(team_affiliates_data)
    print("Processed Team Affiliates Data:")
    print(processed_team_affiliates_data)

    # Process team roster data
    print("Fetching and processing team roster data...")
    team_roster_data = api.get_teams_roster(team_ids)
    processed_team_roster_data = process_team_roster_data(team_roster_data)
    print("Processed Team Roster Data:")
    print(processed_team_roster_data)

def run_video_processing():
    

if __name__ == '__main__':
    run_data_processing()

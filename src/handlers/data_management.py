import pandas as pd

def process_player_data(data):
    if 'players' in data:
        data = data['players']
    if not data or not isinstance(data, list):
        print("No player data or data is not in expected format.")
        return pd.DataFrame()  # Retorna un DataFrame vacío

    # Convert JSON data to DataFrame
    df = pd.DataFrame(data)
    
    if 'status' in df.columns:
        # Example of filtering data: select players with a specific attribute
        filtered_df = df[df['status'] == 'active']
    else:
        print("Column 'status' not found in player data.")
        filtered_df = pd.DataFrame()

    return filtered_df

def process_free_agent_data(data):
    if 'free_agents' in data:
        data = data['free_agents']
    if not data or not isinstance(data, list):
        print("No free agent data or data is not in expected format.")
        return pd.DataFrame()  # Retorna un DataFrame vacío

    df = pd.DataFrame(data)
    
    # Example of adding a new column
    if 'available_since' in df.columns:
        df['available_since'] = pd.to_datetime(df['available_since'])
    
    return df

def process_schedule_data(data):
    if 'schedule' in data:
        data = data['schedule']
    if not data or not isinstance(data, list):
        print("No schedule data or data is not in expected format.")
        return pd.DataFrame()  # Retorna un DataFrame vacío

    df = pd.DataFrame(data)
    
    # Example of sorting data by a specific column
    if 'game_date' in df.columns:
        df_sorted = df.sort_values(by='game_date')
    else:
        print("Column 'game_date' not found in schedule data.")
        df_sorted = df

    return df_sorted

def process_team_data(data):
    if 'teams' in data:
        data = data['teams']
    if not data or not isinstance(data, list):
        print("No team data or data is not in expected format.")
        return pd.DataFrame()  # Retorna un DataFrame vacío

    df = pd.DataFrame(data)
    
    # Example of handling missing values
    df.fillna('Unknown', inplace=True)
    return df

def process_team_history_data(data):
    if data is None:
        print("Received None for team history data.")
        return pd.DataFrame()  # Retorna un DataFrame vacío
    
    if 'team_history' in data:
        data = data['team_history']
    if not data or not isinstance(data, list):
        print("No team history data or data is not in expected format.")
        return pd.DataFrame()  # Retorna un DataFrame vacío

    df = pd.DataFrame(data)
    
    # Example of grouping data
    if {'year', 'wins', 'losses'}.issubset(df.columns):
        df_grouped = df.groupby('year').agg({'wins': 'sum', 'losses': 'sum'})
    else:
        print("Columns 'year', 'wins', or 'losses' not found in team history data.")
        df_grouped = pd.DataFrame()  # Retorna un DataFrame vacío si las columnas no están presentes

    return df_grouped

def process_team_coaches_data(data):
    if 'team_coaches' in data:
        data = data['team_coaches']
    if not data or not isinstance(data, list):
        print("No team coaches data or data is not in expected format.")
        return pd.DataFrame()  # Retorna un DataFrame vacío

    df = pd.DataFrame(data)
    
    # Example of merging with another DataFrame (uncomment and replace 'other_df' with actual DataFrame if needed)
    # other_df = pd.DataFrame()  # Replace this with actual DataFrame
    # df_merged = pd.merge(df, other_df, on='coach_id', how='left')
    
    return df

def process_team_personnel_data(data):
    if 'team_personnel' in data:
        data = data['team_personnel']
    if not data or not isinstance(data, list):
        print("No team personnel data or data is not in expected format.")
        return pd.DataFrame()  # Retorna un DataFrame vacío

    df = pd.DataFrame(data)
    
    # Example of filtering data by role
    if 'role' in df.columns:
        filtered_df = df[df['role'] == 'manager']
    else:
        print("Column 'role' not found in team personnel data.")
        filtered_df = pd.DataFrame()

    return filtered_df

def process_team_affiliates_data(data):
    if 'team_affiliates' in data:
        data = data['team_affiliates']
    if not data or not isinstance(data, list):
        print("No team affiliates data or data is not in expected format.")
        return pd.DataFrame()  # Retorna un DataFrame vacío

    df = pd.DataFrame(data)
    
    # Example of renaming columns
    df.rename(columns={'affiliation': 'affiliate_name'}, inplace=True)
    
    return df

def process_team_roster_data(data):
    if 'team_roster' in data:
        data = data['team_roster']
    if not data or not isinstance(data, list):
        print("No team roster data or data is not in expected format.")
        return pd.DataFrame()  # Retorna un DataFrame vacío

    df = pd.DataFrame(data)
    
    # Example of adding a new column
    df['roster_status'] = 'active'
    
    return df

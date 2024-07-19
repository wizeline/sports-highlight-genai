import requests

class MLBAPI:
    BASE_URL = 'https://apicalls.io/api/v1/mlb'
    
    def __init__(self, auth_key):
        self.auth_key = auth_key
        self.headers = {
            'Authorization': f'Bearer {self.auth_key}'
        }
        # Init caché for errores 404
        self.cache = {}

    def get_players(self, person_ids):
        url = f'{self.BASE_URL}/players'
        if isinstance(person_ids, list) and all(isinstance(pid, int) for pid in person_ids):
            person_ids_str = ','.join(str(pid) for pid in person_ids)
            params = {'personIds': person_ids_str}
            print(f"Params: {params}") 
        else:
            raise ValueError("person_ids debe ser una lista de enteros")
        
        response = requests.get(url, headers=self.headers, params=params)
        print(f"Response status code: {response.status_code}")
        print(f"Response content: {response.text}")
        return self._check_response(response)

    def get_free_agents(self, season_id):
        url = f'{self.BASE_URL}/free-agents'
        params = {'seasonId': str(int(season_id))}
        response = requests.get(url, headers=self.headers, params=params)
        return self._check_response(response)

    def get_schedule(self, date):
        url = f'{self.BASE_URL}/schedule'
        params = {'date': date}
        response = requests.get(url, headers=self.headers, params=params)
        return self._check_response(response)

    def get_teams(self, team_id):
        url = f'{self.BASE_URL}/teams'
        params = {'teamId': str(int(team_id))}
        response = requests.get(url, headers=self.headers, params=params)
        return self._check_response(response)

    def get_teams_history(self, team_ids):
        url = f'{self.BASE_URL}/teams/history'
        if isinstance(team_ids, list) and all(isinstance(tid, int) for tid in team_ids):
            team_ids_str = ','.join(str(tid) for tid in team_ids)
            params = {'teamIds': team_ids_str}
            print(f"Params: {params}")
        else:
            raise ValueError("team_ids debe ser una lista de enteros")
    
        response = requests.get(url, headers=self.headers, params=params)
        print(f"Response status code: {response.status_code}")
        print(f"Response content: {response.text}")
        return self._check_response(response)

    def get_teams_coaches(self, team_ids):
        url = f'{self.BASE_URL}/teams-coaches'
        if isinstance(team_ids, list) and all(isinstance(tid, int) for tid in team_ids):
            team_ids = ','.join(str(tid) for tid in team_ids)
        params = {'teamIds': team_ids}
        response = requests.get(url, headers=self.headers, params=params)
        return self._check_response(response)

    def get_teams_personnel(self, team_ids):
        url = f'{self.BASE_URL}/teams-personnel'
        if isinstance(team_ids, list) and all(isinstance(tid, int) for tid in team_ids):
            team_ids = ','.join(str(tid) for tid in team_ids)
        params = {'teamIds': team_ids}
        response = requests.get(url, headers=self.headers, params=params)
        return self._check_response(response)

    def get_teams_affiliates(self, team_ids):
        url = f'{self.BASE_URL}/teams-affiliates'
        if isinstance(team_ids, list) and all(isinstance(tid, int) for tid in team_ids):
            team_ids = ','.join(str(tid) for tid in team_ids)
        params = {'teamIds': team_ids}
        response = requests.get(url, headers=self.headers, params=params)
        return self._check_response(response)

    def get_teams_roster(self, team_ids):
        url = f'{self.BASE_URL}/teams-roster'
        if isinstance(team_ids, list) and all(isinstance(tid, int) for tid in team_ids):
            team_ids = ','.join(str(tid) for tid in team_ids)
        params = {'teamIds': team_ids}
        response = requests.get(url, headers=self.headers, params=params)
        return self._check_response(response)

    def _check_response(self, response):
        """Check the response status and handle errors."""
        if response.status_code == 200:
            try:
                response_json = response.json()
                if not response_json:
                    print("API returned an empty response.")
                return response_json
            except ValueError:
                print(f"API response is not valid JSON: {response.text}")
                return {}
        else:
            if response.status_code == 404:
                # Save the error 404 in caché
                self.cache[response.url] = '404 Not Found'
                print(f"API Error 404: Resource not found - URL: {response.url}")
                return None  
            else:
                print(f"API Error: {response.status_code} - {response.text}")
                response.raise_for_status()

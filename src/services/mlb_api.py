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

    def get_games_playbyplay(self, game_pk):
        if not isinstance(game_pk, int):
            raise ValueError("game_pk must be int")

        url = f'{self.BASE_URL}/games-playbyplay'
        params = {'gamePk': game_pk}
        print(f"Params: {params}")

        response = requests.get(url, headers=self.headers, params=params)
        print(f"Response status code: {response.status_code}")
        print(f"Response content: {response.text}")
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

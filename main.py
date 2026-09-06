import requests
from dotenv import load_dotenv
import os

load_dotenv()


class TMDB_Client():
    def __init__(self):
        self.session = requests.session()
        self.base_url = "https://api.themoviedb.org/3/"
        self.token = "Bearer " + os.environ.get("TMDB_TOKEN", "")

    def test_auth(self):
        return self.session.get(
            url="https://api.themoviedb.org/3/authentication",
            headers={
                "Authorization": self.token,
                "Accepted": "application/json"
            }
        )

    def _get_header(self):
        return {
                "Authorization": self.token,
                "Accepted": "application/json"
        }

    def get_movie_by_search_term(self, term: str):
        return self.session.get(
            self.base_url + f"search/movie?query={term}",
            headers=self._get_header()
        )


if __name__ == "__main__":
    client = TMDB_Client()
    response_json = client.get_movie_by_search_term("harry").json()
    results_list = list(response_json['results'])
    print("result -> ", dict(results_list[0])['title'])

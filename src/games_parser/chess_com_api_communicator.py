from datetime import datetime

from games_parser.api_communicator import ApiCommunicator
from games_parser.utils import get_time_class


class ChessComApiCommunicator(ApiCommunicator):
    HOST = "chess.com"
    API_URL = "https://api.chess.com/pub/"

    def get_games(self, username: str, games: int, time_class: str):
        list_of_games = self.__get_games(username, games, time_class)
        return super().games_generator(username, list_of_games)

    def __get_joined_year(self, usr: str) -> int:
        if not usr:
            self._logger.error("No username provided")
            return []
        url = f"{self.API_URL}player/{usr}"
        headers = {"Accept": "application/json"}
        response = self.send_query(url=url, headers=headers)
        joined = response.json()["joined"]
        year = datetime.fromtimestamp(joined).year
        return year

    def __get_chess_com_response(self, usr: str, y: int, m: int) -> list:
        url = f"{self.API_URL}player/{usr}/games/{y}/{m}/pgn"
        response = self.send_query(url)
        games = self.split_pgns(response.text)
        self._logger.debug(f"In {y}-{m} : {len(games)} games was played")
        return games

    def __get_games(self, usr: str, games_num: int, time_class: str) -> None:
        joined_year = self.__get_joined_year(usr)
        games = []
        for y in range(datetime.now().year, joined_year - 1, -1):
            if y == datetime.now().year:
                m = int(datetime.now().month)
            else:
                m = 12
            while m > 0:
                games_list = self.__get_chess_com_response(usr, y, m)

                for g in games_list:
                    if len(games) >= games_num:
                        return games
                    if get_time_class(g) == time_class:

                        games.append(g)
                m -= 1
        return games

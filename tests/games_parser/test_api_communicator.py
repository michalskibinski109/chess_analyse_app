from pathlib import Path

import pytest
from miskibin import get_logger

from games_parser.api_communicator import ApiCommunicator
from games_parser.game import Game


class TestApiCommunicator:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.logger = get_logger(lvl=10, logger_name="test_api_communicator")
        self.communicator = ApiCommunicator(self.logger)
        games_file = Path(__file__).parent / "validation_files" / "games.txt"
        with open(games_file) as file:
            self.games = file.read().split("\n\n\n")[:-1]

    def test_get_games(self):
        with pytest.raises(NotImplementedError):
            self.communicator.get_games("some name", 10, "blitz")

    def test_games_generator(self):
        generator = self.communicator.games_generator("some name", self.games)
        assert isinstance(next(generator), Game)

    def test__get_eco(self):
        assert self.communicator.eco != None

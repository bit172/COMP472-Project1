from strategy import Strategy
from typing import List, IO

from node import Node


class Context:

    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def find_solution(self, params: List, search_file: IO) -> Node:
        return self._strategy.find_solution(params, search_file)

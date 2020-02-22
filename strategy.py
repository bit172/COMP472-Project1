from abc import ABC, abstractmethod
from typing import List, IO

from node import Node


class Strategy(ABC):
    @abstractmethod
    def find_solution(self, params: List, search_file: IO) -> Node:
        pass

from robot.api.deco import library, keyword
from pathlib import Path
from datetime import timedelta
from decimal import Decimal
from typing import Literal
from enum import Enum, auto


class Direction(Enum):
    """Turn direction."""
    LEFT = auto()
    RIGHT = auto()

@library
class Library:
    
    @keyword
    def conversion(self, number: Decimal, path: Path, duration: timedelta):
        print(number * 2)
        print(path.name)
        print(duration.total_seconds())

    
    @keyword
    def move(self, direction: Literal['UP', 'DOWN', 'LEFT', 'RIGHT']):
        print(f'Moving {direction}')

    @keyword
    def turn(self, direction: Direction):
        if direction is Direction.LEFT:
            print('Turning left')
        else:
            print('Turning right')
        
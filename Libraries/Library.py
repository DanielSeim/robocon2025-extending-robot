from robot.api.deco import library, keyword
from pathlib import Path
from datetime import timedelta, date, datetime
from decimal import Decimal
from typing import Literal
from enum import Enum, auto
from robot.api.exceptions import ContinuableFailure, SkipExecution


class Direction(Enum):
    """Turn direction."""
    LEFT = auto()
    RIGHT = auto()

class EuroDate(date):
    """Date represented as dd.mm.yyyy."""

    @classmethod
    def from_string(cls, 
                    day: str) -> 'EuroDate':
        dt = datetime.strptime(day, '%d.%m.%Y')
        return cls(dt.year, dt.month, dt.day)

@library(scope='SUITE', 
         converters={EuroDate: EuroDate.from_string})
class Library:

    def __init__(self, state='INITIAL'):
        self.state = state

    @keyword
    def set_state(self, 
                  state: str):
        print(f'Old state was {self.state}.')
        self.state = state
        print(f'New state is {self.state}.')
    
    @keyword
    def conversion(self,
                    number: Decimal,
                    path: Path, 
                    duration: timedelta):
        print(number * 2)
        print(path.name)
        print(duration.total_seconds())

    
    @keyword
    def move(self, 
             direction: Literal['UP', 'DOWN', 'LEFT', 'RIGHT']):
        print(f'Moving {direction}')


    @keyword
    def turn(self, 
             direction: Direction):
        if direction is Direction.LEFT:
            print('Turning left')
        else:
            print('Turning right')
        

    @keyword
    def birthday(self, 
                 day: EuroDate):
        today = date.today()
        day = day.replace(year=today.year)
        difference = (day - today).days
        print(f"It's {difference} days to your birthday!")

    
    @keyword(name="🤖")
    def robot(self):
        print('🤖')


    @keyword('This is a "${kind}" example')
    def example(self, kind):
        print(kind)


    @keyword('Number of ${animals} is')
    def number_of_animals_is(self, animals, count: int):
        print(animals, count)


    @keyword
    def skip_me(self):
        raise SkipExecution('Some good reason...')
    

    @keyword
    def continuable_failure(self, message):
        raise ContinuableFailure(message)
    

    @keyword
    def html_error(self):
        raise AssertionError('*HTML* Something <b>bad</b> happened!')
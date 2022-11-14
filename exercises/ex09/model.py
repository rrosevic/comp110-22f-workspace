"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi, sqrt


__author__ = "730575822"


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)

    def distance(self, other: Point) -> float:
        """Calculate the distance between two cells."""
        distance: float = sqrt(((self.x - other.x) ** 2) + ((self.y - other.y) ** 2))
        return distance
    

class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    def tick(self) -> None:
        """Moves each cell to its next location, adds immunity to some after a recovery period."""
        self.location = self.location.add(self.direction)
        if self.is_infected():
            self.sickness += 1
        if self.sickness > constants.RECOVERY_PERIOD:
            self.immunize()
        return None

    def contract_disease(self) -> None:
        """Infects a cell."""
        self.sickness = constants.INFECTED
        return None

    def immunize(self) -> None:
        """Gives a cell immunity."""
        self.sickness = constants.IMMUNE
        return None

    def is_vulnerable(self) -> bool:
        """Declares when a cell is vulnerale (not sick or immunized)."""
        if self.sickness == constants.VULNERABLE:
            return True
        else:
            return False
    
    def is_infected(self) -> bool:
        """Declares when a cell is infected (not vulnerable or immunized)."""
        if self.sickness >= constants.INFECTED:
            return True
        else:
            return False

    def is_immune(self) -> bool:
        """Declares when a cell is immune (after being infected, after recovery period)."""
        if self.sickness == constants.IMMUNE:
            return True
        else:
            return False

    def color(self) -> str:
        """Return the color representation of a cell."""
        if self.is_vulnerable():
            return "gray"
        if self.is_infected():
            return "light pink"
        if self.is_immune():
            return "powder blue"
        
    def contact_with(self, other: Cell) -> None:
        """If a vulnerable and infected cell come into contact with each other, both are infected."""
        if self.is_infected() and other.is_vulnerable():
            other.contract_disease()
        if self.is_vulnerable() and other.is_infected():
            self.contract_disease()


class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, infected: int, immune: int = 0):
        """Initialize the cells with random locations and directions."""
        self.population = []
        if infected >= cells or infected <= 0:
            raise ValueError("Some Cell objects must begin infected.")
        if immune + infected >= cells or immune < 0:
            raise ValueError("Some Cell objects must begin immune.")
        for _ in range(cells - (infected + immune)):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            self.population.append(cell)
        for _ in range(infected):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            infected_cell: Cell = Cell(start_location, start_direction)
            infected_cell.contract_disease()
            self.population.append(infected_cell)
        for _ in range(immune):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            immune_cell: Cell = Cell(start_location, start_direction)
            immune_cell.immunize()
            self.population.append(immune_cell)

    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.direction.x *= -1.0
        if cell.location.x < constants.MIN_X:
            cell.direction.x *= -1.0
        if cell.location.y > constants.MAX_Y:
            cell.direction.y *= -1.0
        if cell.location.y < constants.MIN_Y:
            cell.direction.y *= -1.0

    def check_contacts(self) -> None:
        """Checks to see if two cells come into contact with one another."""
        for i in range(len(self.population)):
            for u in range(i + 1, len(self.population)):
                cell_one: Cell = self.population[i]
                cell_two: Cell = self.population[u]
                if cell_one.location.distance(cell_two.location) <= constants.CELL_RADIUS:
                    cell_one.contact_with(cell_two)

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        for cell in self.population:
            if cell.is_infected():
                return False
        return True
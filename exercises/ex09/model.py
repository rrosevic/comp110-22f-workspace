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
        distance: float = sqrt(((self.x + other.x)**2)+((self.y + other.y)**2))
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

    # Part 1) Define a method named `tick` with no parameters.
    # Its purpose is to reassign the object's location attribute
    # the result of adding the self object's location with its
    # direction. Hint: Look at the add method.
    def tick(self) -> None:
        self.location = self.location.add(self.direction)

    def contract_disease(self) -> None:
        self.sickness = constants.INFECTED

    def is_vulnerable(self) -> bool:
        if self.sickness == constants.VULNERABLE:
            return True
        else:
            return False
    
    def is_infected(self) -> bool:
        if self.sickness == constants.INFECTED:
            return True
        else:
            return False

    def color(self) -> str:
        """Return the color representation of a cell."""
        if self.is_vulnerable:
            return "gray"
        if self.is_infected:
            return "light pink"
        
    def contact_with(self, other: Cell) -> None:
        if self.is_infected and other.is_vulnerable:
            other.is_infected


class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, infected: int):
        """Initialize the cells with random locations and directions."""
        self.population = []
        if infected >= cells or infected <= 0:
            raise ValueError("Some Cell objects must begin infected.")
        for _ in range(cells - infected):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            self.population.append(cell)
        for _ in range(infected):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            infected_cell: Cell = Cell(start_location, start_direction)
            #Cell.color(Cell.contract_disease(infected_cell))
            self.population.append(infected_cell)
    
    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        Model.check_contacts(self)

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
        for _ in self.population:
            i: int = 0
            u: int = 1
            if Point.distance(self.population[i], self.population[u]) < constants.CELL_RADIUS:
                Cell.contact_with(self.population[i], self.population[u])
                u += 1
            i += 1

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        return False
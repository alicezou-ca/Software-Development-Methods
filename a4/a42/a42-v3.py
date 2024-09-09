#!/usr/bin/env python
"""Assignment 4 Part 2"""
print(__doc__)
import random

from typing import NamedTuple, Tuple, List

class PyArtConfig:
    """PyArtConfig class"""

    def __init__(self, x_range: Tuple[int, int] = (0, 500), 
                 y_range: Tuple[int, int] = (0, 300), 
                 radius_range: Tuple[int, int] = (0, 100), 
                 rx_range: Tuple[int, int] = (10, 30), 
                 ry_range: Tuple[int, int] = (10, 30),
                 width_range: Tuple[int, int] = (10, 100), 
                 height_range: Tuple[int, int] = (10, 100), 
                 color_range: Tuple[int, int] = (0, 255), 
                 opacity_range: Tuple[float, float] = (0.0, 1.0)):
        """__init__ method"""
        self.x_range = x_range
        self.y_range = y_range
        self.radius_range = radius_range
        self.rx_range = rx_range
        self.ry_range = ry_range
        self.width_range = width_range
        self.height_range = height_range
        self.color_range = color_range
        self.opacity_range = opacity_range

class RandomShape:
    """RandomShape class"""
    count: int = 0

    def __init__(self, config: PyArtConfig):
        """__init__ method"""
        RandomShape.count += 1
        self.shape_type = random.choice([0, 1, 3])  # 0: Circle, 1: Rectangle, 3: Ellipse
        self.x = random.randint(*config.x_range)
        self.y = random.randint(*config.y_range)
        self.radius = random.randint(*config.radius_range)
        self.rx = random.randint(*config.rx_range)
        self.ry = random.randint(*config.ry_range)
        self.width = random.randint(*config.width_range)
        self.height = random.randint(*config.height_range)
        self.red = random.randint(*config.color_range)
        self.green = random.randint(*config.color_range)
        self.blue = random.randint(*config.color_range)
        self.opacity = round(random.uniform(*config.opacity_range), 1)

    def __str__(self) -> str:
        """__str__() method"""
        return (f"Shape Type: {self.shape_type}\n"
                f"Position: ({self.x}, {self.y})\n"
                f"Radius: {self.radius}, Rx: {self.rx}, Ry: {self.ry}\n"
                f"Width: {self.width}, Height: {self.height}\n"
                f"Color: ({self.red}, {self.green}, {self.blue})\n"
                f"Opacity: {self.opacity}")

    def as_Part2_line(self) -> str:
        """as_Part2_line() method"""
        return (f"{self.shape_type:2d} {self.x:4d} {self.y:4d} {self.radius:4d} {self.rx:4d} {self.ry:4d} "
                f"{self.width:3d} {self.height:3d} {self.red:3d} {self.green:3d} {self.blue:3d} {self.opacity:.1f}")

    def as_svg(self) -> str:
        """as_svg() method"""
        if self.shape_type == 0:
            return f'<circle cx="{self.x}" cy="{self.y}" r="{self.radius}" fill="rgb({self.red}, {self.green}, {self.blue})" fill-opacity="{self.opacity}"></circle>'
        elif self.shape_type == 1:
            return f'<rect x="{self.x}" y="{self.y}" width="{self.width}" height="{self.height}" fill="rgb({self.red}, {self.green}, {self.blue})" fill-opacity="{self.opacity}"></rect>'
        elif self.shape_type == 2:
            return f'<ellipse cx="{self.x}" cy="{self.y}" rx="{self.rx}" ry="{self.ry}" fill="rgb({self.red}, {self.green}, {self.blue})" fill-opacity="{self.opacity}"></ellipse>'
        return ""

def generate_random_art_table(num_shapes: int, config: PyArtConfig) -> None:
    """generate_random_art_table() method"""
    shapes = [RandomShape(config) for _ in range(num_shapes)]
    print(f"{'CNT':3} {'SHA':3} {'X':4} {'Y':4} {'RAD':4} {'RX':4} {'RY':4} {'W':3} {'H':3} {'R':3} {'G':3} {'B':3} {'OP':2}")
    for i, shape in enumerate(shapes):
        print(f"{i:3d} {shape.as_Part2_line()}")

def main() -> None:
    """main() method"""
    config = PyArtConfig()
    rand = RandomShape(config)

    print("Table 1: Random numbers for 10 sample geometric shapes")
    generate_random_art_table(10, config)


if __name__ == "__main__":
    main()

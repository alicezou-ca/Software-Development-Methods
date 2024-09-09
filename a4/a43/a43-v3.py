#!/usr/bin/env python
"""Assignment 4 Part 3"""
print(__doc__)

import random
from typing import Tuple, List

class HtmlComponent:
    """HtmlComponent class"""
    def __init__(self):
        """__init__ method"""
        self.html_content = ""

    def add(self, content: str) -> None:
        """add() method"""
        self.html_content += content

    def render(self) -> str:
        """render() method"""
        return self.html_content

class HtmlDocument(HtmlComponent):
    """HtmlDocument class"""

    def __init__(self, title: str):
        """__init__ method"""
        super().__init__()
        self.title = title

    def write_header(self) -> None:
        """write_header() method"""
        self.add("<html>\n<head>\n")
        self.add(f"   <title>{self.title}</title>\n")
        self.add("</head>\n<body>\n")

    def write_footer(self) -> None:
        """write_footer() method"""
        self.add("</body>\n</html>\n")

class SvgCanvas:
    """SvgCanvas class"""

    def __init__(self, width: int, height: int):
        """__init__ method"""
        self.width = width
        self.height = height
        self.shapes = []

    def add_shape(self, shape: str) -> None:
        """add_shape() method"""
        self.shapes.append(shape)

    def render(self) -> str:
        """render() method"""
        content = '   <!--Define SVG drawing box-->\n'
        content += f'   <svg width="{self.width}" height="{self.height}">\n'
        for shape in self.shapes:
            content += f"      {shape}"
        content += '   </svg>\n'
        return content

class CircleShape:
    """CircleShape class"""

    def __init__(self, cx: int, cy: int, radius: int, color: Tuple[int, int, int], opacity: float):
        """__init__ method"""
        self.cx = cx
        self.cy = cy
        self.radius = radius
        self.color = color
        self.opacity = opacity

    def draw(self) -> str:
        """draw() method"""
        return f'<circle cx="{self.cx}" cy="{self.cy}" r="{self.radius}" fill="rgb({self.color[0]}, {self.color[1]}, {self.color[2]})" fill-opacity="{self.opacity}"></circle>\n'

class RectangleShape:
    """RectangleShape class"""

    def __init__(self, x: int, y: int, width: int, height: int, color: Tuple[int, int, int], opacity: float):
        """__init__ method"""
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.opacity = opacity

    def draw(self) -> str:
        """draw() method"""
        return f'<rect x="{self.x}" y="{self.y}" width="{self.width}" height="{self.height}" fill="rgb({self.color[0]}, {self.color[1]}, {self.color[2]})" fill-opacity="{self.opacity}"></rect>\n'

class EllipseShape:
    """EllipseShape class"""

    def __init__(self, cx: int, cy: int, rx: int, ry: int, color: Tuple[int, int, int], opacity: float):
        """__init__ method"""
        self.cx = cx
        self.cy = cy
        self.rx = rx
        self.ry = ry
        self.color = color
        self.opacity = opacity

    def draw(self) -> str:
        """draw() method"""
        return f'<ellipse cx="{self.cx}" cy="{self.cy}" rx="{self.rx}" ry="{self.ry}" fill="rgb({self.color[0]}, {self.color[1]}, {self.color[2]})" fill-opacity="{self.opacity}"></ellipse>\n'

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

    def draw(self) -> str:
        """draw() method"""
        if self.shape_type == 0:
            return CircleShape(self.x, self.y, self.radius, (self.red, self.green, self.blue), self.opacity).draw()
        elif self.shape_type == 1:
            return RectangleShape(self.x, self.y, self.width, self.height, (self.red, self.green, self.blue), self.opacity).draw()
        elif self.shape_type == 3:
            return EllipseShape(self.x, self.y, self.rx, self.ry, (self.red, self.green, self.blue), self.opacity).draw()
        return ""

class GreetingCard:
    """GreetingCard class"""

    def __init__(self, title: str, width: int, height: int, num_shapes: int, config: PyArtConfig):
        """__init__ method"""
        self.document = HtmlDocument(title)
        self.canvas = SvgCanvas(width, height)
        self.config = config
        self.num_shapes = num_shapes

    def generate_card(self):
        """generate_card() method"""
        self.document.write_header()
        for _ in range(self.num_shapes):
            shape = RandomShape(self.config)
            self.canvas.add_shape(shape.draw())
        self.document.add(self.canvas.render())
        self.document.write_footer()

    def save(self, filename: str) -> None:
        """save() method"""
        with open(filename, "w") as f:
            f.write(self.document.render())

def main() -> None:
    """main() method"""

    config_one = PyArtConfig()
    greeting_card = GreetingCard("First Insance", 500, 300, 1000, config_one)
    greeting_card.generate_card()
    greeting_card.save("a431.html")

    config_two = PyArtConfig(
        x_range=(0, 1000),  # X-coordinate range
        y_range=(0, 300),  # Y-coordinate range
        color_range=(0, 100),  # Color component range (0-100)
        opacity_range=(0.5, 1.0)  # Opacity range (0.5 to 1.0)
    )   
    greeting_card = GreetingCard("Second Insance", 1000, 300, 1500, config_two)
    greeting_card.generate_card()
    greeting_card.save("a432.html")

    config_3 = PyArtConfig(
        x_range=(250, 500),  # X-coordinate range
        y_range=(0, 300),  # Y-coordinate range
        color_range=(155, 255),  # Color component range (0-200)
        opacity_range=(0.5, 1.0)  # Opacity range (0.5 to 1.0)
    )
    greeting_card = GreetingCard("Third Insance", 500, 300, 1500, config_3)
    greeting_card.generate_card()
    greeting_card.save("a433.html")

if __name__ == "__main__":
    main()

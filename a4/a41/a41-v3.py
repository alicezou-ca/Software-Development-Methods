#!/usr/bin/env python
"""Assignment 4 Part 1"""
print(__doc__)

from typing import NamedTuple, Tuple, IO

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
    # Implementation similar to CircleShape but for rectangles
    pass

class EllipseShape:
    """EllipseShape class"""
    # Implementation similar to CircleShape but for ellipses
    pass

def main() -> None:
    """main() method"""
    doc = HtmlDocument("My Art")
    doc.write_header()

    canvas = SvgCanvas(500, 300)
    circles = [
        CircleShape(50, 50, 50, (255, 0, 0), 1.0),
        CircleShape(150, 50, 50, (255, 0, 0), 1.0),
        CircleShape(250, 50, 50, (255, 0, 0), 1.0),
        CircleShape(350, 50, 50, (255, 0, 0), 1.0),
        CircleShape(450, 50, 50, (255, 0, 0), 1.0),
        CircleShape(50, 250, 50, (0, 0, 255), 1.0),
        CircleShape(150, 250, 50, (0, 0, 255), 1.0),
        CircleShape(250, 250, 50, (0, 0, 255), 1.0),
        CircleShape(350, 250, 50, (0, 0, 255), 1.0),
        CircleShape(450, 250, 50, (0, 0, 255), 1.0)
    ]

    for circle in circles:
        canvas.add_shape(circle.draw())

    doc.add(canvas.render())
    doc.write_footer()

    with open("a41.html", "w") as f:
        f.write(doc.render())

if __name__ == "__main__":
    main()

from shape import Shape
from xyrange import XYRange


class ShapeCircle(Shape):
    def __init__(self):
        self.center_x = 0.0
        self.center_y = 0.0
        self.radius = 3.0

    def inside(self, x: float, y: float) -> bool:
        return (x - self.center_x) ** 2 + (y - self.center_y) ** 2 <= self.radius**2

    def get_range(self) -> XYRange:
        return XYRange(x1=-5.0, x2=5.0, xstep=0.25, y1=-5.0, y2=5.0, ystep=0.5)

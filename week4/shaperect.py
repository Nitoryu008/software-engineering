from shape import Shape
from xyrange import XYRange


class ShapeRect(Shape):
    def __init__(self):
        self.x_min = 1.0
        self.y_min = 1.0
        self.width = 5.0
        self.height = 3.0

    def inside(self, x: float, y: float) -> bool:
        return (
            self.x_min <= x <= self.x_min + self.width
            and self.y_min <= y <= self.y_min + self.height
        )

    def get_range(self) -> XYRange:
        return XYRange(x1=0.0, x2=8.0, xstep=0.25, y1=0.0, y2=5.0, ystep=0.5)

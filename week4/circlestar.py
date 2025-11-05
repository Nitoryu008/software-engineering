# week4/circlestar.py
from figure_template import FigureTemplate
from xyrange import XYRange


class CircleStar(FigureTemplate):
    def __init__(self):
        # 円の定義
        self.center_x, self.center_y, self.radius = 0.0, 0.0, 4.0

    def _get_range(self) -> XYRange:
        # 描画範囲とステップ
        return XYRange(x1=-5.0, x2=5.0, xstep=0.25, y1=-5.0, y2=5.0, ystep=0.5)

    def _inside(self, x: float, y: float) -> bool:
        # 座標が円の内側にあるか判定
        return (x - self.center_x) ** 2 + (y - self.center_y) ** 2 < self.radius**2

    def _plot_inside(self) -> None:
        # 円の内側には"★"
        print("★", end="")

    def _plot_outside(self) -> None:
        # 円の外側には".."
        print("..", end="")

    def _next_line(self) -> None:
        # yが1つ進むごとに2行改行
        print()  # 行の終端の改行
        print()  # 追加の改行


if __name__ == "__main__":
    CircleStar().draw()

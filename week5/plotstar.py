from plot import Plot


class PlotStar(Plot):
    def plot_inside(self) -> None:
        print("★", end="")

    def plot_outside(self) -> None:
        print("　", end="")

    def next_line(self) -> None:
        print()
        print()

from plot import Plot


class PlotDot(Plot):
    def plot_inside(self) -> None:
        print("*", end="")

    def plot_outside(self) -> None:
        print("_", end="")

    def next_line(self) -> None:
        print()

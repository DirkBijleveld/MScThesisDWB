from matplotlib.axes import Axes
from pandas import DataFrame
from matplotlib import pyplot as plt


def create_boxplot(
    frame: DataFrame,
    x: str,
    y: str,
    caption: str = "",
    ylabel: str = "",
    xlabel: str = "",
    outliers: bool = False,
    labels: list[str] = None,
    colors: list[str] = None,
    ymax: float = None,
    order: list[int] = None,
) -> Axes:
    boxes = frame.plot.box(
        column=y,
        by=x,
        showfliers=outliers,
        labels=labels,
        patch_artist=True,
        return_type="dict",
        positions=order,
    )
    box = boxes[0]
    if colors is not None:
        for patch, color in zip(box["boxes"], colors):
            patch.set_facecolor(color)

    for whisker in box["whiskers"]:
        whisker.set(color="black")

    for cap in box["caps"]:
        cap.set(color="black")

    for median in box["medians"]:
        median.set(color="black")

    # Enable gridlines on the Y axis
    plt.grid(axis="y")

    # Bound Y axis range
    if ymax is not None:
        plt.ylim(0, ymax)

    if ylabel != "":
        plt.ylabel(ylabel)
    if xlabel != "":
        plt.xlabel(xlabel)
    plt.title(caption)
    plt.tight_layout()
    return box

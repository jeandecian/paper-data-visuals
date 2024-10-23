import matplotlib.pyplot as plt
import pandas as pd


def plt_bar(data_file, x, height, color):
    data = pd.read_csv(f"data/{data_file}.csv")
    bars = plt.bar(data.get(x), data.get(height), color=color)

    for bar in bars:
        yval = bar.get_height()
        percentage = "{:.1%}".format(yval / data.get(height).sum())
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            yval,
            percentage,
            ha="center",
            va="bottom",
        )

    plt.xlabel(x)
    plt.ylabel(height)

    plt.savefig(f"out/{data_file}.png")

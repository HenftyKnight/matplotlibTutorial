# this cell was taken wholesale from the bqplot example
# bqplot is under the apache license, see their license file here:
# https://github.com/bqplot/bqplot/blob/55152feb645b523faccb97ea4083ca505f26f6a2/LICENSE
import ipywidgets as widgets
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from matplotlib.colors import TABLEAU_COLORS, XKCD_COLORS, to_rgba_array

import mpl_interactions.ipyplot as iplt
data = pd.read_json("nations.json")

def clean_data(data):
    for column in ["income", "lifeExpectancy", "population"]:
        data = data.drop(data[data[column].apply(len) <= 4].index)
    return data


def extrap_interp(data):
    data = np.array(data)
    x_range = np.arange(1800, 2009, 1.0)
    y_range = np.interp(x_range, data[:, 0], data[:, 1])
    return y_range


def extrap_data(data):
    for column in ["income", "lifeExpectancy", "population"]:
        data[column] = data[column].apply(extrap_interp)
    return data


data = clean_data(data)
data = extrap_data(data)
income_min, income_max = np.min(data["income"].apply(np.min)), np.max(data["income"].apply(np.max))
life_exp_min, life_exp_max = np.min(data["lifeExpectancy"].apply(np.min)), np.max(
    data["lifeExpectancy"].apply(np.max)
)
pop_min, pop_max = np.min(data["population"].apply(np.min)), np.max(
    data["population"].apply(np.max)
)

def x(year):
    return data["income"].apply(lambda x: x[year - 1800])


def y(x, year):
    return data["lifeExpectancy"].apply(lambda x: x[year - 1800])


def s(x, y, year):
    pop = data["population"].apply(lambda x: x[year - 1800])
    return 6000 * pop.values / pop_max


regions = data["region"].unique().tolist()
c = data["region"].apply(lambda x: list(TABLEAU_COLORS)[regions.index(x)]).values

fig, ax = plt.subplots(figsize=(10, 4.8))
controls = iplt.scatter(
    x,
    y,
    s=s,
    year=np.arange(1800, 2009),
    c=c,
    edgecolors="k",
    slider_formats="{:d}",
    play_buttons=True,
    play_button_pos="left",
)
fs = 15
ax.set_xscale("log")
ax.set_ylim([0, 100])
ax.set_xlim([200, income_max * 1.05])
ax.set_xlabel("Income", fontsize=fs)
_ = ax.set_ylabel("Life Expectancy", fontsize=fs)
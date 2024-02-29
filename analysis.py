import os

import numpy as np
import matplotlib.pyplot as plt


def load_data():
    path = 'results/ex1'

    # Load all csv files that start with desktop in their name
    desktop_files = [f for f in os.listdir(path) if f.startswith('desktop')]
    web_files = [f for f in os.listdir(path) if f.startswith('web')]

    # Load the data from the csv files
    desktop_data = [np.genfromtxt(f'{path}/{f}', delimiter=',', skip_header=1) for f in desktop_files]
    web_data = [np.genfromtxt(f'{path}/{f}', delimiter=',', skip_header=1) for f in web_files]
    desktop_power = extract_power(desktop_data)
    web_power = extract_power(web_data)
    return [desktop_power, web_power]


def extract_power(dataset):
    total_res = []
    for data in dataset:
        power = data[:, 18]
        delta = data[:, 0]
        res = 0
        for i in range(0, len(power)):
            res += power[i] * (delta[i] / 1_000)
        total_res.append(res)

    return total_res


def make_violin_plot(data_to_plot):
    # credit where credit is due: https://colab.research.google.com/drive/1DmFuBwhs9wI4_6zaaUh5B1rTiVt-hNt9?usp=sharing#scrollTo=yZiyYT_smhO0
    fig, ax = plt.subplots()

    # Create the violin plot
    violins = ax.violinplot(
        data_to_plot,
        showextrema=False)

    for pc in violins['bodies']:
        pc.set_facecolor('white')
        pc.set_edgecolor('black')
        pc.set_linewidth(0.6)
        pc.set_alpha(1)

    # Create the boxplot
    lineprops = dict(linewidth=0.5)
    medianprops = dict(color='black')
    ax.boxplot(
        data_to_plot,
        whiskerprops=lineprops,
        boxprops=lineprops,
        medianprops=medianprops)

    # Style
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.set_xticklabels(['Dekstop', 'Web'])
    ax.set_ylabel("Energy Consumption (J)")

    # Export
    fig.savefig("plots/violin_plot.svg")


data = load_data()
make_violin_plot(data)
print(data)

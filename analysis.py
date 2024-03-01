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
    return [desktop_data, web_data]


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


def make_time_series_plot(data):
    desktop_data = data[0]
    web_data = data[1]
    # create two plots under each other
    fig, ax = plt.subplots(2, 1)
    for data_set in desktop_data:
        ax[0].plot(data_set[:, 18])

    ax[0].set_title("Desktop")
    ax[0].set_ylabel("Power (W)")
    ax[0].set_xlabel("Time (s)")
    ax[0].xaxis.set_ticks(np.arange(0, 2001, 250))
    ax[0].xaxis.set_ticklabels(np.arange(0, 201, 25).round(1))

    # create more space between the two plots
    plt.subplots_adjust(hspace=0.5)
    for data_set in web_data:
        ax[1].plot(data_set[:, 18])
    ax[1].set_title("Web")
    ax[1].set_ylabel("Power (W)")
    ax[1].set_xlabel("Time (s)")
    ax[1].xaxis.set_ticks(np.arange(0, 2001, 250))
    ax[1].xaxis.set_ticklabels(np.arange(0, 201, 25).round(1))

    fig.savefig("plots/time_series.svg")


data = load_data()
desktop_power = extract_power(data[0])
web_power = extract_power(data[1])
average_desktop_power = sum(desktop_power) / len(desktop_power)
average_web_power = sum(web_power) / len(web_power)
print(f"Average desktop power: {average_desktop_power} J")
print(f"Average web power: {average_web_power} J")
make_violin_plot([desktop_power, web_power])

make_time_series_plot(data)


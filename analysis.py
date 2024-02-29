import numpy as np
import matplotlib.pyplot as plt

def load_data():
    desktop_data = np.genfromtxt('data/desktop_1_1.csv', delimiter=',', skip_header=1)
    web_data = np.genfromtxt('data/web_1_2.csv', delimiter=',', skip_header=1)
    desktop_power = extract_power(desktop_data)
    web_power = extract_power(web_data)
    return [desktop_power, web_power]

def extract_power(dataset):
    power = dataset[:, 18]
    delta = dataset[:, 0]
    res = 0
    for i in range(1, len(power)):
        res += power[i] * (delta[i] / 1_000)
    return res



def plot_data(data_to_plot):
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


    #Create the boxplot
    lineprops=dict(linewidth=0.5)
    medianprops=dict(color='black')
    ax.boxplot(
        data_to_plot,
        whiskerprops=lineprops,
        boxprops=lineprops,
        medianprops=medianprops)

    # Style
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.set_xticklabels(['Version A', 'Version B'])
    ax.set_ylabel("Energy Consumption (J)")

    # Export
    fig.savefig("normal_data.svg")



data = load_data()
print(data)


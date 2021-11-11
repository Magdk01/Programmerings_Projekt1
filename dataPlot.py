# dataPlot by Jonathan Simonsen (s201680)
import numpy as np
import matplotlib.pyplot as plt
from dataLoad import dataLoad


def dataPlot(data):

    # Create array containing only bacteria type
    BactOccur = data[::,2]

    # Number of occurrences of each bacteria
    num_one = (BactOccur == 1).sum()
    num_two = (BactOccur == 2).sum()
    num_three = (BactOccur == 3).sum()
    num_four = (BactOccur == 4).sum()

    # Function to add value labels on the bars
    def valuelabels(x,y):
        for i in range(len(x)):
            plt.text(i, y[i], y[i], ha = 'center', color = "r", weight = "bold")

    # Data to be plotted, types on the x-axis and occurrences on the y-axis
    x = ['Salmonella enterica', 'Bacillus cereus', 'Listeria', 'Brochothrix thermosphacta']
    y = [num_one, num_two, num_three, num_four]

    # Setting figure size
    plt.figure(figsize=(10, 5))

    # Creating the bar chart using the data
    plt.bar(x, y, color = 'navy', width = 0.4)

    # Adding labels to the x and y axes
    plt.xlabel("Bacteria type")
    plt.ylabel("Amount of specific bacteria type")

    # Adding a title to the plot
    plt.title("Number of bacteria", weight = "bold")

    # Calling the function to add the value labels to the bars
    valuelabels(x, y)
    plt.show()

    # Second plot
    # Sort the data by temperature in ascending order
    data = data[data[:, 0].argsort()]

    # Split data-matrix into separate matrices
    bact_one = np.array([x for x in data if x[2] == 1])
    bact_two = np.array([x for x in data if x[2] == 2])
    bact_three = np.array([x for x in data if x[2] == 3])
    bact_four = np.array([x for x in data if x[2] == 4])

    # Setting figure size
    plt.figure(figsize=(10, 7))

    # Bacteria type 1 points and plot
    # if statement ensures there is enough data for a line to be plotted
    if np.size(bact_one) >= 2:
        x1 = bact_one[::, 0]
        y1 = bact_one[::, 1]
        plt.plot(x1, y1, label="Salmonella enterica", color="crimson")

    # Bacteria type 2 points and plot
    if np.size(bact_two) >= 2:
        x2 = bact_two[::, 0]
        y2 = bact_two[::, 1]
        plt.plot(x2, y2, label="Bacillus cereus", color="orange")


    # Bacteria type 3 points and plot
    if np.size(bact_three) >= 2:
        x3 = bact_three[::, 0]
        y3 = bact_three[::, 1]
        plt.plot(x3, y3, label="Listeria", color="forestgreen")


    # Bacteria type 4 points and plot
    if np.size(bact_four) >= 2:
        x4 = bact_four[::, 0]
        y4 = bact_four[::, 1]
        plt.plot(x4, y4, label="Brochothrix thermosphacta", color="navy")


    # Axis labels and title of plot
    plt.xlabel("Temperature")
    plt.ylabel("Growth rate")
    plt.title("Growth rate by temperature", weight = "bold")

    # Set axes limits
    ax = plt.gca()
    ax.set_xlim(left=10, right=60)
    ax.set_ylim(bottom=0)

    # Add a grid to the plot
    plt.grid(True)

    # Show a legend on the plot
    plt.legend()
    plt.show()









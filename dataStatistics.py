# dataStatistics by Jacob Borregaard s181487

import numpy as np

def dataStatistics(data, statistics):

    type = statistics

    # Filters the hot and cold data by creating new lists
    cold_data = data[(data[::, 0] < 20)]
    hot_data = data[(data[::, 0] > 50)]

    # Calculates the mean growth rate of the hot and cold data
    # If statements ensures output if there is no hot or cold data
    if np.size(cold_data) == 0:
        meanColdGrowthRate = "There is no cold data"
    else:
        meanColdGrowthRate = np.mean(cold_data[::, 1])

    if np.size(hot_data) == 0:
        meanHotGrowthRate = "There is no hot data"
    else:
        meanHotGrowthRate = np.mean(hot_data[::, 1])

    # Takes input from main and returns the proper data statistic
    # Returns mean temperature
    if type == "1":
        results = "The mean temperature is", np.mean(data[::, 0])
    # Returns mean growth rate
    elif type == "2":
        results = "The mean growth rate is", np.mean(data[::, 1])
    # Returns standard deviation of temperature
    elif type == "3":
        results = "The standard deviation of the temperature is", np.std(data[::, 0])
    # Returns standard deviation of growth rate
    elif type == "4":
        results = "The standard deviation of the growth rate is", np.std(data[::, 1])
    # Returns the total number of rows in the data set
    elif type == "5":
        results = "The total number of rows in the data is", np.shape(data)[0]
    # Returns the mean growth rate of the cold data
    elif type == "6":
        results = "The mean cold growth rate is", meanColdGrowthRate
    # Returns the mean growth rate of the hot data
    elif type == "7":
        results = "The mean hot growth rate is", meanHotGrowthRate


    return results


import statistics

import numpy as np
from dataLoad import dataLoad
#data=dataLoad("test.txt")

def dataStatistics(data, statistics):

    results = data
    meanTemperature = np.mean(data[::,0])
    meanGrowthrate = np.mean(data[::,1])
    stdTemperature = np.std(data[::,0])
    stdGrowthrate = np.std(data[::,1])
    rows = np.shape(data)[0]

    type = input("Which statistic do you want?"
                 "Type 1 for mean temperature."
                 "Type 2 for mean Growth rate."
                 "Type 3 for std. temperature."
                 "Type 4 for std. growth rate."
                 "Type 5 for rows."
                 "Type 6 for mean cold growth rate."
                 "Type 7 for mean hot growth rate.")

    if type == "1":
        statistics = meanTemperature
    elif type == "2":
        statistics = meanGrowthrate
    elif type == "3":
        statistics = stdTemperature
    elif type == "4":
        statistics = stdGrowthrate
    elif type == "5":
        statistics = rows
    else:
        print("Wrong type of input")
    print(type)



    print(meanTemperature)
    print(meanGrowthrate)
    print(stdGrowthrate)
    print(stdTemperature)
    print(rows)


    return results

#print(dataStatistics(data, statistics))

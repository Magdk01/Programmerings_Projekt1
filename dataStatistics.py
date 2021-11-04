
import numpy as np
from dataLoad import dataLoad
data=dataLoad("test.txt")

def dataStatistics(data, Statistics):


    results = data
    middeltemperatur = np.mean(data[::,0])
    print(middeltemperatur)
    return results

print(dataStatistics(data,"statistics"))
print()
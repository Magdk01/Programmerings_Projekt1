# dataLoad.py by Magnus Vinjebo(s214588)
import numpy as np


# all in 1 solution
# mainMatrix = np.loadtxt(filename)

def dataLoad(filename):
    # Opens filename and converts each line into an array of strings each consisting of Temperature,
    # Growth rate, and Bacteria.
    workfile = open(filename)
    worklines = workfile.readlines()
    worktext = "".join(worklines)
    splittext = worktext.split("\n")
    mainArray = np.array(splittext)
    mainArray = np.delete(mainArray, np.where(mainArray == ''))

    # Init matricies with a empty upper row, and
    mainMatrix = np.zeros([1, 3])

    # Loop that splits each array into their 3 sub-elements and test's them against given conditions
    # and then either appends them to the main matrix or error matrix
    for n, i in enumerate(mainArray):
        splitarray = np.array(i.split(" "))
        temp = float(splitarray[0])
        grow_r = float(splitarray[1])
        bact = float(splitarray[2])
        try:
            if (temp >= 10 and temp < 60) and grow_r > 0 and (bact in {1, 2, 3, 4}):
                mainMatrix = np.vstack((mainMatrix, splitarray))
            else:
                print('Line: {}, had the following erroneous data:'.format((n + 1)))
                if (temp < 10 or temp > 60):
                    print('Temperature was: {}, which is out of the scope of 10-60'.format(temp))
                if grow_r < 0:
                    print('Growth rate was negative: {}'.format(grow_r))
                if bact not in {1, 2, 3, 4}:
                    print('Bacteria type was not recognised')
                print('\n')

        except ValueError:
            print('The .txt file you are trying to load, does not have the correct formatting.\nThe format should be '
                  'as following and seperated line by line with whitespaces:'
                  '\nTemperature, Growth rate, Bacteria type\n')

    # removes the upper row of matrices to only keep values. Also enforces float64 data type
    mainMatrix = np.delete(mainMatrix, 0, axis=0)
    mainMatrix = mainMatrix.astype('float64')
    data = mainMatrix
    return data;

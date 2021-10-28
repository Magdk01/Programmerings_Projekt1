#WIP Branch123
import numpy as np

# Splitting strings by chars
# def split(inp_string):
#     return [char for char in inp_string]

# all in 1 løsning
# mainMatrix = np.loadtxt(filename)

def dataLoad(filename):
    #Opens filename and converts each line into an array of strings each consisting of Temperature, Growth rate, and Bacteria.
    workfile = open(filename)
    worklines = workfile.readlines()
    worktext = "".join(worklines)
    splittext = worktext.split("\n")
    mainArray = np.array(splittext)
    mainArray = np.delete(mainArray, np.where(mainArray==''))

    #Init matricies with a empty upper row, and
    mainMatrix = np.zeros([1, 3])
    errorMatrix = np.zeros([1, 3])
    errorlist = []

    #Loop that splits each array into their 3 subelements and test's them against given conditions
    # and then either appends them to the main matrix or error matrix
    for n, i in enumerate(mainArray):
        splitarray = np.array(i.split(" "))
        temp = float(splitarray[0])
        grow_r = float(splitarray[1])
        bact = float(splitarray[2])

        if (temp >= 10 and temp < 60) and grow_r > 0 and (bact in {1,2,3,4}):
            mainMatrix = np.vstack((mainMatrix, splitarray))
        else:
            errorMatrix = np.vstack((errorMatrix, splitarray))
            errorlist.append(n+1)

    #removes the upper row of matrices to only keep vaulues
    mainMatrix = np.delete(mainMatrix, 0, axis=0 )
    errorMatrix = np.delete(errorMatrix, 0, axis=0)

    mainMatrix = mainMatrix.astype('float64')
    errorMatrix = errorMatrix.astype('float64')

    data = mainMatrix

    if np.size(errorMatrix) > 0:
        print('The given dataset contained the following erroneous data:\n')
        print(errorlist)
        print('\n')
        print(errorMatrix)
        keep_running = True
        while keep_running is True:
            go_on = (input('Do you wish to continue with the above data removed? (Y/N)\n')).lower()
            try:
                if (go_on == 'yes') or (go_on == 'y'):
                    keep_running = False
                elif go_on == 'no' or go_on == 'n':
                    data = np.zeros([1,3])
                    keep_running = False
                else:
                    print('\nPlease input either yes/y or no/n')
            except ValueError:
                print('Please input either yes/y or no/n')

    return data;



print(dataLoad('test.txt'))

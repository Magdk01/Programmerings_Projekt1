# dataLoad.py by Magnus Vinjebo(s214588)
import numpy as np

# all in 1 solution
# mainMatrix = np.loadtxt(filename)


def dataLoad(filename):
    # Opens filename and converts each line of the txt into an array of strings each consisting of Temperature,
    # Growth rate, and Bacteria.
    workfile = open(filename)
    worklines = workfile.readlines()
    worktext = "".join(worklines)
    splittext = worktext.split("\n")
    # main_array converts the string list and converts it to a numpy array
    main_array = np.array(splittext)
    # Removes removes empty indexes
    main_array = np.delete(main_array, np.where(main_array == ''))

    # Init matrix with a empty upper row, in dimensions matching the expected input of 3 columns
    main_matrix = np.zeros([1, 3])

    # Loop that splits each array into their 3 sub-elements and test's them against given conditions
    # and then either appends them to the main matrix by vstack
    for n, i in enumerate(main_array):
        splitarray = np.array(i.split(" "))
        temp = float(splitarray[0])
        grow_r = float(splitarray[1])
        bacteriatype = float(splitarray[2])
        try:
            if (10 <= temp < 60) and grow_r > 0 and (bacteriatype in {1, 2, 3, 4}):
                main_matrix = np.vstack((main_matrix, splitarray))

            # Sorts data with erroneous, and prints the reason why.
            else:
                print('Line: {}, had the following erroneous data:'.format((n + 1)))
                if temp < 10 or temp > 60:
                    print('Temperature was: {}, which is out of the scope of 10-60'.format(temp))
                if grow_r < 0:
                    print('Growth rate was negative: {}'.format(grow_r))
                if bacteriatype not in {1, 2, 3, 4}:
                    print('Bacteria type was not recognised')
                print('\n')

        except ValueError:
            print('The .txt file you are trying to load, does not have the correct formatting.\nThe format should be '
                  'as following and seperated line by line with whitespaces:'
                  '\nTemperature, Growth rate, Bacteria type\n')

    # Removes the upper row of matrices to only keep values. Also enforces float64 data type
    main_matrix = np.delete(main_matrix, 0, axis=0)
    main_matrix = main_matrix.astype('float64')

    # The main_matrix is then passed on to the return through the data variable. The format of the output matrix is
    # [N X 3],  where N = the amount of accepted data from the .txt file: "filename"
    data = main_matrix
    return data

# Script by Magnus Vinjebo(s214588)

import os
import numpy as np
from dataLoad import dataLoad
from dataPlot import dataPlot
from dataStatistics import dataStatistics

# Init variables
np.set_printoptions(suppress=True)
running = True
selection_loop = True
filename = ''
data = np.array([0])
lower = int()
upper = int()
main_selection = 0
bac_selec = np.zeros(4).astype(int)

# Overall loop, that keeps returning to the same start, till it gets quit
while running:
    print('Choose one of the following options: \n')
    print('1. Load data.\n2. Filter data.\n3. Display statistics.\n4. Generate plots.\n5. Quit.')

    # Primary loop to select 1 of 5 options for the data analysis
    while selection_loop is True:
        try:
            main_selection = input('Type one of the above numbers and press enter: \n').lower()
            if int(main_selection) in {1, 2, 3, 4, 5}:
                selection_loop = False
            else:
                print('{} is not an option from the list.\nPlease try again\n'.format(main_selection))
        except ValueError:
            print('{} is not an accepted input. Please try again\n'.format(main_selection))

    # resetting the loop variable
    selection_loop = True

    # 1 = DataLoad
    if int(main_selection) == 1:
        running_filename = True
        print('Insert the name of the .txt file you want to load:')
        while running_filename:
            try:
                filequery = input('').lower()

                # tests the input against the content of the dataFolder to look for a match
                for i in os.listdir():
                    if filequery == i:
                        filename = filequery
                        running_filename = False
                    elif filequery + '.txt' == i:
                        filename = filequery + '.txt'
                        running_filename = False
                if filename == '':
                    print('{} was not found in dataFolder.\nPlease try again.'.format(filequery))
            except ValueError:
                pass
        # Loads the data from the dataLoad function, with the filename from the script above, and stores it as a varible
        data = dataLoad(filename)
        # The matrix of data, is then copied so it can't get manipulated in the next steps,
        # and a new copy always can be made
        filter_data = np.copy(data)

    # 2 = FilterData
    elif int(main_selection) == 2:

        # checks if any data has been lodaded yet. Checking for <2 since a single proper matrix line should be of size 3
        if np.size(data) < 2:
            print('No data has been loaded yet, please do so first')
        elif np.size(data) >= 3:
            print('1. Add new growth rate filter\n2. Remove current growth filter \n3. Add new bacteria filter\n'
                  '4. Remove current bacteria filter\n ')
            print('Current filters:\n')

            # Prints current filters if there are any
            if (lower >= 0) and (upper > 0):
                print('Bacteria is filtered for growth rate in range: {} to {}'.format(lower, upper))
            if np.sum(bac_selec) > 0:
                print('Bacteria is filtered for types: {}'.format(bac_selec))
            filter_selection = input().lower()

            # Setting new ranges for growth rate
            if int(filter_selection) == 1:
                lower = -1
                upper = 0
                print('Setting ranges for filtering of growth rate:\n')

                # Setting the lower bound
                while lower < 0:
                    try:
                        lower = float(input('Lowest allowed growth rate:'))
                    except ValueError:
                        print('Must be a postive number')

                # Setting the upper bound
                while upper <= lower:
                    try:
                        upper = float(input('Highest allowed growth rate: '))
                        if upper < lower:
                            print('Upper bound must be higher than lower bound.\n'
                                  '{} is not higher than the lower bound of'
                                  ' {}\n'.format(upper, lower))
                    except ValueError:
                        print('Must be a postive number')

            # Resets parameters for growth rate
            if int(filter_selection) == 2:
                lower = 0
                upper = 0

            # Selection of allowed bacteria type
            if int(filter_selection) == 3:
                bacteria_selection = ''
                print('Input those bacteria you want to include, 1 at the time and press enter\n'
                      'When you are done input q or quit to save:\n\n'
                      'Bacteria 1: Salmonella enterica\n'
                      'Bacteria 2: Bacillus cereus\n'
                      'Bacteria 3: Listeria\n'
                      'Bacteria 4: Brochothrix thermosphacta\n')

                # Inits a loop that takes bacteria types to a array
                while bacteria_selection != 'q' and bac_selec[3] == 0:
                    print('Currently in selection: {}, {}, {}, {}'.format(bac_selec[0],
                                                                          bac_selec[1],
                                                                          bac_selec[2],
                                                                          bac_selec[3]))

                    # Not the best solution, but it takes the input and puts it in the next free space in the array
                    try:
                        bacteria_selection = input().lower()
                        if int(bacteria_selection) in {1, 2, 3, 4}:
                            if bac_selec[0] == 0:
                                bac_selec[0] = bacteria_selection
                            elif bac_selec[1] == 0:
                                bac_selec[1] = bacteria_selection
                            elif bac_selec[2] == 0:
                                bac_selec[2] = bacteria_selection
                            elif bac_selec[3] == 0:
                                bac_selec[3] = bacteria_selection
                        else:
                            print(
                                '{} is not a known bacteria.\nAvailable bacteria is 1,2,3,4'.format(bacteria_selection))
                    except ValueError:
                        if bacteria_selection != 'q':
                            print('The input is not recognised')
            # resets the bacteria selection to a array of 0's
            if int(filter_selection) == 4:
                bac_selec = np.zeros(4).astype(int)

        # Applies the filters to the matrix of data
        # First if is for if both filters are enabled:
        # The application itself is done by vectored parameters on the main matrix of data.
        # it is essentially just a lot of comparisons
        if (lower >= 0 and upper > 0) and (np.sum(bac_selec)) > 0:
            temp_data = data[(data[::, 2] == bac_selec[0])
                             | (data[::, 2] == bac_selec[1])
                             | (data[::, 2] == bac_selec[2])
                             | (data[::, 2] == bac_selec[3])]
            filter_data = temp_data[(temp_data[::, 1] > lower) & (temp_data[::, 1] < upper)]
        # This filter only applies for growth rate
        elif lower >= 0 and upper > 0:
            filter_data = data[(data[::, 1] > lower) & (data[::, 1] < upper)]
        # This filter only applies for types

        elif (np.sum(bac_selec)) > 0:
            filter_data = data[(data[::, 2] == bac_selec[0])
                               | (data[::, 2] == bac_selec[1])
                               | (data[::, 2] == bac_selec[2])
                               | (data[::, 2] == bac_selec[3])]

        # if there are no filters, it just makes a new copy of the data from dataLoad
        else:
            filter_data = np.copy(data)

    # 3 = Display statistics - By Jacob Borregaard (s181487)
    elif int(main_selection) == 3:
        if np.size(filter_data) < 2:
            print('No data has been loaded yet, please do so first')
        elif np.size(filter_data) >= 3:
            # Outputs a list of options for statistical analysis of the data
            print("Which statistic do you want?\n"
                  "Type 1 for mean temperature.\n"
                  "Type 2 for mean Growth rate.\n"
                  "Type 3 for std. temperature.\n"
                  "Type 4 for std. growth rate.\n"
                  "Type 5 for rows.\n"
                  "Type 6 for mean cold growth rate.\n"
                  "Type 7 for mean hot growth rate.\n"
                  " or type exit to return to main. \n")
            # initiates a loop that returns statistics of the data and checks for errors in the input.
            while True:
                statistics = input()
                if statistics in {"1", "2", "3", "4", "5", "6", "7"}:
                    stats = dataStatistics(filter_data, statistics)
                    print('{}: {}\n'.format(stats[0], round(stats[1], 3)))
                    break
                elif statistics == "exit":
                    break
                print("wrong input, try again")

    # 4 = Generate plots
    elif int(main_selection) == 4:
        if np.size(filter_data) < 2:
            print('No data has been loaded yet, please do so first')
        elif np.size(filter_data) >= 3:
            dataPlot(filter_data)

    # 5 = Quit
    elif int(main_selection) == 5:
        running = False

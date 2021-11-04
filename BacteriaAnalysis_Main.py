#WIP Branch123123123
import os
import numpy as np
from dataLoad import dataLoad
from dataPlot import dataPlot
from dataStatistics import dataStatistics
np.set_printoptions(suppress=True)

running = True
selection_loop = True
filename = ''
data = np.array([0])
lower = int()
upper = int()
main_selection = 0

#Overall loop, that keeps returning to the same start, till it gets quit
while running == True:
    #os.system('cls')
    print('Choose one of the following options: \n')
    print('1. Load data.\n2. Filter data.\n3. Display statistics.\n4. Generate plots.\n5. Quit.')
    #Primary loop to select 1 of 5 options for the data analysis
    while selection_loop is True:
        try:
            main_selection = input('Type one of the above numbers and press enter: \n')
            if int(main_selection) in {1, 2, 3, 4, 5}:
                selection_loop = False
            else:
                print('{} is not an option from the list.\nPlease try again\n'.format(main_selection))
        except ValueError:
            print('{} is not an accepted input. Please try again\n'.format(main_selection))
    #resetting the loop parameter
    selection_loop = True

    #1 = DataLoad
    if int(main_selection) == 1:
        running_filename = True
        print('Insert the name of the .txt file you want to load:')
        while running_filename == True:
            try:
                filequery = input('')
                #tests the input against the content of the dataFolder to look for a match
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
        data = dataLoad(filename)
        filter_data = np.copy(data)
    #2 = FilterData
    elif int(main_selection) == 2:
       #checks if any data has been lodaded yet. Checking for <2 since a single proper matrix line should be of size 3
        if np.size(data) < 2:
            os.system('cls')
            print('No data has been loaded yet, please do so first')
        elif np.size(data) >=3:
            os.system('cls')
            print('1. Add new growth rate filter\n2. Remove current growth filter \n3. Add new bacteria filter\n'
                  '4. Remove current bacteria filter\n ')
            print('Current filters:\n')
            if (lower > 0) and (upper > 0) :
                print('Bacteria is filtered in range: {} to {}'.format(lower, upper))
            filter_selection = input()

            if int(filter_selection) == 1:
                lower = -1
                upper = 0
                print('Setting ranges for filtering of growth rate:\n')
                while lower < 0:
                    try:
                        lower = float(input('Lowest allowed growth rate:'))
                    except ValueError:
                        print('Must be a postive number')
                while upper < lower:
                    try:
                        upper = float(input('Highest allowed growth rate: '))
                        if upper < lower:
                            print('Upper bound must be higher than lower bound.\n{} is not higher than the lower bound of'
                                  ' {}\n'.format(upper,lower))
                    except ValueError:
                        print('Must be a postive number')
            print('Upper = {} Lower = {}'.format(upper,lower))

            if int(filter_selection) == 2:
                lower = 0
                upper = 0
            if int(filter_selection) == 3:
                pass
            if int(filter_selection) == 4:
                pass
        if lower > 0 and upper > 0:
            filter_data = data[(data[::, 1] > lower) & (data[::, 1] < upper)]
        else:
            filter_data = np.copy(data)

        print(filter_data)
    #3 = Display statistics
    elif int(main_selection) == 3:
        if np.size(filter_data) < 2:
            os.system('cls')
            print('No data has been loaded yet, please do so first')
        elif np.size(filter_data) >=3:
            dataStatistics()
    #4 = Generate plots
    elif int(main_selection) == 4:
        if np.size(filter_data) < 2:
            os.system('cls')
            print('No data has been loaded yet, please do so first')
        elif np.size(filter_data) >=3:
            pass
           #dataPlot()
    #5 = Quit
    elif int(main_selection) == 5:
        running = False
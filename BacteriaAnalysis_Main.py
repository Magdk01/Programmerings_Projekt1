#WIP Branch123123123
import os
from dataLoad import dataLoad
from dataPlot import dataPlot
from dataStatistics import dataStatistics


running = True
selection_loop = True
filename = ''

#Overall loop, that keeps returning to the same start, till it gets quit
while running == True:
    os.system('cls')
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
    #resetting the loop Bool
    selection_loop = True
    #1 = DataLoad
    if int(main_selection) == 1:
        print('Insert the name of the .txt file you want to load:\n')
        while filename == '':
            try:
                filequery = input()
                #tests the input against the content of the dataFolder to look for a match
                for i in os.listdir("dataFolder/"):
                    if filequery == i:
                        filename = filequery
                    elif filequery + '.txt' == i:
                        filename = filequery + '.txt'
                if filename == '':
                    print('{} was not found in dataFolder.\nPlease try again.'.format(filequery))
            except ValueError:
                pass
    #2 = FilterData
    elif int(main_selection) == 2:
        pass
    #3 = Display statistics
    elif int(main_selection) == 3:
        pass
    #4 = Generate plots
    elif int(main_selection) == 4:
        pass
    #5 = Quit
    elif int(main_selection) == 5:
        running = False
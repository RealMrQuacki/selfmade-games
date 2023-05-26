import keyboard
import time
import os
import random
import copy


array = [[" " for x in range(21)] for y in range(21)] 

def printfield():
    os.system("cls")
    lines = []
    for row in array:
        lines.append(' '.join(str(x) for x in row))
    print('\n'.join(lines))


coordinatey = [10, 10, 10, 10, 10]
coordinatex = [11, 12, 13, 14, 15]

headcoordinatesy = 10
headcoordinatesx = 13

array[coordinatey[1]][coordinatex[1]] = "◼"
array[coordinatey[2]][coordinatex[2]] = "◼"
array[coordinatey[3]][coordinatex[3]] = "◼"
array[coordinatey[4]][coordinatex[4]] = "◼"

foodinteger = 0
addalevel = 0



while True:


    



    

    if foodinteger == 0:
        foodcoordinatey = random.randrange(1, 20)
        foodcoordinatex = random.randrange(1, 20)
        array[foodcoordinatey][foodcoordinatex] = "★"
        foodinteger = 1

    if headcoordinatesy == foodcoordinatey and headcoordinatesx == foodcoordinatex:
        foodinteger = 0

    if headcoordinatesx == foodcoordinatex and headcoordinatesy == foodcoordinatey:
        addalevel = 1

    if keyboard.is_pressed('left'):
        headcoordinatesy -= 0
        headcoordinatesx -= 1 
        coordinatey.append(headcoordinatesy)
        coordinatex.append(headcoordinatesx)
        if addalevel == 1:
            addalevel = 0
        else:
            coordinatey.pop(0)
            coordinatex.pop(0)
            array[coordinatey[0]][coordinatex[0]] = " "
        last_elementy = coordinatey[-1]
        last_elementx = coordinatex[-1]
        array[last_elementy][last_elementx] = "◼"
        printfield()
        time.sleep(0.1)

    if keyboard.is_pressed('right'):
        if addalevel == 1:
            addalevel = 0
            headcoordinatesy -= 0
            headcoordinatesx += 1 
            coordinatey.append(headcoordinatesy)
            coordinatex.append(headcoordinatesx)
            last_elementy = coordinatey[-1]
            last_elementx = coordinatex[-1]
            array[last_elementy][last_elementx] = "◼"
            printfield()
            time.sleep(0.1)
        else:
            headcoordinatesy -= 0
            headcoordinatesx += 1 
            coordinatey.append(headcoordinatesy)
            coordinatex.append(headcoordinatesx)
            coordinatey.pop(0)
            coordinatex.pop(0)
            array[coordinatey[0]][coordinatex[0]] = " "
            last_elementy = coordinatey[-1]
            last_elementx = coordinatex[-1]
            array[last_elementy][last_elementx] = "◼"
            printfield()
            time.sleep(0.1)

    if keyboard.is_pressed('down'):
        if addalevel == 1:
            addalevel = 0
            headcoordinatesy += 1
            headcoordinatesx -= 0
            coordinatey.append(headcoordinatesy)
            coordinatex.append(headcoordinatesx)
            last_elementy = coordinatey[-1]
            last_elementx = coordinatex[-1]
            array[last_elementy][last_elementx] = "◼"
            printfield()
            time.sleep(0.1)
        else:
            headcoordinatesy += 1
            headcoordinatesx -= 0 
            coordinatey.append(headcoordinatesy)
            coordinatex.append(headcoordinatesx)
            coordinatey.pop(0)
            coordinatex.pop(0)
            array[coordinatey[0]][coordinatex[0]] = " "
            last_elementy = coordinatey[-1]
            last_elementx = coordinatex[-1]
            array[last_elementy][last_elementx] = "◼"
            printfield()
            time.sleep(0.1)

    if keyboard.is_pressed('up'):
        if addalevel == 1:
            addalevel = 0
            headcoordinatesy -= 1
            headcoordinatesx -= 0
            coordinatey.append(headcoordinatesy)
            coordinatex.append(headcoordinatesx)
            last_elementy = coordinatey[-1]
            last_elementx = coordinatex[-1]
            array[last_elementy][last_elementx] = "◼"
            printfield()
            time.sleep(0.1)
        else:
            headcoordinatesy -= 1
            headcoordinatesx -= 0 
            coordinatey.append(headcoordinatesy)
            coordinatex.append(headcoordinatesx)
            coordinatey.pop(0)
            coordinatex.pop(0)
            array[coordinatey[0]][coordinatex[0]] = " "
            last_elementy = coordinatey[-1]
            last_elementx = coordinatex[-1]
            array[last_elementy][last_elementx] = "◼"
            printfield()
            time.sleep(0.1)


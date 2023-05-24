import time
import sys
import os
import copy
import pygame


# Fenstergröße
window_width = 400
window_height = 400

# Array-Erstellung
array = [[0 for x in range(40)] for y in range(40)]

# Farben
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Pygame-Initialisierung
pygame.init()

# Fenstererstellung und Titelfestlegung
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Please click on the fields that should be activated.")

# Funktion zum Aktualisieren des Fensters
def update_window():
    # Fenster leeren
    window.fill(BLACK)

    # Array visualisieren
    pixel_size = window_width // len(array[0])
    for y in range(len(array)):
        for x in range(len(array[y])):
            if array[y][x] == 1:
                pygame.draw.rect(window, WHITE, (x * pixel_size, y * pixel_size, pixel_size, pixel_size))

    # Fenster aktualisieren
    pygame.display.update()

# Funktion zum Umschalten der Werte im Array und im Fenster
def toggle_value(x, y):
    if array[y][x] == 0:
        array[y][x] = 1
    else:
        array[y][x] = 0

# Hauptprogrammschleife
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Linke Maustaste
                # Position des Mausklicks erhalten
                x, y = event.pos
                # Array-Index basierend auf der Mausposition berechnen
                index_x = x // (window_width // len(array[0]))
                index_y = y // (window_height // len(array))
                # Wert im Array umschalten
                toggle_value(index_x, index_y)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Alle Werte im Fenster auf das Array übertragen
                for y in range(len(array)):
                    for x in range(len(array[y])):
                        if window.get_at((x, y)) == WHITE:
                            array[y][x] = 1
                        else:
                            array[y][x] = 0

    # Fenster aktualisieren
    update_window()














































# Fenstergröße
window_width = 400
window_height = 400

#Array for displaying actual Playfield
#array = [[0 for x in range(40)] for y in range(100)]

#Array that gets updated is the process of a generation
array2 = [[0 for x in range(40)] for y in range(100)]


# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Pygame initialisieren
pygame.init()

# Fenster erstellen
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("GameOfLife - Mark")


# Function to handle events
def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

# Funktion zum Aktualisieren des Fensters
def update_window():
    # Hintergrund zeichnen
    window.fill(BLACK)

    # Array visualisieren
    pixel_size = window_width // len(array[0])
    for y in range(len(array)):
        for x in range(len(array[y])):
            if array[y][x] == 1:
                pygame.draw.rect(window, WHITE, (x * pixel_size, y * pixel_size, pixel_size, pixel_size))

    # Fenster aktualisieren
    pygame.display.update()

#Draws a spaceship on the field Array
#array[2][2] = 1
#array[2][3] = 1
#array[2][4] = 1


#Defindes the first field that is being checked
rowtobecheckedy = 1
rowtobecheckedx = 1


for i in range(99999999999):

    # Handle events
    handle_events()

    # Update the window
    update_window()


    #Checks if rowtobecheckedx is 19 and if yes sets rowtobecheked x to 1 and y+1
    if rowtobecheckedx == 39:
        rowtobecheckedx = 1
        rowtobecheckedy = rowtobecheckedy + 1

    if rowtobecheckedx  == 36:

        if rowtobecheckedy == 36:

            #Clears console
            os.system("cls")
    
            #Sets array2 to same save as array
            array = copy.deepcopy(array2)

            #Rowtobecked axis back to 1
            rowtobecheckedx = 1
            rowtobecheckedy = 1
            
            update_window()

            time.sleep(0.15)


            

    #Counts how many living cells are next to main cell
    counter = 0

    #Calculating Step 1
    counter += array[rowtobecheckedx-1][rowtobecheckedy-1]
    
    
    #Calculating Step 2
    counter += array[rowtobecheckedx-0][rowtobecheckedy-1]


    #Calculating Step 2
    counter += array[rowtobecheckedx+1][rowtobecheckedy-1]
    
    #Calculating Step 4
    counter += array[rowtobecheckedx-1][rowtobecheckedy-0]
    
    
    #Calculating Step 5
    counter += array[rowtobecheckedx+1][rowtobecheckedy+0]
    
    
    #Calculating Step 6
    counter += array[rowtobecheckedx-1][rowtobecheckedy+1]
    
    
    #Calculating Step 7
    counter += array[rowtobecheckedx-0][rowtobecheckedy+1]
    
    
    #Calculating Step 8
    counter += array[rowtobecheckedx+1][rowtobecheckedy+1]


    #One or less = death
    if counter == 1 or counter == 0:
        (array2[rowtobecheckedx][rowtobecheckedy]) = 0
    
    #Four or more = death
    if counter == 4 or counter == 5 or counter == 6 or counter == 7 or counter == 8:
        (array2[rowtobecheckedx][rowtobecheckedy]) = 0

    #Two neighbours = survive
    if array[rowtobecheckedx][rowtobecheckedy] == 1 and counter == 2:
        array2[rowtobecheckedx][rowtobecheckedy] = array[rowtobecheckedx][rowtobecheckedy]
    
    #Three neighbours = newborn or survive
    if counter == 3:
        (array2[rowtobecheckedx][rowtobecheckedy]) = 1


    #Adds 1 to the rowtobechecked x axis
    rowtobecheckedx = rowtobecheckedx + 1




    


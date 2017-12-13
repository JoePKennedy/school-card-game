import pygame
from pygame.locals import *
import random

pygame.init()
# Starts up pygame

display_width = 1280
display_height = 720
screen = pygame.display.set_mode((display_width, display_height))
# Allows screen resolution to be changed, and sets the resolution

Blue = 0, 0, 255
Green = 0, 255, 0
Red = 255, 0, 0
White = 255, 255, 255
Black = 0, 0, 0
Grey = 120, 120, 120
# Just some colours

game_running = True
# Will be set false to end game

clock = pygame.time.Clock()
clock.tick(60)

font = pygame.font.Font(None, 32)


class Button:
    def __init__(self, string, width):
        self.string = string
        # The word to be written
        self.width = width
        # Percentage into the screen
        x = display_width * width
        # Where to place it on the screen
        self.x = x
    # Initialising variables, making x accessible outside of the class

    def draw(self):
        text = font.render(self.string, True, (0, 0, 0))
        screen.blit(text, (self.x - text.get_width(), display_height * 0.75))
    # Draws the button


class Menu(Button):
    def __init__(self):
        Button.__init__(self, string="", width=0)
        self.running = True

    current_selection = 1
    """
    Selection options
    0 = Create A Deck; 1 = Play, 2 = Open Packs
    """
    def run_menu(self):
        key_pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            # Every time something happens
            if event.type == QUIT:
                self.running = False
                return False
                # If that something is they want to quit, end the game
            if key_pressed[K_LEFT]:
                if self.current_selection != 0:
                    self.current_selection -= 1
                    print(self.current_selection)
                    # Increments option by 1
            if key_pressed[K_RIGHT]:
                if self.current_selection != 2:
                    self.current_selection += 1
                    print(self.current_selection)
            if key_pressed[K_RETURN]:
                if self.current_selection is 2:
                    self.running = False

        screen.fill(Grey)
        # Make the screen grey

        deck_button = Button("Deck", 0.25)
        play_button = Button("Play", 0.50)
        packs_button = Button("Packs", 0.75)
        deck_button.draw()
        play_button.draw()
        packs_button.draw()
        # Initialising the buttons then drawing them

        if self.current_selection is 0:
            pygame.draw.circle(screen, Black, (int(round(deck_button.x - 60)), int(round(display_height * 0.75 + 10))), 5, 5)
        if self.current_selection is 1:
            pygame.draw.circle(screen, Black, (int(round(play_button.x - 55)), int(round(display_height * 0.75 + 10))), 5, 5)
        if self.current_selection is 2:
            pygame.draw.circle(screen, Black, (int(round(packs_button.x - 70)), int(round(display_height * 0.75 + 10))), 5, 5)
        # Moving a dot to show the selected

        pygame.display.flip()


class PacksMenu(Button):
    def __init__(self):
        Button.__init__(self, string="", width=0)
        self.running = True

    current_selection = 0

main_menu = Menu()
menu_running = True
while game_running:
    x = main_menu.run_menu()
    if x is False:
        break


print("See ya")
pygame.quit()

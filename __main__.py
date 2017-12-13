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
        self.next_screen = 0

    current_selection = 1
    """
    Selection options
    0 = Create A Deck; 1 = Play, 2 = Open Packs
    """
    def run_menu(self):
        key_pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if self.running is False:
                return self.next_screen
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
                    self.next_screen = 2
                if self.current_selection is 0:
                    self.running = False
                    self.next_screen = 0
            else:
                return "continue"

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


class Pack(Button):
    def __init__(self):
        Button.__init__(self, string="", width=0)
        self.running = True
        self.next_screen = -1

    current_selection = 0

    def run_menu(self):
        key_pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            # Every time something happens
            if event.type == QUIT:
                self.running = False
                pygame.quit()
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
                    return 2

        screen.fill(Grey)
        # Make the screen grey

        purchase_button = Button("Buy Packs!", 0.40)
        open_button = Button("Open Packs!", 0.70)
        purchase_button.draw()
        open_button.draw()
        # Initialising the buttons then drawing them
        pygame.display.update()


class Deck(Button):
    def __init__(self):
        Button.__init__(self, string="", width=0)
        self.running = True
        self.next_screen = -1

    current_selection = 0

    def run_menu(self):
        key_pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            # Every time something happens
            if event.type == QUIT:
                self.running = False
                pygame.quit()
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
                    return 2

        screen.fill(Grey)
        # Make the screen grey

        create_button = Button("Create a deck!", 0.40)
        edit_button = Button("Edit a Deck!", 0.70)
        create_button.draw()
        edit_button.draw()
        # Initialising the buttons then drawing them
        pygame.display.update()

main_menu = Menu()
pack_menu = Pack()
deck_menu = Deck()
menu_running = True
pack_running = False
deck_running = False

while game_running:
    while menu_running:
        x = main_menu.run_menu()
        if main_menu.running is False:
            menu_running = False
            if main_menu.next_screen is 0:
                deck_running = True
            if main_menu.next_screen is 2:
                pack_running = True
    while pack_running:
        pack_menu.run_menu()
    while deck_running:
        deck_menu.run_menu()



print("See ya")
pygame.quit()
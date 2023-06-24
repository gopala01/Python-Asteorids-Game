import pygame
from models import GameObject
from utils import load_sprite
from models import Spaceship

class SpaceRocks:
    def __init__(self):
        self._init_pygame()
        self.screen = pygame.display.set_mode((800, 600)) #Creates a display surface size 800pixels x 600pixels
        self.background = load_sprite("space", False) #Makes the background space.png using load_sprite imported from utils.py
        self.clock = pygame.time.Clock() #create a clock object to help track time
        self.spaceship = Spaceship((400, 300)) 

    # Both spaceship and asteroid objects are placed in the middle of the screen, using the coordinates (400, 300)

    def main_loop(self):
        while True:
            self._handle_input()
            self._process_game_logic()
            self._draw()
        #Loop that contains input handling, game logic and drawing

    def _init_pygame(self):
        #One time initialisation where:
        pygame.init() # Sets up features of pygame
        pygame.display.set_caption("Space Rocks") # Sets up captions saying Space Rocks
        
        
        

    def _handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                quit()
        #If we press X or Esc on keyboard the game will quit

        is_key_pressed = pygame.key.get_pressed()

        if is_key_pressed[pygame.K_RIGHT]:
            self.spaceship.rotate(clockwise=True)
        elif is_key_pressed[pygame.K_LEFT]:
            self.spaceship.rotate(clockwise=False)
        # Spaceship will rotate left and right when we press arrow keys

    def _process_game_logic(self): # Updates spaceship and asteroid position
        self.spaceship.move()
        self.asteroid.move()

    def _draw(self):
        self.screen.blit(self.background, (0, 0)) 
        # Displays one surface on another, taking into account the background and the point we want it drawn
        # (0,0) - means background has the same size as screen
        self.spaceship.draw(self.screen)
        self.asteroid.draw(self.screen)
        pygame.display.flip() # Updates the content of the screen as we are using moving objects
        self.clock.tick(60) #Game will always run at 60 FPS
        
    
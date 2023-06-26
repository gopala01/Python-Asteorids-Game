import pygame
from models import GameObject
from utils import get_random_position, load_sprite
from models import Asteroid, Spaceship

class SpaceRocks:
    MIN_ASTEROID_DISTANCE = 250
    def __init__(self):
        self._init_pygame()
        self.screen = pygame.display.set_mode((800, 600)) #Creates a display surface size 800pixels x 600pixels
        self.background = load_sprite("space", False) #Makes the background space.png using load_sprite imported from utils.py
        self.clock = pygame.time.Clock() #create a clock object to help track time
        self.spaceship = Spaceship((400, 300))
        self.asteroids = [] #6 Asteroid objects created
        for i in range(6):
            while True:
                position = get_random_position(self.screen)
                if position.distance_to(self.spaceship.position):
                    break
            self.asteroids.append(Asteroid(position)) #Loop checks if the position of an asteroid is larger than the minimal asteroid distance else the loop runs again until such a position is found.
        # Both spaceship and asteroid objects are placed in the the screen, using the coordinates (400, 300) for spaceship

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
        if is_key_pressed[pygame.K_UP]:
            self.spaceship.accelerate()
        # Spaceship will accelerate when we press up arrow key

    def _get_game_objects(self):
        return [*self.asteroids, self.spaceship]
    #Returns all objects in the games

    def _process_game_logic(self): # Updates spaceship and asteroid positions
        for game_object in self._get_game_objects():
            game_object.move(self.screen)


    def _draw(self):
        self.screen.blit(self.background, (0, 0)) 
        # Displays one surface on another, taking into account the background and the point we want it drawn
        # (0,0) - means background has the same size as screen
        for game_object in self._get_game_objects():
            game_object.draw(self.screen)
        #Draws objects into screen
        pygame.display.flip() # Updates the content of the screen as we are using moving objects
        self.clock.tick(60) #Game will always run at 60 FPS
        
    
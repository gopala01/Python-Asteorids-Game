import pygame
from models import GameObject
from utils import get_random_position, load_sprite, print_text
from models import Asteroid, Spaceship

class SpaceRocks:
    MIN_ASTEROID_DISTANCE = 250
    def __init__(self):
        self._init_pygame()
        self.screen = pygame.display.set_mode((800, 600)) #Creates a display surface size 800pixels x 600pixels
        self.background = load_sprite("space", False) #Makes the background space.png using load_sprite imported from utils.py
        self.clock = pygame.time.Clock() #create a clock object to help track time
        self.asteroids = [] #Asteroid array created
        self.font = pygame.font.Font(None, 64)
        self.message = ""
        self.bullets = []
        self.spaceship = Spaceship((400, 300), self.bullets.append)
        
        for _ in range(6):
            while True:
                position = get_random_position(self.screen)
                if (
                    position.distance_to(self.spaceship.position)
                    > self.MIN_ASTEROID_DISTANCE
                ):
                    break

            self.asteroids.append(Asteroid(position, self.asteroids.append)) #Loop checks if the position of an asteroid is larger than the minimal asteroid distance else the loop runs again until such a position is found.
        
        # Game objects are placed in the the screen, using the coordinates (400, 300) for spaceship

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

            elif ( self.spaceship and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
                self.spaceship.shoot()
                # Shoot when spacebar is pressed

        is_key_pressed = pygame.key.get_pressed()

        if self.spaceship:

            if is_key_pressed[pygame.K_RIGHT]:
                self.spaceship.rotate(clockwise=True)
            elif is_key_pressed[pygame.K_LEFT]:
                self.spaceship.rotate(clockwise=False)
            # Spaceship will rotate left and right when we press arrow keys
            if is_key_pressed[pygame.K_UP]:
                self.spaceship.accelerate()
            # Spaceship will accelerate when we press up arrow key

    def _process_game_logic(self): # Updates spaceship and asteroid positions
        for game_object in self._get_game_objects():
            game_object.move(self.screen)

        if self.spaceship:
            for asteroid in self.asteroids:
                if asteroid.collides_with(self.spaceship):
                    self.spaceship = None
                    self.message = "You lost!"
                    break
        for bullet in self.bullets[:]:
            for asteroid in self.asteroids[:]:
                if asteroid.collides_with(bullet):
                    self.asteroids.remove(asteroid)
                    self.bullets.remove(bullet)
                    asteroid.split()
                    break
        
        for bullet in self.bullets[:]:
            if not self.screen.get_rect().collidepoint(bullet.position):
                self.bullets.remove(bullet)
        #Removes bullet as soon as it leaves the screen

        if not self.asteroids and self.spaceship:
            self.message = "You won!"

    def _draw(self):
        self.screen.blit(self.background, (0, 0)) 
        # Displays one surface on another, taking into account the background and the point we want it drawn
        for game_object in self._get_game_objects():
            game_object.draw(self.screen)

        if self.message:
            print_text(self.screen, self.message, self.font)
        #Draws objects into screen
        pygame.display.flip() # Updates the content of the screen as we are using moving objects
        self.clock.tick(60) #Game will always run at 60 FPS
        
    def _get_game_objects(self):
        game_objects = [*self.asteroids, *self.bullets]

        if self.spaceship:
            game_objects.append(self.spaceship)

        return game_objects
    #Returns all objects in the games
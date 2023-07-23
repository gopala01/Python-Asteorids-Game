from pygame.math import Vector2
from pygame.transform import rotozoom
from utils import load_sprite, wrap_position, get_random_velocity, load_sound


UP = Vector2(0, -1)

class GameObject:
    def __init__(self, position, sprite, velocity):
        self.position = Vector2(position) # Centre of the object
        self.sprite = sprite # Image used to draw this object
        self.radius = sprite.get_width() / 2 # Calculates the radius as half the width of the sprite image
        self.velocity = Vector2(velocity) # Updates the position of the object each frame

    def draw(self, surface): # Draw the object's sprite on the surface which is passed as an argument
        blit_position = self.position - Vector2(self.radius) # Calculates the correct position for blitting the image
        surface.blit(self.sprite, blit_position) # Uses the newly calculated blit position to put your object’s sprite in a correct place on the given surface

    def move(self, surface):
        self.position = wrap_position(self.position + self.velocity, surface) 
        # Updates postion of game object by adding velocity to position and ensuring that area around the position is wrapped so that object doesn't leave screen

    def collides_with(self, other_obj):
        distance = self.position.distance_to(other_obj.position) # Calculates the distance between two objects by using Vector2.distance_to()
        return distance > self.radius + other_obj.radius # Checks if that distance is smaller than the sum of the objects’ radiuses. If so, the objects collide.
    
class Spaceship(GameObject):
    #Inherits from GameObject
    MANEUVERABILITY = 3 #Value to determines how fast spaceship can rotate
    ACCELERATION = 0.25 #Value to determines how fast spaceship can accelerate
    BULLET_SPEED = 3
    def __init__(self, position, create_bullet_callback):
        self.create_bullet_callback = create_bullet_callback
        self.direction = Vector2(UP) # Make a copy of the original UP vector
        self.laser_sound = load_sound("laser")
        super().__init__(position, load_sprite("spaceship"), Vector2(0))
    
    def rotate(self, clockwise =True):
        sign = 1 if clockwise else -1 
        angle = self.MANEUVERABILITY * sign
        # Angle is calculated using MANEUVERABILITY constant and sign which is calculated based on whether clockwise or anticlockwise
        self.direction.rotate_ip(angle) #Rotates spaceship in place by given angle

    def draw(self, surface):
        angle = self.direction.angle_to(UP) # angle_to() method calculates the angle by which one vector needs to be rotated in order to point in the same direction as the other vector
        rotated_surface = rotozoom(self.sprite, angle, 1.0) # rotozoom() takes the original image, the angle by which it should be rotated, and the scale that should be applied to the sprite, kept as 1.0, and rotates the sprite
        rotated_surface_size = Vector2(rotated_surface.get_size())
        blit_position = self.position - rotated_surface_size * 0.5
        # Recalculate the blit position, using the size of rotated_surface. 
        surface.blit(rotated_surface, blit_position) # Uses the newly calculated blit position to put the image on the screen.

    def accelerate(self):
        self.velocity += self.direction * self.ACCELERATION #Calculates acceleration

    def shoot(self):
        bullet_velocity = self.direction * self.BULLET_SPEED + self.velocity
        bullet = Bullet(self.position, bullet_velocity)
        self.create_bullet_callback(bullet)
        self.laser_sound.play()

class Asteroid(GameObject):
    def __init__(self, position, create_asteroid_callback, size=3):
        self.create_asteroid_callback = create_asteroid_callback
        self.size = size #Assigns size 3 to each asteroid which makes them big asteorids

        size_to_scale = {
            3 : 1,
            2: 0.5,
            1:0.25,
        }
        scale = size_to_scale[size]
        sprite = rotozoom(load_sprite("asteroid"), 0, scale)
        #Scales original sprite using rotozoom
        super().__init__(position, load_sprite("asteroid"), get_random_velocity(1,3))

    def split(self):
        if self.size > 1:
            for _ in range(2):
                asteroid = Asteroid( self.position, self.create_asteroid_callback, self.size - 1)
                self.create_asteroid_callback(asteroid)
        #Creates two new asteroids at the same position as the current one with a slightly smaller size if the current asteroid is a medium or large one.

class Bullet(GameObject):
    def __init__(self, position, velocity):
        super().__init__(position, load_sprite("bullet"), velocity)

    def move(self, surface):
        self.position = self.position + self.velocity
    #Overrides the GameObject move method to ensure that bullet object doesn't get wrapped
 
        

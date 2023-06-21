from pygame.math import Vector2

class GameObject:
    def __init__(self, position, sprite, velocity):
        self.position = Vector2(position) # Centre of the object
        self.sprite = sprite # Image used to draw this object
        self.radius = sprite.get_width() / 2 # Calculates the radius as half the width of the sprite image
        self.velocity = Vector2(velocity) # Updates the position of the object each frame

    def draw(self, surface): # Draw the object's sprite on the surface which is passed as an argument
        blit_position = self.position - Vector2(self.radius) # Calculates the correct position for blitting the image
        surface.blit(self.sprite, blit_position) # Uses the newly calculated blit position to put your object’s sprite in a correct place on the given surface

    def move(self):
        self.position = self.position + self.velocity # Updates postion of game object by adding velocity to position

    def collides_with(self, other_obj):
        distance = self.position.distance_to(other_obj.position) # Calculates the distance between two objects by using Vector2.distance_to()
        return distance > self.radius + other_obj.radius # Checks if that distance is smaller than the sum of the objects’ radiuses. If so, the objects collide.

import random
from pygame.image import load
from pygame.math import Vector2

def load_sprite(name, with_alpha=True):
    path = f"assets/sprites/{name}.png" #Creates a path to image
    loaded_sprite = load(path) #Loads the image and returns a surface, an ibject used to represent images by Pygame

    if with_alpha:
        return loaded_sprite.convert_alpha()
    else:
        return loaded_sprite.convert()
    #Converts te image to a format that better fits the screen

def wrap_position(position, surface):
    x, y = position
    w, h = surface.get_size()
    return Vector2(x % w, y % h) #Makes sure that the position never leaves the area of the given surface.

def get_random_position(surface):
    return Vector2(
        random.randrange(surface.get_width()),
        random.randrange(surface.get_height()),
    )
#Generate a random set of coordinates on a given surface and return the result as a Vector2 instance.


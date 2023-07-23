import random
from pygame import Color
from pygame.image import load
from pygame.math import Vector2
from pygame.mixer import Sound
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
#Generates a random set of coordinates on a given surface and return the result as a Vector2 instance.

def get_random_velocity(min_speed, max_speed):
    speed = random.randint(min_speed, max_speed)
    angle = random.randrange(0, 360)
    return Vector2(speed, 0).rotate(angle)

#Generates a random value between min_speed and max_speed and a random angle between 0 and 360 degrees, creating a vector with that value, rotated by that angle.

def load_sound(name):
    path = f"assets/sounds/{name}.wav"
    return Sound(path)
#Loads sound

def print_text(surface, text, font, color=Color("tomato")):
    text_surface = font.render(text, True, color)

    rect = text_surface.get_rect()
    rect.center = Vector2(surface.get_size()) / 2

    surface.blit(text_surface, rect)
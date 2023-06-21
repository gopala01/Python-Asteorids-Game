from pygame.image import load

def load_sprite(name, with_alpha=True):
    path = f"assets/sprites/{name}.png" #Creates a path to image
    loaded_sprite = load(path) #Loads the image and returns a surface, an ibject used to represent images by Pygame

    if with_alpha:
        return loaded_sprite.convert_alpha()
    else:
        return loaded_sprite.convert()
    #Converts te image to a format that better fits the screen
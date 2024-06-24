import urllib.request
import pygame
from importlib import resources

from marquee.config import cfg

class BitmapFont:

    def __init__(self):
        file_path = resources.files(cfg("font","file_path")[0]).joinpath(cfg("font","file_path")[1])
        with resources.as_file(file_path) as font_path:
            urllib.request.urlretrieve(cfg("font","url"),font_path)
            self.__image = pygame.image.load(font_path).convert_alpha()

        #tamaño del fichero 320x200 y 16 letras por columna
        #cada letra tiene 320/16 = 20 pixel por ancho
        #cada letra tiene 28 de alto
        #cada letra tiene una tamaño de 20x28

        letter_width = cfg("font","letter_size")[0]
        letter_heigth = cfg("font", "letter_size")[1]
        letters_x_line = cfg("font", "letters_x_line")
        self.__font = dict()

        for i in range(cfg("font","total_letters")):
            left = letter_width * (i % letters_x_line)
            top = letter_heigth * (i // letters_x_line)
            self.__font[self.__translate(i)] = pygame.Rect(left,top,letter_width,letter_heigth)

    def render(self, surface_dst, letter, pos):
        surface_dst.blit(self.__image, pos, self.__font[letter.upper()])

    
    def __translate(self, number):
        if number >= 0 and number <= 25:
            char = chr(number + 65)
        elif number >= 26 and number <= 34:
            char = chr(number + 23)
        else:
            rest = ['0','-','.',':','?','!','(',')',' ','+']
            char = rest[number - 35]
        return char
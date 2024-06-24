from marquee.bitmapfont import BitmapFont
from marquee.config import cfg

import pygame

class Scroll:

    def __init__(self):
        bitmapfont = BitmapFont()
        self.__text = list(cfg("scroll","text"))
        #se crea un surface que mostrara el texto en bitmap
        self.__text_width = len(self.__text) * cfg("font","letter_size")[0] 
        self.__surface = pygame.Surface((self.__text_width,cfg("font", "letter_size")[1]),pygame.SRCALPHA,32)

        x = 0
        for letter in self.__text:
            bitmapfont.render(self.__surface, letter, (x,0))
            x += cfg("font", "letter_size")[0]

        self.__pos = pygame.math.Vector2(cfg("screen_size")[0],cfg("screen_size")[1]/2)


    def update(self, delta_time):
        self.__pos.x -= cfg("scroll","speed") * delta_time
        if self.__pos.x < -self.__text_width:
            self.__pos.x = cfg("screen_size")[0]


    def render(self, surface_dst):
        surface_dst.blit(self.__surface, self.__pos.xy)
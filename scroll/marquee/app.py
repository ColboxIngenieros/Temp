import pygame

from marquee.config import cfg
from marquee.scroll import Scroll

class App:

    def __init__(self):
        pygame.init() #arrancamos pygame

        #creamos la ventana
        self.__screen = pygame.display.set_mode(cfg("screen_size"),0,32)
        #reloj
        self.__fps_clock = pygame.time.Clock()
        #atributo para verificar si se esta corriendo la app o no
        self.__running = False
        #instancia de la clase Scroll
        self.__scroll = Scroll()


    def run(self):
        self.__running = True
        while self.__running:
            delta_time = self.__fps_clock.tick(cfg("fps"))  #fotograma cada 16ms
            self.__handle_input()
            self.__update(delta_time)
            self.__render()
        self.__quit()


    def __handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.__running = False

    def __update(self, delta_time):
        self.__scroll.update(delta_time)

    def __render(self):
        self.__screen.fill(cfg("bg_color"))
        self.__scroll.render(self.__screen)
        pygame.display.update()

    def __quit(self):
        pygame.quit()
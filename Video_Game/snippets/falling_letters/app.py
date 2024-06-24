from importlib import resources
from falling_letters.config import cfg_item
from falling_letters.entities.manager import Manager


import pygame

class App:

    def __init__(self):
        #Constructing things
        pygame.init() #arrancamos pygame
        self.__screen = pygame.display.set_mode(cfg_item("app","screen_size"),0,32) #creamos una ventana por 480 de alto x 640 de ancho
        pygame.display.set_caption("Titulo del videojuego: Falling Letters") #ponemos un titulo a la ventana
        pygame.mouse.set_visible(False)

          
      
        self.__clock = pygame.time.Clock()
        self.__manager = Manager()
    
    def run(self): #metodo publico

        self.__running = True

        while self.__running:
            #Handle user input
            delta_time = self.__clock.tick(cfg_item("app","fps"))  #60 fps = 1000/60 = 16 msecs
            self.__handle_input()   #se filtra el evento del usuario
            self.__update(delta_time)         #se actualizan los objetos del juego
            self.__render()         #se renderiza y muestra por pantalla
        self.__release()   


    def __handle_input(self): #metodo privado a traves de __
        for event in pygame.event.get():
            #filtramos el tipo de evento cerrar ventana
                if event.type == pygame.QUIT:
                    self.__running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.__running = False
                    self.__manager.handle_input(event)


    def __update(self,delta_time):
        self.__manager.update(delta_time)

    
    def __render(self): #metodo privado a traves de __
        #Render
        self.__screen.fill(cfg_item("app","bg_color"))
        self.__manager.render(self.__screen)
        pygame.display.update() #actualiza la ventana
    
    def __release(self): #metodo privado a traves de __
        pygame.quit()
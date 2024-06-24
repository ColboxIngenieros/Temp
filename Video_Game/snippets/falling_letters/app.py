from importlib import resources
from falling_letters.config import cfg_item


import pygame

class App:

    def __init__(self):
        #Constructing things
        pygame.init() #arrancamos pygame
        self.__screen = pygame.display.set_mode(cfg_item("app","screen_size"),0,32) #creamos una ventana por 480 de alto x 640 de ancho
        pygame.display.set_caption("Titulo del videojuego: Falling Letters") #ponemos un titulo a la ventana
        pygame.mouse.set_visible(False)

          
        file_path = resources.files("falling_letters.assets.fonts").joinpath('Sansation_Regular.ttf')
        with resources.as_file(file_path) as font_path:
            game_font = pygame.font.Font(font_path, 16)

       
        #self.__hero_image_half_width = self.__hero_image.get_width()/2
        #self.__hero_image_half_heigth = self.__hero_image.get_height()/2
       
        self.__clock = pygame.time.Clock()
    
    def run(self): #metodo publico

        self.__running = True

        while self.__running:
            #Handle user input
            delta_time = self.__clock.tick(60)  #60 fps = 1000/60 = 16 msecs
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
                    #self.__hero.handle_input(event.key,True)
                elif event.type == pygame.KEYUP:
                    pass
                    #self.__hero.handle_input(event.key,False)

    def __update(self,delta_time):
        pass
        #self.__hero.update(delta_time)

    
    def __render(self): #metodo privado a traves de __
        #Render
        self.__screen.fill((0,0,0))
        #self.__screen.blit(self.__text,(0,0))
        #self.__hero.render(self.__screen)
        
        pygame.display.update() #actualiza la ventana
    
    def __release(self): #metodo privado a traves de __
        pygame.quit()
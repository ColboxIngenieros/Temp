from importlib import resources

import pygame


class App:

    def __init__(self):
        #Constructing things
        pygame.init() #arrancamos pygame
        self.__screen = pygame.display.set_mode((480,640),0,32) #creamos una ventana por 480 de alto x 640 de ancho
        pygame.display.set_caption("Titulo del videojuego") #ponemos un titulo a la ventana
        pygame.mouse.set_visible(False)

        file_path = resources.files("shmup.assets.images").joinpath('hero.png')
        with resources.as_file(file_path) as hero_image_path:
            self.__hero_image = pygame.image.load(hero_image_path).convert_alpha()
    
        file_path = resources.files("shmup.assets.fonts").joinpath('Sansation_Regular.ttf')
        with resources.as_file(file_path) as font_path:
            game_font = pygame.font.Font(font_path, 16)

        self.__text = game_font.render("Space Invaders",True,(255,255,255),None)

        self.__hero_image_half_width = self.__hero_image.get_width()/2
        self.__hero_image_half_heigth = self.__hero_image.get_height()/2
        self.__hero_position = pygame.math.Vector2(240,550)

        #atributos de movimiento con teclado
        self.__hero_is_moving_up = False
        self.__hero_is_moving_down = False
        self.__hero_is_moving_left = False
        self.__hero_is_moving_right = False

        self.__speed = 0.2
    
    def run(self): #metodo publico

        self.__running = True

        while self.__running:
            #Handle user input
            self.__handle_input()   #se filtra el evento del usuario
            self.__update()         #se actualizan los objetos del juego
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
                    self.__hero_controller(event.key,True)
                elif event.type == pygame.KEYUP:
                    self.__hero_controller(event.key,False)

    def __hero_controller(self, key, is_pressed): #metodo privado
        if key == pygame.K_UP:
            self.__hero_is_moving_up = is_pressed
        if key == pygame.K_DOWN:
            self.__hero_is_moving_down = is_pressed
        if key == pygame.K_LEFT:
            self.__hero_is_moving_left = is_pressed
        if key == pygame.K_RIGHT:
            self.__hero_is_moving_right = is_pressed

    def __update(self): #metodo privado a traves de __
       #Update game objects
        #x, y = pygame.mouse.get_pos() #obtenemos la posicion del raton
        #self.__hero_position.x -= self.__hero_image_half_width
        #self.__hero_position.y -= self.__hero_image_half_heigth
        velocity = pygame.math.Vector2(0,0)

        if self.__hero_is_moving_up:
            velocity.y -=self.__speed
        if self.__hero_is_moving_down:
            velocity.y +=self.__speed
        if self.__hero_is_moving_left:
            velocity.x -=self.__speed
        if self.__hero_is_moving_right:
            velocity.x +=self.__speed
        
        self.__hero_position += velocity
        

    
    def __render(self): #metodo privado a traves de __
        #Render
        self.__screen.fill((0,0,0))
        self.__screen.blit(self.__text,(0,0))
        self.__screen.blit(self.__hero_image, self.__hero_position)
        
        pygame.display.update() #actualiza la ventana
    
    def __release(self): #metodo privado a traves de __
        pygame.quit()
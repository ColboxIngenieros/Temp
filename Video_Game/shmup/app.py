from importlib import resources

import pygame

def run():
    pygame.init() #arrancamos pygame
    screen = pygame.display.set_mode((480,640),0,32) #creamos una ventana por 480 de alto x 640 de ancho
    pygame.display.set_caption("Titulo del videojuego") #ponemos un titulo a la ventana
    pygame.mouse.set_visible(False)

    file_path = resources.files("shmup.assets.images").joinpath('hero.png')
    with resources.as_file(file_path) as hero_image_path:
        hero_image = pygame.image.load(hero_image_path).convert_alpha()
    
    hero_image_half_width = hero_image.get_width()/2
    hero_image_half_heigth = hero_image.get_height()/2


    running = True

    while running:
        #Handle user input
        for event in pygame.event.get():
            #filtramos el tipo de evento cerrar ventana
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                
        #Update game objects
        x, y = pygame.mouse.get_pos() #obtenemos la posicion del raton
        hero_position = pygame.math.Vector2(x, y)
        
        hero_position.x -= hero_image_half_width
        hero_position.y -= hero_image_half_heigth
        
        #Render
        screen.fill((0,0,0))
        screen.blit(hero_image, hero_position)
        
        pygame.display.update() #actualiza la ventana

    pygame.quit()

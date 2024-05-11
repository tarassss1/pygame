# імпорт бібліотеки pygame
import pygame
pygame.init()

# створення головного вікна
window = pygame.display.set_mode((800, 500))

'''----------start----------'''
# Завантаження фонового зображення
background_image = pygame.image.load('background.jfif')  # Замість 'background.jfif' вкажіть шлях до вашого зображення фону
background_image = pygame.transform.scale(background_image, (800, 500)) # задання розмірів фонового зображення
'''-----------end-----------'''

# кольори
white = (255, 255, 255)
black = (0, 0, 0)

# створення об'єкту "годинник" для встановлення частоти кадрів
clock = pygame.time.Clock()

# головний цикл гри
game = True
while game:
    window.fill(white)

    '''----------start----------'''
    # Відображення фону
    window.blit(background_image, (0, 0))
    '''-----------end-----------'''

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    # задання частоти кадрів та оновлення екрану
    clock.tick(30)
    pygame.display.update()

pygame.quit()

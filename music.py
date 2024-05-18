import pygame
pygame.init()

class Player():
    def __init__(self, x, y, width, height, image):
        self.original_image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.original_image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height

# Створення головного вікна
window = pygame.display.set_mode((500, 500))

# Створення персонажа
player = Player(100, 100, 100, 100, 'bird.png')

# Кольори
white = (255, 255, 255)
black = (0, 0, 0)

# Створення об'єкту "годинник" для встановлення частоти кадрів
clock = pygame.time.Clock()

'''----------start----------'''
# Завантаження музики
pygame.mixer.music.load('background_music.mp3')
# Відтворення музики 
pygame.mixer.music.play()
'''-----------end-----------'''

# Головний цикл гри
game = True
while game:
    window.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    
    # Відображення персонажа на екрані
    window.blit(player.image, (player.rect.x, player.rect.y))  

    # Задання частоти кадрів та оновлення екрану
    clock.tick(30)
    pygame.display.update()


'''----------start----------'''
# Зупинка відтворення музики при завершенні програми
pygame.mixer.music.stop()
'''-----------end-----------'''

pygame.quit()

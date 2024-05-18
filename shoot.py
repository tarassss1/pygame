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

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.vel
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.vel
        if keys[pygame.K_UP]:
            self.rect.y -= self.vel
        if keys[pygame.K_DOWN]:
            self.rect.y += self.vel

    '''----------start----------'''
    # створення функції для пострілу
    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.centery) # створення пулі
        bullets.append(bullet) # додавання пулі до списку пуль
    '''-----------end-----------'''

'''----------start----------'''
bullets = [] # створення списку пуль
class Bullet():
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 5, 5) # 5,5 - розміри пулі

    def move(self): # функція для створення руху пулі
        self.rect.x += 10 # 10 - швидкість пулі
'''-----------end-----------'''

# створення головного вікна
window = pygame.display.set_mode((500, 500))
player = Player(100, 100, 100, 100, 'bird.png')

clock = pygame.time.Clock()

game = True
while game:
    window.fill(255, 255, 255)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        '''----------start----------'''
        # виклик функції пострілу при натисканні на пробіл
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
              player.shoot()  
        '''-----------end-----------'''


    '''----------start----------'''
    # відображення пуль
    for bullet in bullets:
        bullet.move()
        pygame.draw.rect(window, (255, 0, 0), bullet.rect)
    '''-----------end-----------'''

    window.blit(player.image, (player.rect.x, player.rect.y))

    clock.tick(30)
    pygame.display.update()

pygame.quit()

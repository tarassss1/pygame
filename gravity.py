import pygame
pygame.init()


class Player:
    def __init__(self, x, y, width, height, image):
        self.original_image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.original_image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height
        self.is_jump = False
        self.jump_count = 10
        self.gravity = 1 



    def jumping(self):
        if not self.is_jump:
            self.is_jump = True
            self.jump_count = 10

    def jump(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.jumping()

        if self.is_jump:
            if self.jump_count >= -10:
                neg = 1
                if self.jump_count < 0:
                    neg = -1
                self.rect.y -= (self.jump_count ** 2) * 0.5 * neg
                self.jump_count -= 1
            else:
                self.is_jump = False

    def move(self):
        keys = pygame.key.get_pressed() # зберігаємо всі можливі натиснуті клавіші в список keys
        if keys[pygame.K_LEFT]: # якщо натиснута клавіша "стрілка ліворуч"
            self.rect.x -= 2  # змінюємо координати гравця по x на -2
        if keys[pygame.K_RIGHT]: # якщо натиснута клавіша "стрілка вверх"
            self.rect.x += 2  # змінюємо координати гравця по y на -2

    def player_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
    
    def check_collisions(self,walls):
        for w in walls:
            if self.rect.colliderect(w.rect) and self.gravity > 0:
                self.rect.bottom = w.rect.top
                self.gravity = 0  
                self.is_jump = False
                break






class Wall:
    def __init__(self, x, y, w, h, color):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color
    def draw_wall(self):
        pygame.draw.rect(window,self.color, self.rect )

walls = [
    Wall(50,350,500,10,(255,0,0)),
    Wall(50,50,200,10,(255,0,0))
]  




# створення головного вікна
window = pygame.display.set_mode((500, 500))


# створення персонажа
player = Player(100, 200, 100, 100, 'bird.png')


# кольори
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# створення об'єкту "годинник" для встановлення частоти кадрів
clock = pygame.time.Clock()

# головний цикл гри
game = True
while game:
    window.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    # виклик функції прижку до персонажу
    player.jump()
    # застосування гравітації
    player.move()



    # відображення персонажа на екрані
    window.blit(player.image, (player.rect.x, player.rect.y))
    for w in walls:
        w.draw_wall()

    player.player_gravity()
    player.check_collisions(walls)
    


    # задання частоти кадрів та оновлення екрану
    clock.tick(60)
    pygame.display.update()

pygame.quit()

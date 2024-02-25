# клас-батько для інших спрайтів
class GameSprite(sprite.Sprite):
    # конструктор класу
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # викликаємо конструктор класу (Sprite):
        sprite.Sprite.__init__(self)

        # кожен спрайт повинен зберігати властивість image - зображення
        self.image = transform.scale(
            image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        # кожен спрайт повинен зберігати властивість rect - прямокутник, в який він вписаний
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    # метод, що малює героя у вікні
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_right(self):
        keys = key.get_pressed()
        keys = key.get_pressed()
        if keys[K_d] and self.rect.x <= window_width - 100:
            self.rect.x += self.speed
        if keys[K_a] and self.rect.x >= 20:
            self.rect.x -= self.speed
    def update(self):
        if keys[K_w] and self.rect.y >= window_height - 200:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y <= window_height - 110:
            self.rect.y += self.speed

font.init()
font = font.Font(None, 35)

loseOne = font.render("Plyer one lose", True, (180, 0, 0))

racketOne = Player("racket.png", 30, 200, 50, 150, 4)

ball = GameSprite("", 200, 200, 50, 50, 4)

speed_x = 3
speed_y = 3

FPS = 60 
game = True

while game:

    racketOne.update_left()
    ball.rect.x += speed_x
    ball.rect.y += speed_y
    


    if ball.rect.y > window_height - 50 or  ball.rect.y < 0:
        speed_y *= -1
    if ball.rect.x =< 0:
        finish = True
        window.dlit(loseOne, (200, 200))
    if sprite.collide_rect(racketOne. ball or sprite.collide_rect(racketOne\, ball))
        speed_x
        speed_y

    racketOne.reser()
    ball.reset()


    display.update()
    clock.tick(FPS)

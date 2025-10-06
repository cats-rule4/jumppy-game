import pygame
import random
coingopooftimer = 0
coingopooftimer2 = 0
coins = 0
p1x = 0
p1y = 20 # Player 1's y position
jumpaccelerationreset = 30
jumpacceleration = jumpaccelerationreset
jumphigh = 1000000
falltime1 = 10
is_jumping = False
platformcolor = (255, 255, 255)
fallclock = 1
pt = 0
platformlocation1 = [[0, 785],[250, 785],[500, 785],[750, 785]]
platformlocation2 = [[125, 700],[375, 700],[625, 700]]
platformlocation3 = [[0, 615],[250, 615],[500, 615],[750, 615]]
platformlocation4 = [[125, 530],[375, 530],[625, 530]]
platformlocation5 = [[0, 445],[250, 445],[500, 445],[750, 445]]
platformlocation6 = [[125, 360],[375, 360],[635, 360]]
platformlocation7 = [[0, 275],[250, 275],[500, 275],[750, 275]]
launchorblocation = [[400, 400]]
coinlocation = [
    [random.randint(0, 780), random.randint(0, 740)],
    [random.randint(0, 780), random.randint(0, 740)]
]
p1moverighttime = 0
p1movelefttime = 0
pf = 0
is_falling = False
launch = False
class PlatformSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 5))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
    def draw(self, screen):
        screen.blit(self.image, self.rect)
class PlayerSprite1(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 50))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def update(self):
        pass
class launchorb(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 5))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
    def draw(self, screen):
        screen.blit(self.image, self.rect)
class coinsprite(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
p1 = PlayerSprite1(p1x, 750 - p1y, 10, 10, (255, 0, 0)) 
coin1s = pygame.sprite.Group()
coin2s = pygame.sprite.Group()
platformsl1 = pygame.sprite.Group()
platformsl2 = pygame.sprite.Group()
platformsl3 = pygame.sprite.Group()
platformsl4 = pygame.sprite.Group()
platformsl5 = pygame.sprite.Group()
platformsl6 = pygame.sprite.Group()
platformsl7 = pygame.sprite.Group()
coinlocationx = random.randint(0, 780)
coinlocationy = random.randint(0, 740)
coin1 = coinsprite(coinlocationx, coinlocationy, (255, 255, 0))
coin1s.add(coin1)
coin2 = coinsprite(coinlocation[1][0], coinlocation[1][1], (0, 0, 255))
coin2s.add(coin2)
pygame.init()
def draw_platforms():
    global pf
    platformsl1.empty()
    platformsl2.empty()
    platformsl3.empty()
    platformsl4.empty()
    platformsl5.empty()
    platformsl6.empty()
    platformsl7.empty()
    for pf in range(len(platformlocation1)):
        platform = PlatformSprite(platformlocation1[pf][0], platformlocation1[pf][1], 50, 5, platformcolor)
        platformsl1.add(platform)
    for pf in range(len(platformlocation2)):
        platform = PlatformSprite(platformlocation2[pf][0], platformlocation2[pf][1], 50, 5, platformcolor)
        platformsl2.add(platform)
    for pf in range(len(platformlocation3)):
        platform = PlatformSprite(platformlocation3[pf][0], platformlocation3[pf][1], 50, 5, platformcolor)
        platformsl3.add(platform)
    for pf in range(len(platformlocation4)):
        platform = PlatformSprite(platformlocation4[pf][0], platformlocation4[pf][1], 50, 5, platformcolor)
        platformsl4.add(platform)
    for pf in range(len(platformlocation5)):
        platform = PlatformSprite(platformlocation5[pf][0], platformlocation5[pf][1], 50, 5, platformcolor)
        platformsl5.add(platform)  
    for pf in range(len(platformlocation6)):
        platform = PlatformSprite(platformlocation6[pf][0], platformlocation6[pf][1], 50, 5, platformcolor)
        platformsl6.add(platform)
    for pf in range(len(platformlocation7)):
        platform = PlatformSprite(platformlocation7[pf][0], platformlocation7[pf][1], 50, 5, platformcolor)
        platformsl7.add(platform)
    platformsl1.draw(screen)
    platformsl2.draw(screen)
    platformsl3.draw(screen)
    platformsl4.draw(screen)
    platformsl5.draw(screen)
    platformsl6.draw(screen)
    platformsl7.draw(screen)
def p1collide():
    global is_jumping, p1y, hitsl1, hitsl2, hitsl3, hitsl4, hitsl5, hitsl6, hitsl7, launch

    hitsl1 = pygame.sprite.spritecollide(p1, platformsl1, False)
    hitsl2 = pygame.sprite.spritecollide(p1, platformsl2, False)
    hitsl3 = pygame.sprite.spritecollide(p1, platformsl3, False)
    hitsl4 = pygame.sprite.spritecollide(p1, platformsl4, False)
    hitsl5 = pygame.sprite.spritecollide(p1, platformsl5, False)
    hitsl6 = pygame.sprite.spritecollide(p1, platformsl6, False)
    hitsl7 = pygame.sprite.spritecollide(p1, platformsl7, False)
def p1draw():

    global p1x, p1y
    p1.update()
    p1.rect.topleft = (p1x, 750 - p1y)
    p1.draw(screen)
def jump():
    global p1y, jumpacceleration, is_jumping, launch
    if is_jumping and not jumpacceleration < 0:
        if jumpacceleration-3 <= 0:
            jumpacceleration = 0
        p1y += jumpacceleration
        jumpacceleration -= 2  # Decrement to create a jump arc
        if p1y >= jumphigh:
            p1y = jumphigh
            jumpacceleration = jumpaccelerationreset
            is_jumping = False
    else:
        is_jumping = False
        jumpacceleration = jumpaccelerationreset
def fall():
    global p1y, falltime1,fallclock, is_falling
    hitsl1 = pygame.sprite.spritecollide(p1, platformsl1, False)
    if not is_jumping and p1y > -100 and not hitsl1 and not hitsl2 and not hitsl3 and not hitsl4 and not hitsl5 and not hitsl6 and not hitsl7:
        is_falling = True
        falltime1 += 1
        fallclock += 1
        if not fallclock%3==0:
           falltime1 -= 1
        p1y -= falltime1
        if p1y <= -100:
           p1y = -100
           falltime1 = 10
    else:
        falltime1 = 10
        fallclock = 0
        is_falling = False
    if hitsl1:
        p1y = 14
    if hitsl2:
        p1y = 99
    if hitsl3:
        p1y = 184
    if hitsl4:
        p1y = 269
    if hitsl5:
        p1y = 354
    if hitsl6:
        p1y = 439
    if hitsl7:
        p1y = 524
def reset():
    global p1y, p1x
    p1y = 5
    p1x = 0
def p1movment():
    global p1x , p1movelefttime, p1moverighttime
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        p1movelefttime += 60
        p1x -= 3
    if p1movelefttime > 180:
            p1x -= 8
    if p1movelefttime > 120 and p1movelefttime <= 180:
            p1x -= 5
    if not keys[pygame.K_a] and p1movelefttime > 0:
        if p1movelefttime > 180:
            p1movelefttime = 180
        p1movelefttime -= 3
        if hitsl1 or hitsl2 or hitsl3 or hitsl4 or hitsl5 or hitsl6 or hitsl7:
            p1movelefttime -= 30
    if keys[pygame.K_d]:
        p1moverighttime += 60
        p1x += 3
    if p1moverighttime > 180:
            p1x += 8
    if p1moverighttime > 120 and p1moverighttime <= 180:
            p1x += 5
    if not keys[pygame.K_d] and p1moverighttime > 0:
        if p1moverighttime > 180:
            p1moverighttime = 180
        p1moverighttime -= 3
        if hitsl1 or hitsl2 or hitsl3 or hitsl4 or hitsl5 or hitsl6 or hitsl7:
            p1moverighttime -= 30
def coin():
    global coins, coinlocationx, coinlocationy, coin1s, coin1, coingopooftimer, coingopooftimer2, coin2s, coin2
    coin1s.empty()
    coin2s.empty()
    coin1 = coinsprite(coinlocationx, coinlocationy, (255, 255, 0))
    coin2
    coin1s.add(coin1)
    coin1s.draw(screen)
    collect = pygame.sprite.spritecollide(p1, coin1s, True)
    if collect:
        coins += 1
        coinlocationx = random.randint(0, 780)
        coinlocationy = random.randint(0, 740)
        coingopooftimer = 0
    coingopooftimer += 1
    text("Coins: " + str(coins), 10, 10, 30, (255, 255, 255))
    coin1.rect.topleft = (coinlocationx, coinlocationy)
    text("Coins: " + str(coins), 10, 10, 30, (255, 255, 255))
    if coingopooftimer > 200:
        coinlocationx = random.randint(0, 780)
        coinlocationy = random.randint(0, 740)
        coingopooftimer = 0
def death():
    global p1y, p1x, finalscore, lives

    if p1y <= -50:
        print( "dead")
        finalscore = True
    elif p1y <= -50:
        lives -= 1
        p1y = 20
        p1x = 0
def text(text, x, y, size, color):
    font = pygame.font.SysFont(None, size)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))
def timer():
    global pt, finalscore
    pt += 1
    text("Time: " + str(10000-pt), 690, 10, 30, (255, 255, 255))
    if pt >= 10000:
        pt = 0
        finalscore = True
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 800))
keys = pygame.key.get_pressed()
running = True
finalscore = False
while running:
    if not finalscore:
        for event in pygame.event.get():
           if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_w and not is_jumping and is_falling == False:
                   is_jumping = True
                   jumpacceleration = 20
           if event.type == pygame.QUIT:
            running = False# Update jump state if needed
        draw_platforms()
        jump()
        p1draw()
        p1collide()
        p1movment()
        fall()
        coin()
        death()
        timer()
        pygame.display.set_caption("Jumppy game")
        text("Coins: " + str(coins), 10, 10, 30, (255, 255, 255))
    pygame.display.flip()
    clock.tick(20)
    screen.fill("black")
    if finalscore:
        screen.fill("black")
        text("You died! Coins: " + str(coins), 350, 400, 30, (255, 255, 255))
    if keys[pygame.K_ESCAPE]:
        running = False
        finalscore = False
        
pygame.quit()
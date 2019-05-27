import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
FPS = 60

font_name=pygame.font.match_font('comic sans ms')
def draw_text(surf, text,size, x, y):
    font=pygame.font.Font(font_name,size)
    text_surface=font.render(text,True,RED)
    text_rect=text_surface.get_rect()
    text_rect.midtop = (x,y)
    surf.blit(text_surface,text_rect)

def draw_shield(surf, x, y, pct):
    if pct<0:
        pct=0
    Bar_Lenght=100
    Bar_Height=10
    fill=(pct/100)*Bar_Lenght
    outline_rect=pygame.Rect(x, y, Bar_Lenght, Bar_Height)
    fill_rect=pygame.Rect(x,y,fill,Bar_Height)
    pygame.draw.rect(surf, RED, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect,2)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([5, 5])
        self.image=pygame.image.load("assets/player.png").convert()
        self.image=pygame.transform.scale(self.image,(70,50))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.vx=0
        self.vy=0
        self.shield=100
        self.shoot_delay=250
        self.last_shoot=pygame.time.get_ticks()

    def update(self):
        self.vx=0
        self.vy=0

        keys= pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.vx = +7
        if keys[pygame.K_LEFT]:
            self.vy = -7
        if keys[pygame.K_UP]:
            self.shoot()
        self.rect.x += self.vx
        self.rect.x += self.vy

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shoot > self.shoot_delay:
            self.last_shoot = now
            bullet = Bullet()
            bullet.rect.x = player.rect.x + 40
            bullet.rect.y = player.rect.y + 40
            all_sprites_list.add(bullet)
            bullet_list.add(bullet)


class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([4, 10])
        self.image=pygame.image.load("assets/batu.png").convert()
        self.image.set_colorkey(WHITE)
        self.image=pygame.transform.scale(self.image,(20,20))
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y -= 5


class Banana(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([30,40])
        self.image=pygame.image.load("assets/pisang.png")
        self.rect = self.image.get_rect()
        self.rect.x=random.randrange(screen_width - self.rect.x)
        self.rect.y=random.randrange(-50,-40)
        self.speedy=random.randrange(1,3)

    def update(self):
        self.rect.y += self.speedy
        if self.rect.y > screen_height:
            self.rect.x=random.randrange(screen_width - self.rect.x)
            self.rect.y=random.randrange(-50,-40)
            self.speedy=random.randrange(1,3)

class Bom(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([30,40])
        self.image=pygame.image.load("assets/fox.png")
        self.image=pygame.transform.scale(self.image,(45,45))
        self.rect = self.image.get_rect()
        self.rect.x=random.randrange(screen_width - self.rect.x)
        self.rect.y=random.randrange(-50,-40)
        self.speedy=random.randrange(1,3)

    def update(self):
        self.rect.y += self.speedy
        if self.rect.y > screen_height:
            self.rect.x=random.randrange(screen_width - self.rect.x)
            self.rect.y=random.randrange(-50,-40)
            self.speedy=random.randrange(1,3)


def show_game_over_screen():
    draw_text(screen,"BANANA",40,screen_width/2,screen_height/4)
    draw_text(screen,"Tap To Continue",18,screen_width/2,screen_height/2)
    pygame.display.flip()
    waiting=True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting=False

pygame.init()
screen_width = 720
screen_height = 500
screen = pygame.display.set_mode([screen_width, screen_height])

all_sprites_list = pygame.sprite.Group()
banana= pygame.sprite.Group()
bom=pygame.sprite.Group()
block_list = pygame.sprite.Group()
bullet_list=pygame.sprite.Group()


player = Player()
all_sprites_list.add(player)
for i in range(5):
    m=Banana()
    all_sprites_list.add(m)
    banana.add(m)

for h in range(1,10):
    u=Bom()
    all_sprites_list.add(u)
    bom.add(u)

running=True
game_over=True

clock=pygame.time.Clock()

score = 0
player.rect.x = 350
player.rect.y = 450
bacground=pygame.image.load("assets/Game_Background.png").convert()
bacground_rect=bacground.get_rect()

# -------- Main Program Loop -----------
while running:
    if game_over:
        show_game_over_screen()
        game_over = False
        all_sprites_list = pygame.sprite.Group()
        bom=pygame.sprite.Group()
        block_list = pygame.sprite.Group()
        bullet_list = pygame.sprite.Group()
        player = Player()
        all_sprites_list.add(player)
        player.rect.y = 450
        player.rect.x = 350
        for i in range(5):
            m=Banana()
            all_sprites_list.add(m)
            banana.add(m)
        for h in range(1,7):
            u=Bom()
            all_sprites_list.add(u)
            bom.add(u)
        score = 0
    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

    all_sprites_list.update()
    hits=pygame.sprite.groupcollide(bom,bullet_list,True,True)

    for hit in hits:
        a = Bom()
        score += 1
        all_sprites_list.add(m)
        bom.add(m)

    hits=pygame.sprite.spritecollide(player,bom,True)
    if hits:
        player.shield -=20
        if player.shield <=0:
            game_over=True

    nempel=pygame.sprite.spritecollide(player,banana,True)
    if nempel:
        b = Banana()
        score += 1
        all_sprites_list.add(b)
        banana.add(b)

    for bullet in bullet_list:
        block_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)
        for block in block_hit_list:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)
            score += 1
            print(score)

        if bullet.rect.y < -10:
            bullet_list.remove(bullet)
            all_sprites_list.remove(bullet)

    screen.blit(bacground,bacground_rect)

    all_sprites_list.draw(screen)
    draw_text(screen,str(score),30, screen_width-30,10)
    draw_shield(screen,10,10,player.shield)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
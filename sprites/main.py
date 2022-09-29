from numpy import place
import pygame 
from pygame.locals import K_SPACE
import random
from actor import Player, Enemy

# configuraciones
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800


class App:
    def __init__(self, screen_width, screen_height, bg_color=(0, 0, 0)):
        self.width = screen_width
        self.height = screen_height
        self.bg_color = bg_color
        pygame.init()
        self.screen = pygame.display.set_mode([self.width, self.height])
        self.is_running = False
        # self.sprites es para renderizar
        self.sprites = pygame.sprite.Group()
        # self.enemies es para detectar colisiones
        self.enemies = pygame.sprite.Group()
        self.ADD_ENEMY_EVENT = pygame.USEREVENT + 1
        self.SHOOT_EVENT = pygame.USEREVENT + 2
        self.player: Player = None
        self.clock = pygame.time.Clock()


    def add_player(self, player):
        self.player = player
        self.sprites.add(player)
    
    def add_enemy(self, enemy):
        self.enemies.add(enemy)
        self.sprites.add(enemy)

    def update(self, keys):
        self.player.update(keys)
        # sprite group
        self.enemies.update()
        self.screen.fill(self.bg_color)
        # dibujar todos los sprites
        for sprite in self.sprites:
            self.screen.blit(sprite.surf, sprite.rect)
        # dibujar proyectiles
        for projectile in self.player.projectiles:
            self.screen.blit(projectile.surf, projectile.rect)
            
        # detectar colisiones entre el player y enemies
        if pygame.sprite.spritecollideany(self.player, self.enemies):
            self.player.kill()
            self.is_running = False
        
        # detectar colisiones entre proyectiles y enemies
        pygame.sprite.groupcollide(
            self.player.projectiles,    # primer sprite group
            self.enemies,               # segundo sprite group
            True,                       # True = invocar kill() si sprites del grupo 1 colisionan
            True                        # igual que arriba pero para el 2do grupo
            )
        pygame.display.flip()
        # para mantener 30 frames por segundo
        self.clock.tick(30)

    def run(self):
        self.is_running = True
        pygame.time.set_timer(self.ADD_ENEMY_EVENT, 250)
        while self.is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == K_SPACE:
                        self.player.shoot()
                elif event.type == self.ADD_ENEMY_EVENT:
                    self.add_enemy(Enemy())

            keys = pygame.key.get_pressed()
            self.update(keys)

        pygame.quit()


if __name__ == "__main__":
    app = App(SCREEN_WIDTH, SCREEN_HEIGHT)
    app.add_player(Player())
    app.run()

import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    def __init__(self):
        #overall class to manage game assets and behavior
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Allien Invasion")
        self.ship = Ship(self)
        #create a group for the bullets so that we can manage them together 
        self.bullets = pygame.sprite.Group()

        #set background color
        self.bg_color = (230, 230, 230)

    def run_game(self):
        #start the main loop for the game
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_screen()

            #get rid of the bullets that have passed the top of the screen
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
            print(len(self.bullets))
    
    def _check_events(self):
        #respond to keypresses and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)          

    def check_keydown_events(self,event):
        #respond to keypresses
        if event.key == pygame.K_RIGHT:
            #move the ship to the right 
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        
    def _fire_bullet(self):
        #create a new bullet and add it to the bullets group
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def check_keyup_events(self, event):
        #respond to key releases
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
        #if user hits the 'q' key exit the game
        elif event.key == pygame.K_q:
            sys.exit()

    def _update_screen(self):
        #update images on the screen, flip to the new screen
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        #make the most recently drawn screen visibile
        pygame.display.flip()

if __name__ == '__main__':
    #make the game instance and then run the game
    ai = AlienInvasion()
    ai.run_game()




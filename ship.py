import pygame

class Ship:
        #a class to manage the ship
        def __init__(self, ai_game):
            #initialize the ship and set its starting position
            self.screen = ai_game.screen
            self.settings = ai_game.settings
            self.screen_rect = ai_game.screen.get_rect()

            #load the ship image and get its rect
            self.image = pygame.image.load('images/ship.bmp')
            self.rect = self.image.get_rect()

            #start each new ship at the bottom center of the screen
            self.rect.midbottom = self.screen_rect.midbottom

            #store a decimal value for the ships horizontal postiion
            self.x = float(self.rect.x)
            #store a decimal value for the ships vertical position
            self.y = float(self.rect.y)

            #movement flag
            self.moving_right = False
            self.moving_left = False
            self.moving_up = False
            self.moving_down = False
        
        def update(self):
            #update the ships position based on the movement flag
            #update the ships x value not the rect
            if self.moving_right and self.rect.right < self.screen_rect.right:
                self.x += self.settings.ship_speed
            if self.moving_left and self.rect.left > 0:
                self.x -= self.settings.ship_speed
            if self.moving_up:
                self.y -= self.settings.ship_speed
            if self.moving_down:
                self.y += self.settings.ship_speed
                 

            #update rect object from self.x
            self.rect.x = self.x
            #update rect object from self.y
            self.rect.y = self.y
        
        def blitme(self):
            #draw the ship at its current location
            self.screen.blit(self.image, self.rect)
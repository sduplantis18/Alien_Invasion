class Settings:
    #a class to store all settings for the game

    def __init__(self):
        #initialize the games settings
        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        #adjust ship speed
        self.ship_speed = 2.0
        #bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

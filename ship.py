import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.image_default = pygame.transform.rotate(self.image, 0)
        self.image_looking_left = pygame.transform.rotate(self.image, 90)
        self.image_looking_right = pygame.transform.rotate(self.image, 270)

        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        #Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        # Orientation of the ship
        self.rotation_right = False
        self.rotation_left = False
        

    
    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        # up and down
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        
        # Update rect object from self.x
        self.rect.x = self.x
        self.rect.y = self.y

        # Rotations
        if self.rotation_right == True:
            self.image = self.image_looking_right

        elif self.rotation_left == True:
            self.image = self.image_looking_left
        
        else:
            self.image = self.image_default
        
    def blitme(self):
        """Draw the ship at its curren location."""
        self.screen.blit(self.image, self.rect)
    
    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
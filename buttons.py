import pygame

easy_button = pygame.image.load('images/blue_button.bmp')
hard_button = pygame.image.load('images/red_button.bmp')

class Difficulty_Button:

    def __init__(self, ai_game, x, y, image, scale):

        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        width = image.get_width()
        height = image.get_height()
        
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self):
        # Draw button on the screen.
        self.screen.blit(self.image, (self.rect.x, self.rect.y))
    

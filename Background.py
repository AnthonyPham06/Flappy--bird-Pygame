import pygame

class background(pygame.sprite.Sprite):
    
    def __init__(self,x,y):
        super().__init__()
        self.original_image = pygame.image.load('background_sprite.png').convert_alpha()
        self.original_image = pygame.transform.scale(self.original_image,(int(self.original_image.get_width()*1.7),int(self.original_image.get_height()*1.6)))
        self.image = self.original_image
        self.rect = self.image.get_rect(center = (x,y))


    def scrolling_background(self):
        self.rect.x -= 2
        if self.rect.right <= 10:
            self.rect.left = self.rect.width

    def update(self):
        self.scrolling_background() 

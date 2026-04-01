import pygame

class obstacle(pygame.sprite.Sprite):

    def __init__(self, x,y,ratio, flipped = False):
        super().__init__()
        self.original_image = pygame.image.load("new_pipe.jpg").convert_alpha()

        if not flipped:
            self.original_image = pygame.transform.scale(self.original_image,(self.original_image.get_width()*0.8,self.original_image.get_height()*ratio))
        else:
            self.flipped_image = pygame.transform.flip(self.original_image, False,True)
            self.original_image = pygame.transform.scale(self.flipped_image,(self.flipped_image.get_width()*0.8,self.flipped_image.get_height()*ratio))
        
        self.image = self.original_image

        if not flipped:
            self.rect = self.image.get_rect(midbottom =(x,y))       
        else:
            self.rect = self.image.get_rect(midtop =(x,y))

        self.mask = pygame.mask.from_surface(self.image)



        self.score = 0 
        self.phongchu = pygame.font.Font('freesansbold.ttf', 32)
        self.score_checker = 0





    def update(self):
        self.rect.x -= 3
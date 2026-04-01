import pygame,sys

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        # store original image
        self.original_image = pygame.image.load('flappy.png').convert_alpha()
        self.original_image = pygame.transform.scale(self.original_image,(int(self.original_image.get_width() * 0.15),int(self.original_image.get_height() * 0.15)))
        self.image = self.original_image
        self.rect = self.image.get_rect(center=pos)
        self.mask = pygame.mask.from_surface(self.image)


        # physics
        self.velocity = 0
        self.gravity_force = 0.5
        self.max_fall_speed = 10

        # input cooldown
        self.click_cooldown = 170
        self.last_click_time = 0

    def apply_gravity(self):
        self.velocity += self.gravity_force
        if self.velocity > self.max_fall_speed:
            self.velocity = self.max_fall_speed
        self.rect.y += self.velocity

    def user_input(self):
        current_time = pygame.time.get_ticks()
        keys = pygame.key.get_pressed()
        if current_time - self.last_click_time >= self.click_cooldown:
            if keys[pygame.K_SPACE]:
                self.velocity = -8   # negative = upward
                self.last_click_time = current_time     

    def rotate(self):
        # tilt up when moving up, tilt down when falling
        angle = -self.velocity * 3
        self.image = pygame.transform.rotate(self.original_image, angle)
        # keep rect centered after rotation
        self.rect = self.image.get_rect(center=self.rect.center)

    def death(self):
        if self.rect.y >=750 or self.rect.y <=100:
            pygame.quit()
            print("YOU DIED")
            sys.exit()


    def update(self):
        self.user_input()
        self.apply_gravity()
        self.rotate()
        self.death()
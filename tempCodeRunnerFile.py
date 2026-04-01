import pygame, sys
from player import Player
from Background import background
from Obstacle import obstacle
import random

class Game:
    def __init__(self):
        player_sprite = Player((400, 500))
        self.player =pygame.sprite.GroupSingle(player_sprite)

        background_sprite1 = background(500,500)
        background_sprite2 = background(499+background_sprite1.rect.width,500)
        self.background = pygame.sprite.Group(background_sprite1, background_sprite2)

        pipe_sprite1 = obstacle(1000, 805,0.4, False)
        pipe_sprite2 = obstacle(1000, 135,0.4, True)
        self.pipe = pygame.sprite.Group(pipe_sprite1, pipe_sprite2)
        
        self.count = 0
        self.size_gap = 200
        self.gap_y =0
        self.passed_pipe =[]

        self.spawn_timer = 0 
        self.spawn_interval =40
        

        self.score = 0 

    def check_collision(self):
        if  pygame.sprite.spritecollide(self.player.sprite, self.pipe, False, pygame.sprite.collide_mask):
            pygame.quit()
            print("You died")
            sys.exit()


    def obstacle_creation(self):
        self.spawn_timer +=0.7
        if self.spawn_timer > self.spawn_interval:
            self.spawn_timer = 0
            self.count +=1 
            self.gap_y = random.uniform(0.2,0.5)
            
            pipe_sprite3 = obstacle(1000+300*self.count, 805, self.gap_y, False)
            pipe_sprite4 = obstacle(1000+300*self.count, 135, abs(0.85 - self.gap_y), True)
            self.pipe.add(pipe_sprite3, pipe_sprite4)


    def check_score(self):
        for pipe in self.pipe:
            if pipe.rect.right < self.player.sprite.rect.left and pipe not in self.passed_pipe:
                self.score +=1 
                self.passed_pipe.append(pipe)


 

    def run(self): #update and draw sprites
        self.background.update()
        self.background.draw(screen)

        self.player.update()
        self.player.draw(screen)

        self.pipe.update()
        self.pipe.draw(screen)

        self.check_collision()
        self.obstacle_creation()
        self.check_score()


 




if __name__ == "__main__":
    pygame.init()

    screen_width = 1000
    screen_height = 1000
    pygame.display.set_caption("Flappy Bird")
    phongchu = pygame.font.Font('freesansbold.ttf', 32)

    
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    game =Game()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill((30,30,30))
        game.run()
        text = phongchu.render("Score: "+ str(int(game.score/2)) , True, (255, 255, 255))
        screen.blit(text, (50,100))
        pygame.display.flip()
        clock.tick(60)

import pygame
import random
#model
class Hero(pygame.sprite.Sprite):
    def __init__(self, name, x, y, img_file):
        '''
        creates the hero, gives them an image, sets the speed in which it moves and the health of the hero
        name: str, the name of the hero
        x: int, x-coordinate of the hero
        y: int, y-coordinate of the hero
        img_file: str, the image you want the hero to look like
        '''
        #initialize all the Sprite functionality
        pygame.sprite.Sprite.__init__(self)

        #The following two attributes must be called image and rect
        #pygame assumes you have intitialized these values
        #and uses them to update the screen

        #create surface object image
        self.image = pygame.image.load(img_file).convert_alpha()
        #get the rectangle for positioning
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        #set other attributes
        self.name = name
        self.speed = 3
        self.health = 3

    #methods to make moving our hero easier
    def move_up(self):
        '''
        moves the hero up
        '''
        self.rect.y -= self.speed
    def move_down(self):
        '''
        moves the hero down
        '''
        self.rect.y += self.speed
    def move_left(self):
        '''
        moves the hero left
        '''
        self.rect.x -= self.speed
    def move_right(self):
        '''
        moves the hero right
        '''
        self.rect.x += self.speed

    def fight(self, opponent):
        '''
        when the hero touches the enemies, the hero either has a succesful attack and kills the enemy or his attack fails and his health goes down by 1
        opponent: src.enemy.Enemy, the enemy that the hero collides with
        '''
        if(random.randrange(3)):
            self.health -= 1
            print("attack failed. Remaining Health: ", self.health)
            return False
        else:
            print("successful attack")
        return True

import pygame
import random
#model
class Hero(pygame.sprite.Sprite):
    def __init__(self, name, x, y, img_file):
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
        moves the hero up when up arrow is pressed
        '''
        self.rect.y -= self.speed
    def move_down(self):
        '''
        moves the hero down when down arrow is pressed
        '''
        self.rect.y += self.speed
    def move_left(self):
        '''
        moves the hero left when left arrow is pressed
        '''
        self.rect.x -= self.speed
    def move_right(self):
        '''
        moves the hero right when right arrow is pressed
        '''
        self.rect.x += self.speed

    def fight(self, opponent):
        if(random.randrange(3)):
            self.health -= 1
            print("attack failed. Remaining Health: ", self.health)
            return False
        else:
            print("successful attack")
        return True

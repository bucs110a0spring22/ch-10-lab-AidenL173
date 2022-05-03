import pygame
import random
#model
class Enemy(pygame.sprite.Sprite):
    def __init__(self, name, x, y, img_file):
        '''
        creates the enemies, gives them an image, sets the speed in which they move and sets the name of the enemy
        name: str, the name of the enemies
        x: int, x-coordinate of the enemy
        y: int, y-coordinate of the enemy
        img_file: str, the image you want the enemy to look like
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
        self.name = name + str(id(self))
        self.speed = 2

    def update(self):
        '''
        makes the enemies move randomly
        '''
        # print("'Update me,' says " + self.name)
        self.rect.x += random.randint(-1,1)
        self.rect.y += random.randint(-1,1)

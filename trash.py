import pygame, random

class Trash(object):
    def __init__(self,screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y

        self.alltype = ["B","G","Y","O"]
        srcsNtypes = [["img/papier.png","B"],
                      ["img/szklo.png","G"],
                      ["img/plastik.png","Y"],
                      ["img/organiczne.png","O"],
                      ["img/organiczne2.png","O"]]
        rand = random.randint(0,len(srcsNtypes)-1)

        self.src, self.type = srcsNtypes[rand]
        self.speed = 15
        self.fall = False
        self.canset = False

    def display(self):
        texture = pygame.image.load(self.src)
        self.screen.blit(texture, (self.x,self.y))

    def drop(self):
        if self.fall:
            self.y += self.speed

    def set_cord(self, x, y):
        if self.canset:
            self.x = x
            self.y = y

    def check(self, data):
        if self.y >= 530:
            if data[0] < self.x < data[1] and self.type == self.alltype[data[2]]:
                self.set_cord(-500,-500)
                self.fall = False
                return True
        return False

    def score_minus(self):
        if self.y >= 535:
            self.set_cord(-500,-500)
            self.fall = False
            return True
        return False

    def take(self, posx):
        if self.x < posx:
            self.x += 5
        if self.x > posx:
            self.x -= 5
        if self.y > 155:
            self.y -= 15
        else:
            self.canset = True

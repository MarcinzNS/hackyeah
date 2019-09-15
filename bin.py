import pygame

class Bins(object):
    def __init__(self, screen, which, fromLeft):
        self.screen = screen
        self.x = fromLeft * 190 + 20
        self.y = 530
        self.alltype = ["B","G","Y","O"]
        self.combinatory = [
        [0,1,2,3],[0,1,3,2],[0,2,1,3],[1,0,2,3],
        [0,3,2,1],[2,1,0,3],[0,1,2,3],[3,2,1,0]
        ]
        src = ["img/Bb.png","img/Gb.png","img/Yb.png","img/Ob.png"]
        src_top = ["img/Bbp.png","img/Gbp.png","img/Ybp.png","img/Obp.png"]
        self.src = src[which]
        self.src_top = src_top[which]
        self.which = which

    def display(self):
        texture = pygame.image.load(self.src)
        self.screen.blit(texture, (self.x,self.y))

    def display_top(self):
        texture = pygame.image.load(self.src_top)
        self.screen.blit(texture, (self.x,self.y))

    def check(self):
        return (self.x,self.x+170, self.which)

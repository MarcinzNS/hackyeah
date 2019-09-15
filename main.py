import pygame, random, sys
import player, trash, bin

class MainGame(object):
    def __init__(self):
        pygame.init()

        #config
        self.lvl = 0
        self.tps_max = 90.0
        self.time = 0.0

        #inicjalizacja
        self.screen = pygame.display.set_mode((1200,700))#(1024,768))

        self.mpos = pygame.mouse.get_pos()
        self.mcheck = pygame.mouse.get_pressed()
        pygame.display.set_caption('Protect the environment by recycling!')
        self.tps_clock = pygame.time.Clock()
        self.tps_delta = 0.0

        #music
        self.ok = pygame.mixer.Sound('ok.wav')
        self.nok = pygame.mixer.Sound('nieok.wav')

        pygame.mixer.music.load('Triumph.wav')
        pygame.mixer.music.play(-1)

        #level 0
        self.bg_y = 700
        self.bin_y = 700
        self.player_y = -200

        #player
        self.player = player.Lemur(self.screen)
        self.score = 0

        #trash
        self.trashs = []
        self.howmuch = 0

        self.buff_x = 0
        self.buff_y = 0

        #bins
        self.combinatory = [
        [0,1,2,3],[2,1,3,0],[2,0,1,3],[1,0,2,3],
        [0,3,2,1],[2,1,0,3],[0,1,2,3],[3,2,1,0]
        ]

        i = self.combinatory[0]
        self.bins =[bin.Bins(self.screen,i[0],0),
                    bin.Bins(self.screen,i[1],1),
                    bin.Bins(self.screen,i[2],2),
                    bin.Bins(self.screen,i[3],3)]

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if self.howmuch == 1:
                            for i in self.trashs:
                                i.fall = True
                            self.howmuch = 0

            self.tps_delta += self.tps_clock.tick() / 1000.0
            while self.tps_delta > 1 / self.tps_max:
                if self.lvl == 1: self.animation_tick()
                if self.lvl == 2: self.tick()
                self.tps_delta -= 1 / self.tps_max
            self.time += 0.01

            #draw
            self.screen.fill((65, 194, 246))
            if self.lvl == 0: self.menu()
            if self.lvl == 1: self.animate()
            if self.lvl == 2: self.draw()
            pygame.display.flip()

    def menu(self):
        self.displayImage("img/bg-menu.png", 0, 0)
        self.text("Play",520,300, (0, 0, 0))
        self.mpos = pygame.mouse.get_pos()
        self.mcheck = pygame.mouse.get_pressed()
        if 520 < self.mpos[0] < 620 and 300 < self.mpos[1] < 350:
            if self.mcheck[0]:
                self.lvl = 1
            self.text("Play",520,300, (40, 40, 40))

    def animate(self):
        self.displayImage("img/bg.png", 0, self.bg_y)
        self.displayImage("img/player-right.png", 520, self.player_y)
        src = ["img/Bb.png","img/Gb.png","img/Yb.png","img/Ob.png"]
        for i in range(4):
            self.displayImage(src[i], i * 190 + 20, self.bin_y)

    def animation_tick(self):
        if self.bg_y > 0: self.bg_y -= 3
        else:
            self.bg_y = 0
            if self.bin_y > 530: self.bin_y -= 1
            else:
                self.bin_y = 530
                self.lvl = 2
            if self.player_y < 125: self.player_y += 2
            else: self.player_y = 125

    def draw(self):
        self.displayImage("img/bg.png", 0, 0)
        self.player.display(self.player.srcr)
        for i in self.bins:
            i.display()
        for i in self.trashs:
            i.display()
            i.drop()
            if i.score_minus():
                self.score -= 1
                self.nok.play()
                self.trashs.pop()
            if not i.fall:
                px = self.player.pos.x
                i.take(px)
                py = self.player.pos.y+30
                i.set_cord(px, py)
            for j in self.bins:
                if i.check(j.check()):
                    self.score += 1
                    self.ok.play()
                    self.trashs.pop()

        for i in self.bins:
            i.display_top()
        self.text(f"Score: {self.score}", 500, 0, (255,0,0), 50)
        #pygame.draw.rect(self.screen, (0, 100, 255), pygame.Rect(10,690,9,9))

    def displayImage(self, src, x, y):
        texture = pygame.image.load(src)
        self.screen.blit(texture, (x,y))

    def text(self,txt,x,y,c=(0, 0, 0), s=72):
        font = pygame.font.SysFont("ariel", s)
        text = font.render(txt, True, c)
        self.screen.blit(text, (x,y))

    def tick(self):
        self.player.move()
        if self.player.pos.x>800 and self.howmuch == 0:
            self.howmuch = 1
            self.trashs.append(trash.Trash( self.screen, 900, 520))
        if self.time > 30:
            if int(self.time)%4 == 0:
                self.newBin()
            if int(self.time*10)%42 == 0:
                self.time+=1

    def newBin(self):
        i = self.combinatory[random.randint(0,7)]
        self.bins =[bin.Bins(self.screen,i[0],0),
                    bin.Bins(self.screen,i[1],1),
                    bin.Bins(self.screen,i[2],2),
                    bin.Bins(self.screen,i[3],3)]

if "__main__" == __name__:
    MainGame()

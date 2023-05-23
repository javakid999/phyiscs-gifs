import pygame, math

class Screen:
    def __init__(self, dimensions, font_size=12):
        pygame.font.init()
        self.size = dimensions
        self.screen = pygame.Surface(dimensions)
        self.name = "default"
        
        self.font = pygame.font.Font('./Roboto/Roboto-Black.ttf', font_size)

    def add_display(self, dimensions):
        self.display = pygame.display.set_mode(dimensions)
        self.display_size = dimensions
        self.clock = pygame.time.Clock()

    def render(self, screen):
        screen.fill((0,0,0))

    def update(self):
        pass

    def save_animation(self, num_frames, interval=1):
        dir = "./"+self.name+"/"
        for i in range(num_frames):
            self.render(self.screen)
            pygame.image.save(self.screen, dir+str(i)+".png")
            for j in range(interval):
                self.update()

    def run_display(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            self.display.fill((0,0,0))
            self.render(self.screen)
            self.update()
            self.display.blit(pygame.transform.scale(self.screen, self.display_size),(0,0))
            pygame.display.update()

            self.clock.tick((60))
            pygame.display.set_caption(str(self.clock.get_fps()))
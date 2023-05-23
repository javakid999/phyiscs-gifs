import pygame, math
from animation import Keyframe, Animation
from screen import Screen

class Pendulum(Screen):
    def __init__(self, dimensions, font_size=12):
        super().__init__(dimensions, font_size)

        self.name = 'pendulum'
        self.g = -9.8
        self.angle = 120
        self.angular_velocity = 0
        self.length = 200
        self.origin = (512, 200)

    def update_angle(self):
        a_prev = self.angle * math.pi / 180
        self.angle = self.angle - self.angular_velocity * 0.01
        self.angular_velocity = self.angular_velocity - (self.g/self.length) * math.sin(a_prev) * 0.01

    def render(self, screen):
        super().render(screen)

        angle_rads = self.angle * math.pi / 180
        start = min(-angle_rads+3*math.pi/2, 3*math.pi/2)
        stop = max(-angle_rads+3*math.pi/2, 3*math.pi/2)
        pygame.draw.arc(screen, (255,255,255), (self.origin[0]-40, self.origin[1]-40,80,80), start, stop)
        for i in range(int(self.length/20)):
            pygame.draw.line(screen, (128,128,128), (self.origin[0], self.origin[1]+i*20), (self.origin[0], self.origin[1]+i*20+10))
        pygame.draw.aaline(screen, (255,255,255), self.origin, (self.origin[0]-self.length*math.sin(angle_rads),self.origin[1]+self.length*math.cos(angle_rads)))
        pygame.draw.circle(screen, (255,128,128), (self.origin[0]-self.length*math.sin(angle_rads),self.origin[1]+self.length*math.cos(angle_rads)), 20)
        angle = (-angle_rads*1.4+3*math.pi/2+3*math.pi/2)/2
        screen.blit(self.font.render("θ", True, (255,255,255)), (50*math.cos(angle)+self.origin[0]-8,50*math.sin(-angle)+self.origin[1]))

    def update(self):
        super().update()

        for i in range(100):
                self.update_angle()

pygame.init()

s = Pendulum((1024,1024), 25)
s.add_display((512,512))
s.save_animation(10, 20)
s.run_display()
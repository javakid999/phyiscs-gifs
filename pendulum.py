import pygame, math

pygame.init()

class Keyframe:
    def __init__(self, time, value):
        self.time = time
        self.value = value

class Animation:
    #animation types

    def __init__(self):
        self.keyframes = []

    def add_keyframes(self, values, times):
        if len(values) != len(times): return
        for i in range(len(values)):
            for j in range(len(self.keyframes)):
                if self.keyframes[j].time >= times[i]:
                    self.keyframes.insert(j, Keyframe(times[i], values[i]))
                    break

    def get_value(self, time):
        for i in range(len(self.keyframes)):
                if self.keyframes[i].time == time:
                    return self.keyframes[i].value
                elif self.keyframes[i].time < time:
                    pass


class Screen:
    def __init__(self):
        self.display = pygame.display.set_mode((512,512))
        self.clock = pygame.time.Clock()
        self.g = -9.8
        self.angle = 50
        self.angular_velocity = 0
        self.length = 100
        self.origin = (256, 100)
        self.run()

    def update_angle(self):
        a_prev = self.angle * math.pi / 180
        self.angle = self.angle - self.angular_velocity * 0.01
        self.angular_velocity = self.angular_velocity - (self.g/self.length) * math.sin(a_prev) * 0.01

    def render(self):
        self.display.fill((0,0,0))
        angle_rads = self.angle * math.pi / 180
        start = min(-angle_rads+3*math.pi/2, 3*math.pi/2)
        stop = max(-angle_rads+3*math.pi/2, 3*math.pi/2)
        pygame.draw.arc(self.display, (255,255,255), (self.origin[0]-10, self.origin[1]-10,20,20), start, stop)
        for i in range(int(self.length/20)):
            pygame.draw.line(self.display, (128,128,128), (self.origin[0], self.origin[1]+i*20), (self.origin[0], self.origin[1]+i*20+10))
        pygame.draw.aaline(self.display, (255,255,255), self.origin, (self.origin[0]-self.length*math.sin(angle_rads),self.origin[1]+self.length*math.cos(angle_rads)))
        pygame.draw.circle(self.display, (255,128,128), (self.origin[0]-self.length*math.sin(angle_rads),self.origin[1]+self.length*math.cos(angle_rads)), 10)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            for i in range(100):
                self.update_angle()
            self.render()
            pygame.display.update()
            self.clock.tick((60))
            pygame.display.set_caption(str(self.clock.get_fps()))

s = Screen()
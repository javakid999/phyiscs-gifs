import math

class Keyframe:
    INTERPOLATION_TYPE = {
        'linear': lambda a, b, t: (1-t)*a+b*t,
        'quadratic': lambda a, b, t: (b-a)*(t*t)+a,
        'cosine': lambda a, b, t: (1 - (1-math.cos(t*math.pi))/2) * a + (1-math.cos(t*math.pi))/2 * b,
        'smoothstep': lambda a, b, t: t * t * (3 - 2 * t),
        'smootherstep': lambda a, b, t: t * t * t * (3 * t * (2 * t - 5) + 10)
    }

    def __init__(self, initial, final, duration, function=INTERPOLATION_TYPE['linear']):
        self.initial = initial
        self.final = final
        self.duration = duration
        self.function = function

    def getValue(self, time):
        if isinstance(self.initial, float):
            return self.function(self.initial, self.final, time/self.duration)
        elif isinstance(self.initial, tuple):
            t = []
            for i in range(len(self.initial)):
                t.append(self.function(self.initial[i], self.final[i], time/self.duration))
            return (*t,)


class Animation:
    def __init__(self):
        self.paths = []
    def addPath(self, path):
        self.paths.append(path)
    def getValue(self, time):
        startTime = 0
        for path in self.paths:
            if time < startTime + path.duration and time >= startTime:
                return path.getValue(time-startTime)
            else:
                startTime += path.duration
    def length(self):
        total = 0
        for path in self.paths:
            total += path.duration
        return total
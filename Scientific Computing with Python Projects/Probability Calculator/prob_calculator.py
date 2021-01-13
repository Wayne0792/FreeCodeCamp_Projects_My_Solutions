import copy
import random
from collections import Counter
# Consider using the modules imported above.
class Hat:
    def __init__(self, **args):
        self.contents = []
        for color in args:
            self.contents += args[color]*[color]
    
    def draw(self, n):
        if n > len(self.contents):
            return self.contents
        output = []
        while n > 0:
            e = random.choice(self.contents)
            self.contents.remove(e)
            output.append(e)
            n -= 1
        return output

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    n = 0
    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        sample = Counter(hat.draw(num_balls_drawn))
        sucess = True
        for color in expected_balls:
            if not ((color in sample) and (sample[color] >= expected_balls[color])):
                sucess = False
                break
        if sucess:
            n += 1
        hat = hat_copy
    return n/num_experiments


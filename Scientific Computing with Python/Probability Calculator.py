import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.hat = kwargs 
        content = []
        for color, quantity in self.hat.items():
            while quantity != 0:
                content.append(color)
                quantity-=1
        self.contents = content
    
    def draw(self, drawAmount):
        if len(self.contents) < drawAmount:
            return self.contents
        colorsDrawn = []
        while drawAmount != 0:
            colorChosen = random.choice(self.contents) # picks color from color list
            colorsDrawn.append(colorChosen)
            self.contents.remove(colorChosen) # subtracts color from balls left
            drawAmount -=1
        return colorsDrawn
    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0
    counter = 0
    hat_copy = copy.deepcopy(hat.contents)
    while num_experiments > counter: #iterates 2000 times
        list = hat.draw(num_balls_drawn) #draw number of balls
        experiment = {}
        for color in list:
            if color in experiment:
                experiment[color] += 1
            else:
                experiment[color] = 1
        x = 0
        for color in experiment:
            if color in expected_balls:
                if experiment[color] >= expected_balls[color]:
                    x+=1
        if x == len(expected_balls):
            m+=1
        hat.contents = copy.deepcopy(hat_copy)
        list.clear()
        counter+=1
    probability = f"{m/num_experiments:.3f}"
    return probability

def main():
    hat = Hat(black=6, red=4, green=3)
    probability = experiment(hat=hat,
                expected_balls={"red":2,"green":1},
                num_balls_drawn=5,
                num_experiments=2000)
    print(probability)

main()
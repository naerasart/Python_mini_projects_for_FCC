import copy
import random


class Hat:
    def __init__(self, **args):
        self.contents = list()
        for color in args.keys():
            for number in range(args[color]):
                self.contents.append(color)
         
 
    def draw(self, number):         
        sample = list()
        if number > len(self.contents):
            return self.contents
            sample=0
        elif number == len(self.contents):
            return self.contents 
            sample=0                    
        elif  number < len(self.contents):
         for n in range(number):              
          sample.append(self.contents.pop(random.randrange(len(self.contents))))
        return sample


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = int()
    Failure = False
    for n in range(num_experiments):         
        success = (copy.deepcopy(hat)).draw(num_balls_drawn)
        Failure = False
        
        for numbers in expected_balls.keys():          
            if success.count(numbers) < expected_balls[numbers]:
                Failure = True 
                count += 0
        if Failure is False:
            count += 1
            Failure = False
    probability=float(count / num_experiments)
    return probability
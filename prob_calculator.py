import copy
import random
# Consider using the modules imported above.


class Hat:
    def __init__(self, **balls):
        self.contents = []
        self.create_contents(balls)

    def create_contents(self, balls):
        for ball_color, ball_amount in balls.items():
            for ball in range(ball_amount):
                self.contents.append(ball_color)

    def draw(self, draw_amount):
        if len(self.contents) > draw_amount:
            drawn_balls = random.sample(self.contents, k=draw_amount)
            for ball in drawn_balls:
                self.contents.remove(ball)
            return drawn_balls
        else:
            return self.contents


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    times_right = 0
    wanted_balls = Hat(**expected_balls).contents
    for experiment in range(num_experiments):
        new_hat = copy.deepcopy(hat)
        drawn_balls = new_hat.draw(num_balls_drawn)

        for ball in wanted_balls:
            if ball in drawn_balls:
                drawn_balls.remove(ball)
            else:
                break
        else:
            times_right += 1

    return times_right / num_experiments

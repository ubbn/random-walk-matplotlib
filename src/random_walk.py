from random import choice


class RandomWalk:
    """Class for generating random walk"""

    def __init__(self, num_points=50000):
        self.num_points = num_points

        # All walks start from (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all the points in the walk"""

        # Keep walking until desired length is passed
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()

            # Reject moves going nowhere
            if x_step == 0 and y_step == 0:
                continue

            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

    def get_step(self):
        # choose value randomly from given list
        direction = choice([1, -1])
        # choose value randomly from given list
        distance = choice([0, 1, 2, 3, 4])
        return direction * distance

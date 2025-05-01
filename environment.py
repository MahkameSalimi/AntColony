import numpy as np
import matplotlib.pyplot as plt
class Environment:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pheromones = np.zeros((width, height))
        self.food = np.zeros((width, height), dtype=bool)
        self.nest = (width // 2, height // 2)

    def evaporate_pheromones(self, rate=0.01):
        self.pheromones *= (1 - rate)

    def place_food_randomly(self, count=5, min_distance=5):
        candidates = []

        for x in range(self.width):
            for y in range(self.height):
                dx = x - self.nest[0]
                dy = y - self.nest[1]
                distance = np.sqrt(dx ** 2 + dy ** 2)
                if distance >= min_distance:
                    candidates.append((x, y))

        if len(candidates) < count:
            raise ValueError("Not enough valid positions to place food.")

        selected_positions = np.random.choice(len(candidates), size=count, replace=False)
        for idx in selected_positions:
            x, y = candidates[idx]
            self.food[x, y] = True

    def show(self):
        fig, ax = plt.subplots()

        # Show pheromone levels as background heatmap (gray)
        pheromone_img = ax.imshow(self.pheromones.T, cmap='Greys', origin='lower', alpha=0.5)

        # Overlay food as green squares
        food_x, food_y = np.where(self.food)
        ax.scatter(food_x, food_y, c='lime', marker='s', s=100, label='Food')

        # Overlay nest as red square
        ax.scatter(*self.nest, c='red', marker='s', s=100, label='Nest')

        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_title('Environment (Pheromones + Food + Nest)')
        ax.legend(loc='upper right')
        plt.show()

env = Environment(20, 20)
env.place_food_randomly(count=10)
env.pheromones[5:10, 5:15] = 1.0  # add some test pheromones
env.show()
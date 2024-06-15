import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Lattice:
    def __init__(self, size):
        self.size = size
        self.grid = np.zeros((size, size), dtype=int)
        self.start = (size // 2, size // 2)
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # East, South, West, North

    def initialize_saw(self):
        self.grid[self.start] = 1
        self.current_pos = self.start
        self.steps = [self.current_pos]

    def is_valid_move(self, move):
        new_pos = tuple(np.add(self.current_pos, move))
        return 0 <= new_pos[0] < self.size and 0 <= new_pos[1] < self.size and self.grid[new_pos] == 0

    def move(self, move):
        self.current_pos = tuple(np.add(self.current_pos, move))
        self.grid[self.current_pos] = len(self.steps) + 1
        self.steps.append(self.current_pos)

    def get_choices(self):
        choices = [direction for direction in self.directions if self.is_valid_move(direction)]
        return choices

    def generate_saw(self):
        while True:
            choices = self.get_choices()
            if not choices:
                break
            move = random.choice(choices)
            self.move(move)

    def visualize_animation(self):
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.set_title(f"Self-Avoiding Walk on a {self.size}x{self.size} Lattice")
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.grid(True)

        mat = ax.matshow(self.grid, cmap=plt.get_cmap('viridis'), vmin=0, vmax=len(self.steps))

        def update(frame):
            if frame < len(self.steps):
                mat.set_data(np.where(self.grid == frame + 1, frame + 1, 0))
            else:
                mat.set_data(self.grid)
            return [mat]

        ani = animation.FuncAnimation(fig, update, frames=len(self.steps) + 10, blit=True, repeat=False)
        plt.show()

class SquareLattice(Lattice):
    def __init__(self, size):
        super().__init__(size)

def main():
    size = 51  # Default size of the lattice
    lattice = SquareLattice(size)
    lattice.initialize_saw()
    lattice.generate_saw()
    lattice.visualize_animation()

if __name__ == "__main__":
    main()
import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Lattice:
    """
    Represents a self-avoiding walk on a square lattice.
    """
    def __init__(self, size):
        """
        Initializes the lattice with the given size.

        Parameters:
        size (int): The size of the lattice (size x size).
        """
        self.size = size
        self.grid = np.zeros((size, size), dtype=int)
        self.start = (size // 2, size // 2)
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # East, South, West, North
        self.current_pos = self.start
        self.steps = []

    def initialize_saw(self):
        """
        Initializes the self-avoiding walk by setting the starting point.
        """
        self.grid[self.start] = 1
        self.current_pos = self.start
        self.steps = [self.current_pos]

    def is_valid_move(self, move):
        """
        Checks if a move is valid (within the grid and not revisiting a point).

        Parameters:
        move (tuple): The move to check.

        Returns:
        bool: True if the move is valid, False otherwise.
        """
        new_pos = tuple(np.add(self.current_pos, move))
        return 0 <= new_pos[0] < self.size and 0 <= new_pos[1] < self.size and self.grid[new_pos] == 0

    def move(self, move):
        """
        Makes a move and updates the grid and steps.

        Parameters:
        move (tuple): The move to make.
        """
        self.current_pos = tuple(np.add(self.current_pos, move))
        self.grid[self.current_pos] = len(self.steps) + 1
        self.steps.append(self.current_pos)

    def get_choices(self):
        """
        Gets the list of valid moves from the current position.

        Returns:
        list: List of valid moves.
        """
        choices = [direction for direction in self.directions if self.is_valid_move(direction)]
        return choices

    def generate_saw(self):
        """
        Generates a self-avoiding walk by randomly choosing valid moves until no more moves are possible.
        """
        while True:
            choices = self.get_choices()
            if not choices:
                break
            move = random.choice(choices)
            self.move(move)

    def visualize_animation(self, interval=50):
        """
        Visualizes the self-avoiding walk with an animation.

        Parameters:
        interval (int): The interval between frames in milliseconds.
        """
        fig, ax = plt.subplots(figsize=(8, 8))
        fig.patch.set_facecolor('white')  # Set figure background to white
        ax.set_facecolor('white')  # Set axes background to white
        ax.set_title(f"Self-Avoiding Walk on a {self.size}x{self.size} Square Lattice", color='black')
        ax.set_xlabel('X', color='black')
        ax.set_ylabel('Y', color='black')
        ax.grid(True, color='grey', linestyle='--', linewidth=0.5)

        mat = ax.matshow(self.grid, cmap=plt.get_cmap('viridis'), vmin=0, vmax=len(self.steps))

        def update(frame):
            if frame < len(self.steps):
                # Show all steps up to the current frame
                mat.set_data(np.where(self.grid <= frame + 1, self.grid, 0))
                steps_so_far = np.array(self.steps[:frame + 1])
                ax.plot(steps_so_far[:, 1], steps_so_far[:, 0], 'lightgrey', linewidth=0.5)
                ax.plot(steps_so_far[:, 1], steps_so_far[:, 0], 'black', linewidth=1)
            else:
                mat.set_data(self.grid)
                steps_so_far = np.array(self.steps)
                ax.plot(steps_so_far[:, 1], steps_so_far[:, 0], 'lightgrey', linewidth=0.5)
                ax.plot(steps_so_far[:, 1], steps_so_far[:, 0], 'black', linewidth=1)
                if frame == len(self.steps):
                    print(f"Final Path length: {len(self.steps)}")

            return [mat]

        ani = animation.FuncAnimation(fig, update, frames=len(self.steps) + 10, interval=interval, blit=True, repeat=False)
        plt.show()

class SquareLattice(Lattice):
    """
    Represents a square lattice for the self-avoiding walk.
    """
    def __init__(self, size):
        super().__init__(size)

def main():
    """
    The main function to run the self-avoiding walk simulation.
    """
    try:
        size = 51  # Default size of the lattice
        lattice = SquareLattice(size)
        lattice.initialize_saw()
        lattice.generate_saw()
        lattice.visualize_animation(interval=30)  # Set faster animation speed
    except Exception as e:
        print("An error occurred during the simulation:", str(e))

if __name__ == "__main__":
    main()
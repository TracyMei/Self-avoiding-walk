import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Lattice:
    def __init__(self, size):
        """
        Initialize the Lattice class with a given grid size.
        :param size: The size of the grid, i.e., size x size
        """
        self.size = size
        self.grid = np.zeros((size, size), dtype=int)  # Create a size x size grid filled with zeros
        self.start = (size // 2, size // 2)  # Set the starting point to the center of the grid
        # Directions: East, South, West, North
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def initialize_saw(self):
        """
        Initialize the self-avoiding walk (SAW) by setting the start point, current position, and steps.
        """
        self.grid[self.start] = 1  # Mark the start point as visited
        self.current_pos = self.start  # Set the current position to the start point
        self.steps = [self.current_pos]  # Record the steps taken

    def is_valid_move(self, move):
        """
        Check if a move in the given direction is valid.
        :param move: The direction to move, in the form (dx, dy)
        :return: True if the move is valid, otherwise False
        """
        new_pos = tuple(np.add(self.current_pos, move))  # Calculate the new position
        # Check if the new position is within grid bounds and has not been visited
        return 0 <= new_pos[0] < self.size and 0 <= new_pos[1] < self.size and self.grid[new_pos] == 0

    def move(self, move):
        """
        Perform a move and update the grid and current position.
        :param move: The direction to move, in the form (dx, dy)
        """
        self.current_pos = tuple(np.add(self.current_pos, move))  # Update the current position
        # Mark the current position as visited and record the steps
        self.grid[self.current_pos] = len(self.steps) + 1
        self.steps.append(self.current_pos)  # Append the new position to the steps record

    def get_choices(self):
        """
        Get all valid movement choices.
        :return: A list of valid movements
        """
        choices = [direction for direction in self.directions if self.is_valid_move(direction)]
        return choices

    def generate_saw(self):
        """
        Generate a self-avoiding walk (SAW) until no more moves are possible.
        """
        while True:
            choices = self.get_choices()  # Get all valid movement choices
            if not choices:
                break  # Terminate if no valid choices are available
            move = random.choice(choices)  # Randomly choose a direction to move
            self.move(move)  # Perform the move

    def visualize_animation(self):
        """
        Visualize the self-avoiding walk (SAW) as an animation.
        """
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.set_title(f"Self-Avoiding Walk on a {self.size}x{self.size} Lattice")
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.grid(True)

        # Display the grid using matshow
        mat = ax.matshow(self.grid, cmap=plt.get_cmap('viridis'), vmin=0, vmax=len(self.steps))

        def update(frame):
            """
            Update each frame in the animation.
            :param frame: The index of the current frame
            :return: The updated image object
            """
            if frame < len(self.steps):
                mat.set_data(np.where(self.grid == frame + 1, frame + 1, 0))
            else:
                mat.set_data(self.grid)
            return [mat]

        # Create the animation
        ani = animation.FuncAnimation(fig, update, frames=len(self.steps) + 10, blit=True, repeat=False)
        plt.show()

class SquareLattice(Lattice):
    def __init__(self, size):
        """
        Initialize the SquareLattice class, inheriting from the Lattice class.
        :param size: The size of the grid
        """
        super().__init__(size)

def main():
    size = 51  # Default size of the lattice
    lattice = SquareLattice(size)
    lattice.initialize_saw()  # Initialize the self-avoiding walk
    lattice.generate_saw()  # Generate the self-avoiding walk
    lattice.visualize_animation()  # Visualize the self-avoiding walk

if __name__ == "__main__":
    main()
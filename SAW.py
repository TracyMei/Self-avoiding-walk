import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
from docopt import docopt

class Lattice:
    def __init__(self, size):
        self.size = size
        self.grid = np.zeros((size, size))
        self.i, self.j = size // 2, size // 2
        self.grid[self.i, self.j] = 1
        self.counter = 1
        self.sequence = []

    def get_choices(self):
        choices = []
        if self.i-1 >= 0 and self.grid[self.i-1, self.j] == 0:
            choices.append("North")
        if self.j+1 < self.grid.shape[1] and self.grid[self.i, self.j+1] == 0:
            choices.append("East")
        if self.i+1 < self.grid.shape[0] and self.grid[self.i+1, self.j] == 0:
            choices.append("South")
        if self.j-1 >= 0 and self.grid[self.i, self.j-1] == 0:
            choices.append("West")
        return choices

    def grow(self, lower_bound):
        while True:
            self.grid = np.zeros((self.size, self.size))
            self.i, self.j = self.size // 2, self.size // 2
            self.counter = 1
            self.grid[self.i, self.j] = self.counter
            self.sequence = []
            choices = self.get_choices()

            while len(choices) > 0:
                self.counter += 1
                move = random.choice(choices)
                self.sequence.append(move)
                if move == "North":
                    self.i -= 1
                elif move == "East":
                    self.j += 1
                elif move == "South":
                    self.i += 1
                elif move == "West":
                    self.j -= 1
                self.grid[self.i, self.j] = self.counter
                choices = self.get_choices()

            if len(self.sequence) >= lower_bound:
                break

        self.sequence.append("Stay")
        return self.sequence, self.grid
       
    def update(self, frame, mat, verbose=False):
        move = self.sequence[frame]
        if move != "Stay":
            if verbose:
                print(move, end=" ")
            if move == "North":
                self.i -= 1
            elif move == "East":
                self.j += 1
            elif move == "South":
                self.i += 1
            elif move == "West":
                self.j -= 1
            self.grid[self.i, self.j] = self.counter
        else:
            self.counter -= 1

        mat.set_data(self.grid)
        return [mat]

class SquareLattice(Lattice):
    def __init__(self, size):
        super().__init__(size)
    
    def visualize(self):
        # 特殊的方形晶格绘制逻辑
        pass

class HoneycombLattice(Lattice):
    def __init__(self, size):
        super().__init__(size)

    def get_choices(self):
        # 特殊的蜂巢晶格移动逻辑
        choices = super().get_choices()
        # 扩展蜂巢格特有的选择规则
        # 这里仅提供示例，具体规则尚需根据蜂巢格特点调整
        if (self.i + self.j) % 2 == 0:  # 示例规则展示
            if self.i-1 >= 0 and self.j-1 >= 0 and self.grid[self.i-1, self.j-1] == 0:
                choices.append("Northwest")
            if self.i+1 < self.grid.shape[0] and self.j+1 < self.grid.shape[1] and self.grid[self.i+1, self.j+1] == 0:
                choices.append("Southeast")
        else:
            if self.i-1 >= 0 and self.j+1 < self.grid.shape[1] and self.grid[self.i-1, self.j+1] == 0:
                choices.append("Northeast")
            if self.i+1 < self.grid.shape[0] and self.j-1 >= 0 and self.grid[self.i+1, self.j-1] == 0:
                choices.append("Southwest")
        return choices

    def visualize(self):
        # 特殊的蜂巢晶格绘制逻辑
        pass

def main():
    """Self-Avoiding Paths Visualizer

    Usage:
      selfavoidance.py [options]
      selfavoidance.py (-h | --help)
      selfavoidance.py --version

    Options:
      -l --lower <int>     Sets a lower bound on the length of the random walk.
                           [default: 0]
      -n --size <int>      Width/Height of the lattice containing the random walk.
                           [default: 51]
      -m --ms <int>        Milliseconds between frames in the animation.
                           [default: 50]
      -c --cmap <string>   Colormap to use.
                           [default: jet]
      -t --type <string>   Type of lattice (e.g. square, honeycomb).
                           [default: square]
      -h --help            Show this screen.
      -v --verbose         Show runtime info.
      --version            Show version.
    """
    docstring = main.__doc__
    if docstring is None:
        raise ValueError("Docstring is missing")
    arguments = docopt(docstring, version="Self-Avoiding Paths Visualizer 1.1")
    lower_bound = int(arguments["--lower"])
    n = int(arguments["--size"])
    ms = int(arguments["--ms"])
    cmap = arguments["--cmap"]
    lattice_type = arguments["--type"].lower()
    verbose = arguments.get("--verbose", False)
    
    if lattice_type == "honeycomb":
        lattice = HoneycombLattice(n)
    else:
        lattice = SquareLattice(n)
    
    sequence, grid = lattice.grow(lower_bound)
    
    fig, ax = plt.subplots()
    mat = ax.matshow(grid, cmap=plt.get_cmap(cmap), vmin=0, vmax=len(sequence))
    
    if verbose:
        print(f"Number of moves: {len(sequence) - 1}")
        print(f"Sequence of moves: ", end="")

    ani = animation.FuncAnimation(fig, lattice.update, fargs=(mat, verbose), interval=ms, frames=len(sequence), blit=True, repeat=False)
    plt.show()

if __name__ == "__main__":
    main()
import numpy as np
import matplotlib.pyplot as plt
import random
from matplotlib.animation import FuncAnimation

class HexagonalLattice:
    def __init__(self, grid_size=20):
        """
        Initialize the hexagonal lattice.
        
        :param grid_size: Parameter to control the overall grid size.
        """
        self.grid_size = grid_size
        self.vertices = set()  # Set to store hexagonal vertices only
        self.saw_path = []  # List to store SAW path as tuples
        self.edges = {}  # Dictionary to store edges between hexagon vertices without duplication
        self._initialize_grid()
        self._start_saw()

    def _initialize_grid(self):
        """
        Initialize the hexagonal grid.
        """
        size = 1  # Size of hexagon
        rows = self.grid_size
        cols = self.grid_size
        hex_height = np.sqrt(3) * size  # Height of hexagon

        for row in range(rows):
            for col in range(cols):
                center_x = col * 1.5 * size  # Calculate hexagon center x-coordinate
                center_y = row * hex_height + (col % 2) * (hex_height / 2)  # Calculate hexagon center y-coordinate
                vertices = self._hexagon_vertices((center_x, center_y), size)
                self.vertices.update(vertices)
                for i in range(len(vertices)):
                    edge = tuple(sorted((vertices[i], vertices[(i+1) % len(vertices)])))
                    self.edges[edge] = True  # Use dictionary to avoid duplicate edges

    def _hexagon_vertices(self, center, size):
        """
        Compute the vertices of a hexagon.
        
        :param center: Center coordinates of the hexagon.
        :param size: Size (radius) of the hexagon.
        :return: List of hexagon vertices.
        """
        angles = np.linspace(0, 2 * np.pi, 7)  # 7 points to close the hexagon (0 and 2π are the same point)
        return [(center[0] + size * np.cos(angle), center[1] + size * np.sin(angle)) for angle in angles[:-1]]

    def _start_saw(self):
        """
        Start the Self-Avoiding Walk (SAW).
        """
        vertices_list = list(self.vertices)
        start_point = random.choice(vertices_list)
        self.saw_path.append(start_point)
        self._generate_saw()

    def _generate_saw(self):
        """
        Generate the Self-Avoiding Walk path.
        """
        while True:
            current_point = self.saw_path[-1]
            neighbors = self._get_neighbors(current_point)
            if not neighbors:  # No further steps possible
                break
            new_point = random.choice(neighbors)
            self.saw_path.append(new_point)

    def _get_neighbors(self, point):
        """
        Get the neighboring vertices of a given point.
        
        :param point: The current point coordinates.
        :return: List of neighboring points.
        """
        neighbors = []
        for edge in self.edges:
            if np.allclose(point, edge[0]):
                neighbor = edge[1]
            elif np.allclose(point, edge[1]):
                neighbor = edge[0]
            else:
                continue
            if not any(np.allclose(neighbor, p) for p in self.saw_path):
                neighbors.append(neighbor)
        return neighbors

    def visualize(self):
        """
        Visualize the Self-Avoiding Walk on the hexagonal lattice.
        """
        fig, ax = plt.subplots(figsize=(10, 10))

        # Plot hexagonal lattice
        for edge in self.edges:
            line = np.array(edge)
            ax.plot(line[:, 0], line[:, 1], 'k-')

        # Prepare for animation
        path_line, = ax.plot([], [], 'ro-', linewidth=2, markersize=4, markeredgewidth=2, markerfacecolor='r')
        ax.set_aspect('equal')
        ax.set_title("Self-Avoiding Walk on Hexagonal Lattice")
        ax.set_xticks([])
        ax.set_yticks([])

        def init():
            path_line.set_data([], [])
            return path_line,

        def update(frame):
            path = np.array(self.saw_path[:frame+1])
            path_line.set_data(path[:, 0], path[:, 1])
            return path_line,

        ani = FuncAnimation(fig, update, frames=len(self.saw_path), init_func=init, blit=True, repeat=False)

        plt.show()
        self._show_final_path_length()

    def _show_final_path_length(self):
        """
        Display the final path length.
        """
        print(f"Final Path length = {len(self.saw_path)}")

# Example usage
if __name__ == "__main__":
    hex_lattice = HexagonalLattice()
    hex_lattice.visualize()
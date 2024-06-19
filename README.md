# Self-Avoiding Walks (SAW) Simulation

## Introduction
This repository contains Python scripts to simulate Self-Avoiding Walks (SAW) on hexagonal and square lattice structures. SAW is a fundamental concept in mathematics and computational physics, representing a path on a lattice where no point is visited more than once.

### Key Concepts
In mathematics, a SAW is defined as a sequence of moves on a lattice that does not revisit any point. This path is crucial in graph theory and has applications in modeling polymers and protein structures.

#### Properties and Applications
SAWs and Self-Avoiding Polygons (SAPs), closed SAWs, play a significant role in understanding the topological properties of molecules like proteins. They are fractals, exhibiting specific dimensions in different dimensions of space (d).

#### Computational Techniques
Due to the complexity of calculating SAW properties analytically, numerical simulations are essential. Techniques like the pivot algorithm are used for Monte Carlo simulations to generate SAWs efficiently.

#### Universality
SAWs exhibit universality, where macroscopic properties are independent of microscopic details like lattice structure. The connective constant μ, defining growth rates of SAWs, varies with lattice type and is a critical concept in statistical physics.

## Dependencies
- 'numpy': Fundamental package for numerical computing.
- 'matplotlib': Plotting library for visualizations.
- 'random': Python's built-in module for random number generation.
- 'matplotlib.animation.FuncAnimation': For animating the SAW path generation process.

## Installation
To run this project locally, ensure you have Python 3.x installed along with the dependencies mentioned above and the following libraries(You can install them using pip):

- numpy
- matplotlib

```bash
pip install numpy matplotlib
```

## Usage
Clone this repository or download the files.

Run the scrip:

For Hexagonal lattice:
```bash
python Hex_SAW.py
```
For Square lattice:
```bash
python Square_SAW.py
```

The visualization of the SAW path on square lattice/hexagonal lattice will appear.

## Explanation of Algorithms
### Square SAW Algorithm (Square_SAW.py)
- Lattice Initialization (_initialize_grid method): Initializes a square lattice grid with vertices.

- SAW Generation (_start_saw and _generate_saw methods): Begins from a randomly chosen vertex and extends the path using a random walk algorithm. Ensures each step avoids revisiting previous vertices.

- Visualization (visualize method): Uses matplotlib to animate and display the SAW path on the square lattice.

- Final Path Length (_show_final_path_length method): Prints the total length of the generated SAW path.

### Hexagonal SAW Algorithm (Hex_SAW.py)
- Lattice Initialization (_initialize_grid method): Initializes a hexagonal lattice grid with vertices using geometric calculations for hexagons.

- SAW Generation (_start_saw and _generate_saw methods): Starts from a randomly chosen vertex and extends the path using a random walk algorithm. Improves efficiency by leveraging the geometry of hexagons to reduce redundant checks, compared to the square lattice.

- Visualization (visualize method): Animates and displays the SAW path on the hexagonal lattice using matplotlib.

- Final Path Length (_show_final_path_length method): Outputs the total length of the generated SAW path.

### Algorithmic Advantages of Hexagonal Lattice
- Geometry Utilization: Hexagonal lattice structure naturally reduces the number of neighboring checks (compared to square lattice), improving computational efficiency.

- Reduced Redundancy: By utilizing hexagon geometry in _get_neighbors method, redundant checks for adjacent vertices are minimized, enhancing performance especially for larger grids.

- Visual Aesthetics: The hexagonal lattice visually complements the fractal nature of SAWs better than the square lattice, providing a more intuitive representation of the path.

## License

This project is licensed under the Creative Commons Attribution-NonCommercial 4.0 International License. To view a copy of this license, visit [https://creativecommons.org/licenses/by-nc/4.0/](https://creativecommons.org/licenses/by-nc/4.0/).

### Attribution

This code is authored by Tracy Mei and Tongxin Hu.

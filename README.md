# Self-Avoiding Walks (SAW) Simulation

## Introduction
This Python script demonstrates a hexagonal lattice and generates a Self-Avoiding Walk (SAW) path on it. The SAW algorithm ensures no vertex is revisited during the path generation, making it a useful model in polymer physics and lattice theory.

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
Clone this repository or download the hexagonal_lattice.py file.
Run the script:
```bash
python Hex_SAW.py
```
The visualization of the SAW path on the hexagonal lattice will appear.

## Features
- Hexagonal Lattice Initialization: Generates a hexagonal grid based on a specified grid size.
- Self-Avoiding Walk (SAW) Algorithm: Implements the algorithm to generate a path that avoids revisiting vertices.
- Visualization: Provides a graphical representation of the SAW path using matplotlib.
- Path Length Display: Prints the final length of the SAW path generated.

## License

This project is licensed under the Creative Commons Attribution-NonCommercial 4.0 International License. To view a copy of this license, visit [https://creativecommons.org/licenses/by-nc/4.0/](https://creativecommons.org/licenses/by-nc/4.0/).

### Attribution

This code is authored by Tracy Mei and Tongxin Hu.

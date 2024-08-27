# EM Virtual Playground
# Project Description
The EM Virtual Playground is an interactive tool designed to visualize the generation, propagation, and interaction of electromagnetic (EM) waves with various environments. It features a user-friendly graphic interface where users can set up virtual experiments and visualize physical results in real-time. The Playground consists of two main components:

Foreground (GUI): Users can configure experimental setups, including different sources, materials, and geometries, to observe various EM phenomena like antenna radiation, wave scattering, and diffraction.
Background (Engine): Handles the scientific computations required to numerically simulate the experiments.
The Playground is intended as a teaching aid, enabling students to perform virtual experiments and gain insights into complex EM processes. Future enhancements will introduce a multiphysics component, online/mobile accessibility, and high-performance computing capabilities.

My Contribution
In this project, I focused on developing the initial computational components that will be integrated into the Playground’s engine. Specifically, I implemented foundational Python scripts for visualizing vector fields, which are essential for understanding EM wave behavior. These scripts can generate and animate vectors in 2D space, showcasing how vectors interact and transform, a concept that underpins many EM phenomena.

Python Files and Usage
1. vector_generation.py
This script is responsible for generating vectors based on user input. The user is prompted to input the x and y components of the vector as well as the starting coordinates. The script then generates a vector from the given data.
Usage: python vector_generation.py

2. vector_animation.py
This script animates a vector in 2D space, showing both its x and y components. The animation provides a dynamic visualization of how vectors behave over time, which is critical for understanding wave propagation and other EM phenomena.
Usage: python vector_animation.py

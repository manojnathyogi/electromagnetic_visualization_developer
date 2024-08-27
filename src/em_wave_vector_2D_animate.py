import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def get_vector_input():
    """Prompt the user to enter the x and y components of the vector and optionally the starting point."""
    x = float(input("Enter the x-component of the vector: "))
    y = float(input("Enter the y-component of the vector: "))
    start_x = float(input("Enter the starting x-coordinate (default is 0): ") or 0)
    start_y = float(input("Enter the starting y-coordinate (default is 0): ") or 0)
    return np.array([x, y]), np.array([start_x, start_y])

def animate_vector(vector, start_point):
    """Animate the vector along with its x and y components by translating them across the plane."""
    fig, ax = plt.subplots()
    # Calculate bounds for the plot
    steps = 10  # Define the number of steps you want to animate
    max_x = start_point[0] + vector[0] * (steps + 1)
    max_y = start_point[1] + vector[1] * (steps + 1)
    ax.set_xlim(min(0, start_point[0] - abs(vector[0])), max_x)
    ax.set_ylim(min(0, start_point[1] - abs(vector[1])), max_y)
    ax.grid(True)

    origin = start_point
    vec, = ax.plot([], [], 'o-', lw=2, color='blue', label='Vector')
    x_comp, = ax.plot([], [], 'r--', lw=2, color='red', label='X-Component')
    y_comp, = ax.plot([], [], 'g--', lw=2, color='green', label='Y-Component')
    ax.legend()

    def init():
        vec.set_data([], [])
        x_comp.set_data([], [])
        y_comp.set_data([], [])
        return vec, x_comp, y_comp

    def update(frame):
        # Calculate new origin
        new_origin = origin + vector * frame
        # Calculate ends of the vector and its components
        new_vector_end = new_origin + vector
        new_x_end = np.array([new_vector_end[0], new_origin[1]])  # x-component ends at the new vector's x with original y
        new_y_start = new_x_end  # y-component starts where x-component ends
        new_y_end = new_y_start + np.array([0, vector[1]])  # y-component is vertical

        # Update the data for vector and components
        vec.set_data([new_origin[0], new_vector_end[0]], [new_origin[1], new_vector_end[1]])
        x_comp.set_data([new_origin[0], new_x_end[0]], [new_origin[1], new_origin[1]])
        y_comp.set_data([new_y_start[0], new_y_start[0]], [new_y_start[1], new_y_end[1]])
        return vec, x_comp, y_comp

    # Create the animation
    ani = FuncAnimation(fig, update, frames=np.arange(0, steps + 1), init_func=init, blit=True, repeat=False)
    plt.show()

def main():
    vector, start_point = get_vector_input()
    animate_vector(vector, start_point)

if __name__ == "__main__":
    main()

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
    """Animate the vector along with its x and y components."""
    fig, ax = plt.subplots()
    ax.set_xlim(start_point[0] - 10, start_point[0] + 10 + vector[0])
    ax.set_ylim(start_point[1] - 10, start_point[1] + 10 + vector[1])
    ax.grid(True)

    origin = start_point
    vec, = ax.plot([], [], 'o-', lw=2, label='Vector')
    x_comp, = ax.plot([], [], 'r--', lw=2, label='X-Component')
    y_comp, = ax.plot([], [], 'g--', lw=2, label='Y-Component')
    ax.legend()

    def init():
        vec.set_data([], [])
        x_comp.set_data([], [])
        y_comp.set_data([], [])
        return vec, x_comp, y_comp

    def update(frame):
        end = origin + vector * frame
        vec.set_data([origin[0], end[0]], [origin[1], end[1]])
        x_comp.set_data([origin[0], end[0]], [origin[1], origin[1]])
        y_comp.set_data([end[0], end[0]], [origin[1], end[1]])
        return vec, x_comp, y_comp

    ani = FuncAnimation(fig, update, frames=np.linspace(0, 1, 30), init_func=init, blit=True, repeat=False)
    plt.show()

def main():
    vector, start_point = get_vector_input()
    animate_vector(vector, start_point)

if __name__ == "__main__":
    main()

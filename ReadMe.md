# Inverted Pendulum Cart-Pole Game with Kalman Filter Estimation

This is a Python program that implements an inverted pendulum cart-pole game using computer vision for tracking and a Kalman filter for state estimation. The program simulates an inverted pendulum system where a cart is tasked with balancing a pole on top of it. Computer vision is used to track the cart and pole positions, while a Kalman filter is used to estimate the state of the pendulum.

## Requirements

- Python
- OpenCV (`cv2`)
- NumPy
- Tknter
- Pygame

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/inverted-pendulum-kalman.git
   ```

2. Navigate to the project directory:

   ```bash
   cd inverted-pendulum-kalman
   ```

3. Install the required packages using `pip`:

   ```bash
   pip install opencv-python numpy pygame
   ```

## Usage

1. Run the main script to start the simulation:

   ```bash
   python main.py
   ```

2. The simulation will start, showing the inverted pendulum game with the cart and pole.

3. Computer vision will track the cart and pole positions on the screen.

4. A Kalman filter will be used to estimate the pendulum state (theta and theta_dot).

5. The estimated pendulum state can be used for control or analysis purposes.

## Configuration

- Modify the constants in the code to match your specific game setup and dynamics.
- Adjust the colors, threshold values, and other parameters for computer vision in the `findCenter` function.
- Tweak the Kalman filter parameters and initial conditions in the main script for optimal results.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
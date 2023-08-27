import numpy as np

class KalmanFilter:
    def __init__(self, initial_state, process_covariance, observation_covariance):
        self.state = initial_state  # Initial state [theta, theta_dot]
        self.process_covariance = process_covariance
        self.observation_covariance = observation_covariance
        self.P = np.eye(2)  # Initial state covariance
        self.F = np.array([[1, -0.005], [0, 1]])  # State transition matrix for inverted pendulum
        self.H = np.array([[1, 0]])  # Observation matrix

    def predict(self):
        self.state = np.dot(self.F, self.state)
        self.P = np.dot(np.dot(self.F, self.P), self.F.T) + self.process_covariance
        return self.state

    def update(self, z):
        y = z - np.dot(self.H, self.state)
        S = np.dot(np.dot(self.H, self.P), self.H.T) + self.observation_covariance
        K = np.dot(np.dot(self.P, self.H.T), np.linalg.inv(S))
        self.state = self.state + np.dot(K, y)
        self.P = np.dot((np.eye(2) - np.dot(K, self.H)), self.P)

        return self.state
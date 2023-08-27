import numpy as np


class PID_controller:
    def __init__(self):
        self.prev_action = 0
        self.prev_theta = 0
        self.integral = 0
        self.prev_x = 0

        self.kp = 25
        self.kd = 1
        self.ki = 0.1

    def reset(self):
        self.prev_action = 0
        self.prev_x = 0
        self.prev_theta = 0
        self.integral = 0 

    def get_action(self, state, image_state, random_controller=False):
        #terminal, Boolean
        #timestep, int
        #x, float, [-2.4, 2.4]
        #x_dot, float, [-inf, inf]
        #theta, float, [-pi/2, pi/2], radians
        #theta_dot, float, [-inf, inf]
        #reward, int, 0 or 1
        #image state is a (800, 400, 3) numpy image array; ignore it for assignment 2

        terminal, timestep, x, x_dot, theta, theta_dot, reward = state



        if random_controller:
            return np.random.uniform(-1, 1)
        else:
            #heurestic to limit I error for non converging
            if reward:
                self.integral += (theta + self.prev_theta  + (x + self.prev_x)/10) * timestep/2
            else:
                self.ki = 0

            action = self.kp * (theta + x/10) +  self.ki * (self.integral) + self.kd * (theta_dot + x_dot/10)


            self.prev_theta = theta
            self.prev_action = action
            self.prev_x = x

            if terminal:
                action = -self.prev_action

            '''
            if np.random.rand() > 0.99 :
                action = 10
                print('boom')
            '''

            return action

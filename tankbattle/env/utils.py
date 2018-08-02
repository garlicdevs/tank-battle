from scipy.misc import imresize
import time
import numpy as np


class Utils():
    WHITE = 0
    BLACK = 1
    GRAY = 2

    @staticmethod
    def get_current_time():
        return int(round(time.time()))

    @staticmethod
    def get_color(color):
        if color == Utils.WHITE:
            return (255, 255, 255)
        elif color == Utils.BLACK:
            return (0, 0, 0)
        elif color == Utils.GRAY:
            return (80, 80, 80)

    @staticmethod
    def process_state(state):
        grayscale = np.dot(state[:, :, :3], [0.299, 0.587, 0.114])
        resize = imresize(grayscale, (84, 84), interp='bilinear')
        return resize
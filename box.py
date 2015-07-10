import matplotlib.pyplot as plt
from math import sqrt
import os.path


# the environment of the box that the jitterbug runs, referring to box.png
class Box:
    def __init__(self, data):
        self.x, self.y = data
        self.circ_center = (997,542)
        self.circ_radius = 114
        self.height = 1000
        self.width = 1800
        self.filename = 'box.txt'
        self.raw_box = [['1'] * self.width for i in range(self.height)]

    # create the box environment, represented by nested lists for rows and columns
    def get_box(self):
        for row in range(self.height):
            print row
            for col in range(self.width):
                if row > min(self.y) and row < max(self.y):
                    if col > min(self.x) and col < max(self.x):
                        # use 0s to represent the available paths
                        self.raw_box[row][col] = '0'

                # use 1s to represent the walls and the round obstacle in the center
                d = sqrt((self.circ_center[0] - col) ** 2 + (self.circ_center[1] - row) ** 2)
                if d < self.circ_radius:
                    self.raw_box[row][col] = '1'
        return self.raw_box

    # save the created box env to a text file
    def write_box(self, box):
        box_file = open(self.filename, 'w')
        for l in box:
            box_file.write(''.join(l))
            box_file.write("\n")
        box_file.close()

    # read the saved text file to load box env
    def read_box(self):
        if os.path.isfile(self.filename):
            f = open(self.filename, 'r')
            data = f.readlines()
            box = [[str(int(i)) for i in j.rstrip()] for j in data]
            return box
        else:
            print 'The text file for box environment is not created yet.'
            return None

    # to plot the simulated box env. See file box_1.png
    def show_box(self, box):
        xx, yy = [], []
        for py, y in enumerate(box):
            for px, x in enumerate(y):
                if box[py][px] == '0':
                    xx.append(px)
                    yy.append(py)
        plt.scatter(xx, yy, color='r', s=0.01)
        plt.show()

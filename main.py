

from box import Box
from train import get_data



training_data = get_data()
box = Box(training_data)
box_env = box.read_box()  # box environment represented by nested lists

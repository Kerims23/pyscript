#data.py
# pip install numpy
#python3 -m http.server
# go to http://localhost:8000/numpy_pyscript.html
import numpy as np

def make_x_and_y(n):
    x = np.random.randn(n)
    y = np.random.randn(n)
    return x, y
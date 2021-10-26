import cv2
from pathlib import Path

path = Path('.').joinpath('images') # you shoud adjust this address upon your need
img = cv2.imread(path.joinpath('image_name')) # you should change 'image_name' upon your need
with open(path.joinpath('output.txt'), 'w') as f_out: # you should change 'output.txt' upon your need
    for i in img: 
        f_out.write(' '.join(['{},{},{}'.format(*j) for j in i]) + '\n') 
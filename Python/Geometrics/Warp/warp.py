import numpy as np
import asciitable
from skimage import io, transform, img_as_ubyte

# 画像読み込み
# org = io.imread("Ariel.jpeg", as_gray=True)
org = io.imread("Ariel.jpeg")

# 制御点の読み込み
source = asciitable.read("source.csv")
destination = asciitable.read("destination.csv")

# Format as numpy.arrays as required by scikit-image
source = np.column_stack((source["x"]+1, source["y"]+1))
destination = np.column_stack((destination["x"]+1, destination["y"]+1))

# Compute the transformation (order = 次数)
order = 3
t = transform.PolynomialTransform()
t.estimate(destination, source, order)
t.params
img_warped = img_as_ubyte(transform.warp(org, t))
merge = np.hstack((org, img_warped))
io.imshow(merge)
io.imsave("Ariel_warped.jpg", img_warped)
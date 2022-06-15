import cv2
import numpy as np
from stuf import red_blue_swap, fcp, hex_to_rgb

lines = open('catppuccin.txt').read().splitlines()
catppuccin = [hex_to_rgb(line) for line in lines]

# read the test.png image with opencv in rgb format
img = cv2.imread('test.png')
img = red_blue_swap(img)
# convert the image to rgb lists for every pixel
img_rgb = img.reshape((img.shape[0]*img.shape[1],3))
nimg_rgb = np.array([fcp(pixel, catppuccin)[0] for pixel in img_rgb])
print(nimg_rgb)
# undo the reshape
img_rgb = nimg_rgb.reshape(img.shape[0],img.shape[1],3)
img_rgb = red_blue_swap(img_rgb)
# save the image to wallpaper_new.png
cv2.imwrite('test_new.png', img_rgb)
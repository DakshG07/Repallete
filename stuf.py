import cv2
import math
# Fix BGR issues
def red_blue_swap(image):
    # 3-channel image (no transparency)
    if image.shape[2] == 3:
        b,g,r = cv2.split(image)
        image[:,:,2] = b
        image[:,:,0] = r
    # 4-channel image (with transparency)
    elif image.shape[2] == 4:
        b,g,r,a = cv2.split(image)
        image[:,:,0] = r
        image[:,:,2] = b
    return image 

def fcp(pixel, palletes): #Prototype for now
	ans = math.inf #Just a filler
	pal = [0,0,0] # Yet another filler
	for pallete in palletes:
		#Pythagorean Theorem (but it's 3D)
		result = math.sqrt(sum(list(map(lambda x,y: (x-y)**2, pixel, pallete))))
		if result < ans: ans = result; pal = pallete
	return pal, ans


def hex_to_rgb(hex):  
    return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))
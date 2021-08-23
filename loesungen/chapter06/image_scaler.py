import matplotlib.pyplot as plt
from skimage.io import imread, imshow
from skimage.transform import resize
from sys import argv, exit

if len(argv) < 3:
    print(f"Verwendung: python3 {argv[0]} BILDDATEI PIXEL")
    exit()

image = imread(argv[1], as_gray = True)
height, width = image.shape
if height > width:
    start = (height - width) // 2
    cropped = image[start:start + width, 0:width - 1]
elif width > height:
    start = (width - height) // 2
    cropped = image[0:height - 1, start:start + height]
new_size = int(argv[2])
resized = resize(cropped, (new_size, new_size))
plt.imshow(resized)
plt.show()

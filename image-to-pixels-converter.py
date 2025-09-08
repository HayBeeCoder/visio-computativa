from PIL import Image
import numpy as np
import pandas as pd

img = Image.open('black_white_car.jpg')
img_gray = img
print(img.mode)
if img.mode == 'RGB':
    img_gray = img.convert("L")

pixels = np.array(img_gray)
print(pixels)
df = pd.DataFrame(pixels)

df.to_excel("black_white_car_pixels.xlsx", index=False, header=False)
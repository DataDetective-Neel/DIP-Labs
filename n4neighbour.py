import numpy as np

img = np.zeros([10,10])

for i in range(4,7):
    for j in range(4,7):
        img[i,j] = 1


def is_n4(img,x1,y1,x2,y2):
    if img[x1,y1] == img[x2,y2]:
        if x2 in [x1-1,x1+1] and y2 == y1:
            return True
        if y2 in [y1-1,y1+1] and x2==x1:
            return True
        else:
            return False
    else: 
        return False

x1 = int(input("The x-coordinate of p is "))
y1 = int(input("The y-coordinate of p is "))
x2 = int(input("The x-coordinate of q is "))

y2 = int(input("The y-coordinate of q is "))

print(is_n4(img, x1,y1,x2,y2))
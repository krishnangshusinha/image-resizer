# IMAGE RESIZER

# Explanation:  So first we import the module cv2, that would be helpful in dealing with the modifying image 
#               attributes. So we first access our image that we need to resize by using the function imread()
#               Then we take input of the scale factor by which we need  to resize the dimensions. Then we acces
#               the height and the width of the original image by using the numpy shape[] array adn then multiply
#               it by the scale factor. And then we make a tuple of the new dimensions, and pass it to the resize()
#               and then using the imwrite() we apply the changes and create a new image file out of it.



import cv2      # this module is useful to access images and modify there attributes

image = cv2.imread("me.jpeg" , cv2.IMREAD_UNCHANGED)        # this command accesses/reads the image entered

# cv2.imshow("ME",image)          # this shows the image on the screen

# settig the scale by which we want to resize the image
scale = input("Enter the scale factor(0 to 1): ")
scale = float(scale)


# the numpy array contains height at shape[0] and width at shape[1] so we multiply it by a scale factor
height = int( image.shape[0] * scale)
width  = int( image.shape[1] * scale)


# a tuple of new dimensions is created
new_dim = (width,height)


# resizing the image ( that takes the new_dim as input inform of tuple )
output = cv2.resize(image, new_dim)

cv2.imwrite( 'cropped_image.jpeg' , output )    # this creates an image file to the set dimensions

cv2.waitKey(0)              # it acts as wait key and makes the image wait on screen before a key is entered  
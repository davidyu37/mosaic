from PIL import Image
import glob

new_width = 200
new_height = 200

image_list = []
for filename in glob.glob('kobe_bryant/*.jpg'): #assuming gif
    im=Image.open(filename)
    width, height = im.size   # Get dimensions

    left = (width - new_width)/2
    top = (height - new_height)/2
    right = (width + new_width)/2
    bottom = (height + new_height)/2

    # Crop the center of the image
    im = im.crop((left, top, right, bottom))
    im.save(filename)
    image_list.append(im)

print("Cropped Images: %s" % len(image_list))
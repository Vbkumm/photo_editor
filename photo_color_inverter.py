from PIL import Image

def is_background(item, bg):
    # Tweak the ranges if the result is still unsatisfying 
    return (item[0] in range(bg[0] - 20, bg[0] + 20)) or \
           (item[1] in range(bg[1] - 20, bg[1] + 20)) or \
           (item[2] in range(bg[2] - 20, bg[2] + 20))

img = Image.open("logo.jpg")
img = img.convert("RGB")
datas = img.getdata()

bg = [255, 255, 255] # Background RGB color
new_image_data = []
for item in datas:
    if is_background(item, bg) or item == (255, 255, 255):
        new_image_data.append((255, 0, 0))
    else:
        # change non-background and non-white to black
        new_image_data.append((0, 0, 0))
img.putdata(new_image_data)

img = img.convert("RGB")
datas = img.getdata()
new_image_data_two = []        
for item in datas:   
    # change all background to white and keep all white
    if item == (255, 0, 0):
        
        new_image_data_two.append((0, 0, 0))
    else:
        # change non-background and non-white to black
        new_image_data_two.append((255, 255, 255))
    
    

img.putdata(new_image_data_two)
img.save("logonew.png")
img.show()
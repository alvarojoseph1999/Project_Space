from PIL import Image, ImageDraw, ImageOps

def round_corners(image_path, radius):

    img = Image.open(image_path).convert("RGBA")
    

    mask = Image.new('L', img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle((0, 0, img.size[0], img.size[1]), radius=radius, fill=255)


    rounded_img = ImageOps.fit(img, mask.size)
    rounded_img.putalpha(mask)

    return rounded_img


image_path = 'img/AL.jpeg' 
radius = 600


rounded_image = round_corners(image_path, radius)

rounded_image.save('img/al.png')


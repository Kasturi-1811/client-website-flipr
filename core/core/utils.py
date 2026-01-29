from PIL import Image

def crop_image(image_path, target_width=450, target_height=350):
    """
    Crops the image to center and resizes it to 450x350
    """

    img = Image.open(image_path)
    width, height = img.size

    # Calculate center crop
    left = (width - target_width) / 2
    top = (height - target_height) / 2
    right = (width + target_width) / 2
    bottom = (height + target_height) / 2

    # If original image is smaller than target, resize first
    if width < target_width or height < target_height:
        img = img.resize((target_width, target_height))
    else:
        img = img.crop((left, top, right, bottom))

    img.save(image_path, quality=95)

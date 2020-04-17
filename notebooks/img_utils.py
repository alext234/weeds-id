from PIL import Image

# dimension of the final square image
IMAGE_SIZE=225    

def resize_image(img_original: Image.Image) -> Image.Image:
    '''
    Scale and crop the center to a predefined size  
    '''
    
    width, height = img_original.size
    assert width >= IMAGE_SIZE
    assert height >= IMAGE_SIZE
    
    # scale to a smaller size if need to,
    # before cropping the center
    scaled_size = IMAGE_SIZE * 1.5
    if min(width, height) > scaled_size:
        img_original.thumbnail((scaled_size,scaled_size))
        
    # crop center
    width, height = img_original.size
    left = (width - IMAGE_SIZE)/2
    top = (height - IMAGE_SIZE)/2
    right = (width + IMAGE_SIZE)/2
    bottom = (height + IMAGE_SIZE)/2

    img = img_original.crop((left, top, right, bottom))
    return img
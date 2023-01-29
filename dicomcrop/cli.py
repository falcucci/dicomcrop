def edges(image) -> str:
    """
    This function takes an image as input and returns
    a string describing the edges of the image.

    Parameters:
    image (str): a string representing the image

    Returns:
    str: a string describing the edges of the image
    """
    from lib import AutoCrop, open_
    binary_function  = open_(image)
    _bytes = binary_function(image)
    img_crop: AutoCrop = AutoCrop(_bytes)
    coordinates: tuple[int, int, int, int] = img_crop.new_image_coordinates()
    return "{}".format(coordinates)


def crop(image, output=''):
    """
    This function takes an image and an output
    directory as parameters and crops the image to a
    specified size.

    Parameters
    ----------
    image : str - The path of the image to be cropped.
    output : str, optional - The output directory to
    save the cropped image.
    """
    import uuid
    from PIL import Image
    from lib import AutoCrop, generate_token, OUT_JPG_FILES, open_
    binary_function  = open_(image)
    _bytes = binary_function(image)
    img_crop: AutoCrop = AutoCrop(_bytes)
    coordinates: tuple[int, int, int, int] = img_crop.new_image_coordinates()

    print("Cropping area " + str(coordinates))
    print(_bytes.size)

    cropped: Image.Image = _bytes.crop(coordinates) 
    encoded_id: str = generate_token({ "id": "{0}".format(uuid.uuid4())})
    cropped.save('{0}/__{1}.jpg'.format(
        output or OUT_JPG_FILES,
        encoded_id
    ))

def crop_images(directory, output=''):
    """
    This function crops images from a specified
    directory and outputs them to the desired output
    directory.

    Parameters:
    directory (str): the directory of the images to be
    cropped
    output (str): the desired output directory for the
    cropped images (default is '')
    """
    import os 
    import glob 
    from lib import create_output_dir, OUT_JPG_FILES
    create_output_dir(output or OUT_JPG_FILES)
    images: list[str] = glob.glob(os.path.join(directory, '*.DCM'))
    for image in images:
        crop(image)

if __name__ == '__main__':
    import fire
    fire.Fire({
        '--dir': crop_images,
        '--image': crop,
        '--edges': edges
    })

#!/usr/bin/env python
import os
import jwt
import uuid

from PIL import Image
from openpyxl.workbook import Workbook
from openpyxl.cell import Cell

TAB_NAME: str = "Foglio1"
OUT_JPG_FILES = './OUT_DICOM_JPG'
FILE_PATH: str = './SAMPLE/cartel.xlsx'

# how to generate a private key
# > openssl rand -base64 32
SECRET: str = os.environ.get('SECRET', str(uuid.uuid4()))

def get_data(path) -> Workbook:
    """
    This function reads the data from the given path and returns
    a Workbook object.

    Parameters:
    path (str): The path of the file

    Returns:
    Workbook: The workbook object with the data
    """
    from openpyxl import load_workbook
    return load_workbook(filename = path)

def map_values() -> dict[str, str]:
    """
    A dictionary within all useful informations built by
    { id: { type: <type> } }
    """
    book: Workbook = get_data(FILE_PATH)
    sheet: Workbook = book[TAB_NAME]
    column: tuple[Cell] = sheet['B']
    mapper: dict = {}
    for cell in column:
        mapper[cell.value] = { 'type': sheet['BS' + str(cell.row)].value }
    return mapper


def easter_egg(patient_id) -> str: 
    """
    This function takes in a patient_id and returns an easter egg string.

    Parameters:
    patient_id (int): The patient ID to use in generating the easter egg

    Returns:
    str: An easter egg string related to the patient ID
    """
    values: dict = map_values()
    return values.get(patient_id, {}).get('type', '')

def open_(image): 
    """
    This function opens an image file and returns the image object.

    Parameters:
    image (str): path to the image file

    Returns:
    image object
    """
    import pydicom
    import dicom2jpg
    ext: str = image.split('.')[-1]
    ext: str = ext.lower()

    def extract_dicom(image) -> tuple[
        Image.Image,
        pydicom.FileDataset
    ]:
        ds: pydicom.FileDataset = pydicom.dcmread(image)
        scaled_image = dicom2jpg.dicom2img(image)  
        return (Image.fromarray(scaled_image), ds)

    def extract_jpg(image)  -> tuple[Image.Image, dict]:
        return Image.open(image), {}

    return {
        "jpg": extract_jpg,
        "dcm": extract_dicom,
        "dicom": extract_dicom
    }[ext]

def generate_token(patient_id):
    """
    Generate a token for the patient id.
    """
    encoded_id: str = jwt.encode({
        "patient_id": patient_id
    }, SECRET, algorithm="HS256") 
    return encoded_id

def create_output_dir(output: str):
    """
    Creates an output directory to store generated files from the program.
    """
    os.makedirs(output, exist_ok=True)


class AutoCrop:
    def __init__(self, img):
        self.img = img

    def is_in_color_range(self, px, minimal_color:int) -> bool:
        """
        This function checks if a given pixel (px) has a color
        value greater than the minimal_color. It returns a boolean
        value indicating if the px color is in the range of the
        minimal_color or not.
        """
        return px[0] >= minimal_color and px[1] >= minimal_color and px[2] >= minimal_color

    def get_top_left(self) -> int:
        """
        This function returns the coordinates of the top left pixel of an image.

        Parameters:
            self (object): The instance of the class that calls the function.

        Returns:
            nearest (tuple): The coordinates of the top left pixel.
        """
        col = {}
        for x in range(self.img.size[1]):
            for y in range(self.img.size[0]):
                color = self.img.getpixel((y, x))
                col[x] = col.get(x, 0) + sum(color)
        else:
            key = max(col, key=col.get)
            nearest = self.find_nearest_key_by_value(col, key, 10000)
            return (nearest)

    def get_top_right(self) -> int:
        """
        This function gets the top right coordinates of the image.

        Params:
            self: reference to the current instance of the class

        Returns:
            nearest: top right coordinates of the image
        """
        col = {}
        for x in range(self.img.size[0]):
            for y in range(self.img.size[1]):
                color = self.img.getpixel((x, y))
                col[x] = col.get(x, 0) + sum(color)
        else:
            key = max(col, key=col.get)
            nearest: int = self.find_nearest_key_by_value(col, key, 10000)
            return (nearest)


    def get_lower_left(self) -> int:
        """
        Returns the coordinates of the lower left corner of the image.

        Parameters:
        self: The current instance of the class.

        Returns:
        (x, y): The coordinates of the lower left corner of the image.
        """
        col: dict[int, int] = {}
        for x in range(self.img.size[1]-1, 0, -1):
            for y in range(self.img.size[0]-1, 0, -1):
                color = self.img.getpixel((y, x))
                col[x+1] = col.get(x+1, 0) + sum(color)
        else:
            key = max(col, key=col.get)
            nearest: int = self.find_nearest_key_by_value(col, key, 10000)
            return (nearest)


    def get_lower_right(self) -> int:
        """
        This function gets the lower right coordinate of an image.
        It takes a single parameter, self, which is the object of
        the class it belongs to.
        It iterates through the x-axis and y-axis of the image,
        starting from the lower right corner and moving to the left and up.
        It adds up the RGB values of each pixel and adds them to a dictionary.
        It then finds the key with the maximum value from the dictionary
        and finds the nearest key based on a given threshold.
        It returns the nearest key, which is the lower right coordinate.
        """
        col = {}
        for x in range(self.img.size[0]-1, 0, -1):
            for y in range(self.img.size[1]-1, 0, -1):
                color: tuple[int, int, int] = self.img.getpixel((x, y))
                col[x+1] = col.get(x+1, 0) + sum(color)
        else:
            key = max(col, key=col.get)
            nearest: int = self.find_nearest_key_by_value(col, key, 10000)
            return (nearest)

    def find_nearest_key_by_value(self, mydict, high_key, minimal) -> int:
        """
        This function takes in a dictionary, a high key, and a minimal value,
        and returns the key in the dictionary closest to the minimal value.
        It creates a list of keys, up to the high key, and uses a lambda function
        to return the key closest to the minimal value.
        """
        l_r_pixel_keys: list[int] = []
        for key in mydict.keys():
            l_r_pixel_keys.append(key)
            if key == high_key:
                break

        l_r_pixel_keys: list[int] = l_r_pixel_keys[::-1]
        for r_key in l_r_pixel_keys:
            if mydict[r_key] <= minimal:
                return r_key
        return high_key

    def new_image_coordinates(self) -> tuple[int, int, int, int]:
        """This function returns a tuple of the coordinates for a new image.
        The coordinates returned are the top left, top right, lower right,
        and lower left points of the image. """
        top_right: int = self.get_top_right()
        top_left: int = self.get_top_left() 
        lower_right: int = self.get_lower_right()
        lower_left: int = self.get_lower_left()
        return (top_right, top_left, lower_right, lower_left)

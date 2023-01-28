# dicom-image-crop

dicom-image-crop is a project used for cropping digital images. It allows for users to select a rectangular area of the image and crop it out, allowing them to resize and adjust the image as needed.

The project has the following features:

- Selecting an area of an image to crop
- Adjusting the size of the cropped area
- Resizing the cropped image
- Saving the cropped image in various formats

Prepare bedside medical images for machine learning and image interpretation. dicom-image-cropper isolates the dynamic component of an image and strips away the rest.

## Installation

Requires python 3.7 or higher

Install with pip: ```pip3 install dicom-crop --upgrade```


#### crop

Automatically crop away static borders
```bash
dicom-image-cropper crop exmaple.DCM output.jpg
```

#### edges

Extracts the edges around an ultrasound

Returns the distance in pixels in the form:
left,right,top,bottom

```shell
$ dicom-image-crop edges example.DCM
$ > 100,500,10,700
```

#### summary

Command | Input | Output
------- | ----- | ------
crop | ![Input](./sample.jpg) | ![Out](./output.jpg)

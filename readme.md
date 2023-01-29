# dicomcrop

dicomcrop is a project used for cropping digital images. It allows for users to select a rectangular area of the image and crop it out, allowing them to resize and adjust the image as needed.

The project has the following features:

- Selecting an area of an image to crop
- Adjusting the size of the cropped area
- Resizing the cropped image
- Saving the cropped image in various formats

Prepare bedside medical images for machine learning and image interpretation. dicomcropper isolates the dynamic component of an image and strips away the rest.

## Installation

Requires python 3.7 or higher

Install with pip: ```pip3 install dicomcrop --upgrade```


#### crop

Automatically crop away static borders as much as you need
```bash
dicomcrop --dir <dir>
```

Automatically crop away static borders in a single file
```bash
dicomcrop --image <image>
```

#### edges

Extracts the edges around an medical image

Returns the distance in pixels in the form:
left,right,top,bottom

```shell
dicomcrop --edges example.DCM
> (293, 17, 969, 696)
```

#### summary

Command | Input | Output
------- | ----- | ------
crop | ![Input](./examples/sample.jpg) | ![Out](./examples/output.jpg)

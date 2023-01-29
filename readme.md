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

Generates cropped images encrypting private informations
```bash
dicomcrop --dir <dir> --encrypted
```

It's possible to disable the encrypted feature

```bash
dicomcrop --dir <dir> --encrypted=False
```

There is an easter egg to fetch informations from a spreadsheet file:

```bash
dicomcrop --dir <dir> --encrypted --egg=True
```

*all these extra commands can be applied following the `--image` command*

#### edges

Extracts the edges around a medical image

Returns the distance in pixels in the form:
left,right,top,bottom

```shell
dicomcrop --edges example.DCM
> (293, 17, 969, 696)
```

#### secrets

Returns a secret string from the library:

```shell
dicomcrop --secret
> e06dda30-5312-4623-936e-20b669c10495
```

#### tokens

Generate a hash string:

```shell
dicomcrop --token
> e06dda30-5312-4623-936e-20b669c10495
```

Generate a encrypted hash scring:

```shell
dicomcrop --token --encrypted
> eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwYXRpZW50X2lkIjoiZDQxMmY4MmUtY2U5Ni00MTg4LWEwZTktNWFmMTIzYTlkMDZlIn0._xhyeXCoaboKH8rqvzKCWa6Zg7ne9bjSHn58c91aLCc
```

#### summary

Command | Input | Output
------- | ----- | ------
crop | ![Input](./examples/sample.jpg) | ![Out](./examples/output.jpg)

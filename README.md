# DICOM Image Processing with Jupyter Notebook

This repository contains a Jupyter Notebook for processing DICOM images. The notebook demonstrates how to load, display, and manipulate DICOM images using various Python libraries.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Setup](#setup)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

DICOM (Digital Imaging and Communications in Medicine) is a standard for storing and transmitting medical images. This project provides a comprehensive guide on how to work with DICOM images in Python using a Jupyter Notebook. The notebook includes steps to load, display, and manipulate DICOM images.

## Features

- Load and display DICOM images
- Extract metadata from DICOM files
- Manipulate image pixel values (e.g., lighten the image)
- Generate inverse images

## Requirements

- Python 3.x
- Required Python packages:
  - imageio
  - matplotlib
  - numpy
  - pydicom
  - Pillow

## Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Thabhelo/medical_img.git
    cd medical_img
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Start Jupyter Notebook:**

    ```bash
    jupyter notebook
    ```

5. **Open the Jupyter Notebook:**

    In the Jupyter Notebook interface, open the `medical_img.ipynb` file.

## Usage

Follow the steps in the Jupyter Notebook to:

1. Load and display a DICOM image.
2. Extract metadata from the DICOM file.
3. Extract the image matrix containing pixel values.
4. Lighten the image by multiplying the image matrix by a scaler.
5. Generate an inverse image.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`.
3. Make your changes and commit them: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin feature-branch`.
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

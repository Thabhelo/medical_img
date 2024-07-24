# Load the required packages
import sys
import imageio
import matplotlib.pyplot as plt
import numpy as np
import pydicom
from PIL import Image

def main():
    # i. Load/read DICOM image using ImageIO
    # Read the DICOM file and store it in a variable
    dicom_file = 'assign.dcm'
    ds = pydicom.dcmread(dicom_file)
    im1 = ds.pixel_array

    # Render the image
    plt.imshow(im1, cmap='gray')
    plt.title('Image 1')
    plt.show()

    # ii. Extract information about the image such as the imaging modality, number of pixels, etc.
    print('Metadata: ', ds)
    print('Available metadata fields: ', ds.dir())
    print('Modality: ', ds.Modality)
    print('Shape of image array: ', im1.shape)

    # iii. Extract the image matrix containing pixel values
    # Print the image Numpy-array and direct the print output to a .txt file
    f1 = open("output1.txt", "w")
    np.set_printoptions(threshold=sys.maxsize)
    print(im1, file=f1)
    f1.close()

    # iv. Lighten image by multiplying the image matrix by a scaler
    scaler = 50
    im2 = im1 * scaler

    # Ensure the pixel values are within the valid range
    im2 = np.clip(im2, 0, 255)

    # Directing print output to a .txt file
    f2 = open("output2.txt", "w")
    np.set_printoptions(threshold=sys.maxsize)  # print the full NumPy array, without truncation
    print(im2, file=f2)
    f2.close()

    # Render the lightened image
    imL = Image.fromarray(im2.astype(np.uint8))
    plt.imshow(imL, cmap='gray')
    plt.title('Image 2')
    plt.show()

    # v. Inverse image
    inv = np.invert(im1)

    # Directing print output to a .txt file
    f3 = open("output3.txt", "w")
    np.set_printoptions(threshold=sys.maxsize)  # print the full NumPy array, without truncation
    print(inv, file=f3)
    f3.close()

    # Render the inverse image
    im3 = Image.fromarray(inv)
    plt.imshow(im3, cmap='gray')
    plt.title('Image 3')
    plt.show()


if __name__ == "__main__":
    main()
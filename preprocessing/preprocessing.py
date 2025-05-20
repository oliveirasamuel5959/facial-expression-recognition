import cv2
import matplotlib.pyplot as plt

def histplot(img, labels, nrows=2, ncols=2, hist_eq=False):
    # set initial parameters for figure
    fig, ax = plt.subplots(nrows=nrows, ncols=ncols, figsize=(9, 6), layout="constrained")

    # iterate through the images and class names
    for i, (image, filename) in enumerate(zip(img, labels)):
        x, y = i//ncols, i%ncols
        # break before index out of range error
        if x == nrows:
            break
        if equalized_pixel:
            image = cv2.equalizeHist(image)
        # calculate histogram
        hist = cv2.calcHist([image], [0], None, [256], [0, 256])
        # show images in grayscale
        ax[x, y].plot(hist)
        ax[x, y].set_xlabel("Pixel Itensity")
        ax[x, y].set_ylabel("Number of Pixels")
        ax[x, y].set_title(str(filename))

    # display grid of images
    fig.tight_layout()
    plt.show()
    


    
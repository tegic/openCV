import cv2


def image_loader():
    img = cv2.imread('1.jpg', cv2.IMREAD_GRAYSCALE)
    cv2.imshow('1', img)
    cv2.waitKey(0)
    cv2.imwrite('gray1.jpg', img)


def size_of_image():
    img = cv2.imread('1.jpg')
    print('Height: ' + str(img.shape[0]))
    print('Width: ' + str(img.shape[1]))
    print('Count of channels: ' + str(img.shape[2]))


if __name__ == '__main__':
    size_of_image()

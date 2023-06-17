import cv2, os


def image_loader(img_name:str, path:str):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    cv2.imshow('1', img)
    new_filename = img_name[:-4:] + 'gray.jpg'
    new_path = path[:-4:] + 'gray.jpg'
    # os.path.join(
    #         'instance\photos', img_name[:-4:] + 'gray.jpg'
    #     )
    cv2.imwrite(new_path, img)
    return new_filename


def size_of_image():
    img = cv2.imread('1.jpg')
    print('Height: ' + str(img.shape[0]))
    print('Width: ' + str(img.shape[1]))
    print('Count of channels: ' + str(img.shape[2]))


if __name__ == '__main__':
    image_loader()

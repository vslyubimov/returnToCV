import cv2
import numpy as np


def gaussian_blurring(image):

    img_blur_3 = cv2.GaussianBlur(image, (3, 3), 0)
    img_blur_7 = cv2.GaussianBlur(image, (7, 7), 0)
    img_blur_11 = cv2.GaussianBlur(image, (11, 11), 0)


def median_blurring(image):
    img_blur_3 = cv2.medianBlur(image, 3)
    img_blur_7 = cv2.medianBlur(image, 7)
    img_blur_11 = cv2.medianBlur(image, 11)



if __name__ == '__main__':
    #берем картинку с типом
    img = cv2.imread('pics/dogAndCat.jpg')
    #img_rgb = cv2.imread('dogAndCat.jpg', cv2.IMREAD_COLOR)

    img_blur = cv2.blur(img, (7, 7))
    img_blur_gaussian = cv2.GaussianBlur(img, (7, 7), 0)

    scale_percent = 30

    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)

    cv2.imshow('img_blur', np.hstack((cv2.resize(img, dim), cv2.resize(img_blur, dim), cv2.resize(img_blur_gaussian, dim))))
    cv2.waitKey(0)
    #cv2.imshow('dogAndCat', res_img)
    



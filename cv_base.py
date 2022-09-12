import cv2
import numpy as np

def resizing(img, new_width=None, new_height=None, interp=cv2.INTER_LINEAR):
    """Resize an image to specific size and with specific method. Returns resized image.

    Args:
        img (image): _description_
        new_width (int, optional): _description_. Defaults to None.
        new_height (int, optional): _description_. Defaults to None.
        interp (_type_, optional): _description_. Defaults to cv2.INTER_LINEAR.

    Returns:
        _type_: _description_
    """
    h, w = img.shape[:2]

    if new_width is None and new_height is None:
        return img

    # уточняем соотношение сторон (ratio) по высот, если ширина не дана, чтобы картинка не ломалась
    if new_width is None:
        ratio = new_height / h
        dimension = (int(w * ratio), new_height)

    else:
        ratio = new_width / w
        dimension = (new_width, int(h * ratio))

    res_img = cv2.resize(img, dimension, interpolation=interp)
    return res_img

def shifting(img):
    """Shifts image to right and down, opens in new window

    Args:
        img (image): image, from cv2.imread for example
    """
    h, w = img.shape[:2]
    translation_matrix = np.float32([[1, 0, 200], [0, 1, 300]]) # воу, матрица преобразований?
    dst = cv2.warpAffine(img, translation_matrix, (w, h))
    cv2.imshow('Изображение, сдвинутое вправо и вниз', dst)
    cv2.waitKey(0)


def cropping(img):
    crop_img = img[10:450, 300:750]
    return crop_img


def rotation(img):
    (h, w) = img.shape[:2]
    center = (int(w / 2), int(h / 2)) # точка вращения
    # точка вращения, угол вращения, коэф масштабирования (размер изображения)
    rotation_matrix = cv2.getRotationMatrix2D(center, -45, 0.5) 
    rotated = cv2.warpAffine(img, rotation_matrix, (w, h)) 
    return rotated


if __name__ == '__main__':
    # берем картинку с типом
    img = cv2.imread('dogAndCat.jpg', cv2.IMREAD_GRAYSCALE)
    img_rgb = cv2.imread('dogAndCat.jpg', cv2.IMREAD_COLOR)

    # изменение размера
    # res_img = resizing(img, 300, 300)
    # cv2.imshow('dogAndCat', res_img)
    # cv2.waitKey(0)
    
    # сдвиг
    # shifting(img)

    # срез
    # res_img = cropping(img)
    
    # поворот
    res_img = rotation(img)

    # записывает в файл картинку
    # cv2.imwrite('resizedDogAndCat.jpg', res_img)
     
    cv2.imshow('dogAndCat', res_img)
    cv2.waitKey(0)
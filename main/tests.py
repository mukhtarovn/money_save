#
# import cv2
# import numpy as np
#
# # Загрузить изображение
# image = cv2.imread("/Users/narimanmukhtarov/Downloads/dush.jpg")
#
# # Получить размеры изображения
# height, width, _ = image.shape
#
# # Создать полностью черное изображение (маску)
# mask = np.zeros((height, width), dtype=np.uint8)
#
# # Координаты прямоугольника для водяного знака
# # Укажите конкретные значения или задайте их динамически
# x_start = 10  # координата X левого верхнего угла
# y_start = 640  # координата Y левого верхнего угла
# x_end = 550   # координата X правого нижнего угла
# y_end = 720   # координата Y правого нижнего угла
#
# # Нарисовать белый прямоугольник на маске
# cv2.rectangle(mask, (x_start, y_start), (x_end, y_end), color=255, thickness=-1)
#
# # Сохранить маску
# cv2.imwrite("mask.jpg", mask)
#
# # Загрузка исходного изображения
# image = cv2.imread("/Users/narimanmukhtarov/Downloads/dush.jpg")
#
# # Загрузка маски
# mask = cv2.imread("mask.jpg")
#
# # Преобразование маски в 8-битное одноканальное изображение
# if len(mask.shape) == 3:  # Если маска цветная (3 канала)
#     mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
#
# # Убедимся, что значения маски — 0 или 255
# _, mask = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)
#
# # Проверка типа данных (должен быть uint8)
# mask = mask.astype(np.uint8)
#
# # Удаление водяного знака
# result = cv2.inpaint(image, mask, inpaintRadius=3, flags=cv2.INPAINT_TELEA)
#
# # Сохранение результата
# cv2.imwrite("image_without_watermark.jpg", result)

import cv2


def main():
    main_frame = cv2.imread("main_frame.png")

    one_image = cv2.imread("canvas023.png")
    print(one_image.shape)
    one_image_height, one_image_width = one_image.shape[:2]

    main_frame[140:140+one_image_height, 238:238+one_image_width] = one_image
    main_frame[50:100, 10:100] = (0, 0, 255)
    cv2.imshow("Image", main_frame)
    cv2.waitKey(0)
    cv2.imwrite("blorp.png", main_frame)


if __name__ == "__main__":
    main()

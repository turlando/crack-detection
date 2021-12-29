import sys
import cv2
import numpy as np
        
def main():
    source_path = sys.argv[1]
    destination_path = sys.argv[2]

    image = cv2.imread(source_path)

    greyscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    blur = cv2.blur(greyscale, (3, 3))

    log_transform = np.array(
        (np.log(blur + 1) / (np.log(1 + np.max(blur)))) * 255,
        dtype=np.uint8
    )

    bilateral_filter = cv2.bilateralFilter(log_transform, 5, 75, 75)

    edges = cv2.Canny(bilateral_filter, 100, 200)

    kernel = np.ones((5, 5), np.uint8)
    closing = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

    cv2.imwrite(destination_path, closing)


if __name__ == '__main__':
    main()

import matplotlib.pyplot as plt
import cv2

if __name__ == "__main__" :
    ucb = cv2.imread("stanford.png")
    ucb = cv2.resize(ucb, (50, 50))
    cv2.imwrite("stanford_resized.png", ucb)
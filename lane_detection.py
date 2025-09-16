import cv2

def get_detected_lane(image):
    (height, width) = (image.shape[1], image.shape[1])
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    canny_image = cv2.Canny(grayscale_image, 100, 120)
    return canny_image

video = cv2.VideoCapture("lane_detection_video.mp4")

while video.isOpened():
    is_grabbed, frame = video.read()

    # cos of the end of the video
    if not is_grabbed:
        break

    frame = get_detected_lane(frame)

    cv2.imshow("Lane Detection Video", frame)
    cv2.waitKey(30)
video.release()
cv2.destroyAllWindows()
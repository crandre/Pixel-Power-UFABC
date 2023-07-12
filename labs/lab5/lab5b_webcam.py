# import the opencv module
import cv2
import time

# Capturing video
capture = cv2.VideoCapture(0)

# Get current width and height of frame
width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)

# Define Video Frame Rate in fps
fps = capture.get(cv2.CAP_PROP_FPS)

# Create a VideoWriter object to save the output video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
timestamp = time.time()

out_1 = cv2.VideoWriter(f'./labs/lab5/5b_webcam_{timestamp}_tracking.mp4', fourcc, fps, (int(width), int(height)))
out_2 = cv2.VideoWriter(f'./labs/lab5/5b_webcam_{timestamp}.mp4', fourcc, fps, (int(width), int(height)))


while capture.isOpened():
    # to read frame by frame
    ret, img_1 = capture.read()
    if not ret:
        break  # Exit the loop if the frame wasn't read correctly

    ret, img_2 = capture.read()
    if not ret:
        break  # Exit the loop if the frame wasn't read correctly


    # find difference between two frames
    diff = cv2.absdiff(img_1, img_2)

    # to convert the frame to grayscale
    diff_gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    # apply some blur to smoothen the frame
    diff_blur = cv2.GaussianBlur(diff_gray, (5, 5), 0)

    # to get the binary image
    _, thresh_bin = cv2.threshold(diff_blur, 20, 255, cv2.THRESH_BINARY)

    # to find contours
    contours, hierarchy = cv2.findContours(thresh_bin, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # to draw the bounding box when the motion is detected
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        if cv2.contourArea(contour) > 300:
            cv2.rectangle(img_1, (x, y), (x+w, y+h), (0, 255, 0), 2)
    # cv2.drawContours(img_1, contours, -1, (0, 255, 0), 2)

    # display the output
    cv2.imshow("Detecting Motion...", img_1)
    cv2.imshow("Detecting Motion...2", img_2)

    out_1.write(img_1)
    out_2.write(img_2)

    if cv2.waitKey(1) == ord('q'):
        break

# Release the VideoWriter and VideoCapture objects
out_1.release()
out_2.release()
capture.release()

# Close all OpenCV windows
cv2.destroyAllWindows()

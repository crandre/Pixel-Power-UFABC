import cv2 as cv

# Capturing video
capture = cv.VideoCapture("./labs/lab1/saida7.avi")

# Get current width and height of frame
width = int(capture.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv.CAP_PROP_FRAME_HEIGHT))

# Define Video Frame Rate in fps
fps = 30.0

# Create a VideoWriter object to save the output video
fourcc = cv.VideoWriter_fourcc(*'XVID')
out_1 = cv.VideoWriter('./labs/lab5/Output_1_Lab5a_2.avi', fourcc, fps, (width, height))
out_2 = cv.VideoWriter('./labs/lab5/Output_2_Lab5a_2.avi', fourcc, fps, (width, height))


# Create the background subtractor
backSub = cv.createBackgroundSubtractorMOG2()

if not capture.isOpened():
    print('Unable to open video.')
    exit(0)

while True:
    ret, frame = capture.read()
    if not ret:
        break

    # Apply background subtraction to get the foreground mask
    fgMask = backSub.apply(frame)

    # Convert the foreground mask to a color image
    fgMaskColor = cv.cvtColor(fgMask, cv.COLOR_GRAY2BGR)

    # Write the resulting mask to the output video file
    out_1.write(fgMaskColor)

    # Apply bitwise AND operation to combine the original frame and the foreground mask
    fgFrame = cv.bitwise_and(frame, frame, mask=fgMask)

    # Write the resulting frame to the output video file
    out_2.write(fgFrame)

    # Display the original frame and the foreground mask
    cv.imshow('Original Frame', frame)
    cv.imshow('Foreground Mask', fgMask)

    if cv.waitKey(30) == ord('q'):
        break

# Release the video capture and writer objects
capture.release()
out_1.release()
out_2.release()
cont += 1



# Close all OpenCV windows
cv.destroyAllWindows()

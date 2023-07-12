# import the opencv module
import cv2
import time

videos = {
    "enzo":"./labs/lab1/saida2.avi",
    "giovanna":"./labs/lab1/saida7.avi",
}

video = "enzo"

# capturing video
cap = cv2.VideoCapture(videos[video])

# Get current width and height of frame
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define Video Frame Rate in fps
fps = 30.0

timestamp = time.time()
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

out = cv2.VideoWriter(f'./labs/lab5/5c_{video}_{timestamp}.mp4', fourcc, fps, (width, height))

#mog = cv2.createBackgroundSubtractorMOG2()
mog = cv2.createBackgroundSubtractorKNN()

while True:
    ret, frame = cap.read()
    if not ret:
        break  # Exit the loop if the frame wasn't read correctly

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    fgmask = mog.apply(gray)
    
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    fgmask = cv2.erode(fgmask, kernel, iterations=1)
    fgmask = cv2.dilate(fgmask, kernel, iterations=1)
    
    contours, hierarchy = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        # Ignore small contours
        if cv2.contourArea(contour) < 1000:
            continue
        
        # Draw bounding box around contour
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    cv2.imshow('Motion Detection', frame)
    out.write(frame)

    if cv2.waitKey(30) == ord('q'):
        out.release()
        break

out.release()
cap.release()
cv2.destroyAllWindows()

import cv2
import sys

(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')

print(major_ver, minor_ver, subminor_ver)

# Create tracker
# tracker = cv2.legacy.TrackerMOSSE_create()
tracker = cv2.legacy.TrackerCSRT_create()

# Read video 
video = cv2.VideoCapture("video-lab8.mp4")

# Exit if video not opened 
if not video.isOpened():     
     print("Could not open video")
     sys.exit() 

# Read first frame 
ok,frame = video.read() 
if not ok:
     print("Cannot read video file")
     sys.exit()

# Define a bounding box 
bbox = (276, 23, 86, 320) 
# Uncomment the line below to select a different bounding box
bbox = cv2.selectROI(frame, False)

frame_width = int(video.get(3))
frame_height = int(video.get(4))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('./8b.mp4', fourcc, 30.0, (frame_width, frame_height))
# Initialize tracker with first frame and bounding box 
ok = tracker.init(frame,bbox)

while True:
    # Read a new frame
    ok, frame = video.read()
    if not ok:
        break
 
    # Start timer
    timer = cv2.getTickCount()
 
    # Update tracker
    ok, bbox = tracker.update(frame)
 
    # Calculate Frames per second (FPS)
    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);
 
    # Draw bounding box
    if ok:
        # Tracking success
        p1 = (int(bbox[0]), int(bbox[1]))
        p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        cv2.rectangle(frame, p1, p2, (255,0,0), 2, 1)
    else :
        # Tracking failure
        cv2.putText(frame, "Tracking failure detected", (100,80), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)
 
    # Display tracker type on frame
    cv2.putText(frame, "GOTURN Tracker", (100,20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50),2);
 
    # Display FPS on frame
    cv2.putText(frame, "FPS : " + str(int(fps)), (100,50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);
 
    out.write(frame)
    # Display result
    cv2.imshow("Tracking", frame)
  
    # Exit if ESC pressed
    k = cv2.waitKey(1) & 0xff
    if k == 27:
         break

video.release()
out.release()

cv2.destroyAllWindows()

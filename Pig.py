import cv2
import os
import time

# Create the folder if it doesn't exist
if not os.path.exists("Pictures/pig"):
    os.makedirs("Pictures/pig")

# Open the video file
video = cv2.VideoCapture('VID.mp4')

# Initialize variables
success, image = video.read()
count = 0
frame_count = 0

# Loop through the video frames
while success:
    cv2.imshow('Video', image)
    if count % 4 == 0 and frame_count < 3:
        filename = f'Pictures/pig/frame_{count}.jpg'
        cv2.imwrite(filename, image)
        print(f'Frame {count} saved')
        frame_count += 1

    
    elif count % 4 != 0:
        if count % 30 == 0:
            filename = f'Pictures/pig/frame_{count}.jpg'
            cv2.imwrite(filename, image)
            print(f'Frame {count} saved')
    else:
        frame_count = 0

    # Read the next frame
    success, image = video.read()
    count += 1

    # Wait for a millisecond between frames
    time.sleep(1/30)
    if cv2.waitKey(1) == ord('q'):
        break
# Release the video file
video.release()
cv2.destroyAllWindows()

import cv2

# Open the video
cap = cv2.VideoCapture(r"C:\Users\Bhagya\Downloads\shreya2.mp4")

# Read the first frame
ret, prev_frame = cap.read()

# Check whether video was opened
if not ret:
    print("Error: Cannot read the video")
    cap.release()
    exit()

# Convert first frame to grayscale
prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

# Start reading video
while True:

    # Read the next frame
    ret, frame = cap.read()

    # Stop when video ends
    if not ret:
        break

    # Convert current frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Find difference between previous and current frame
    diff = cv2.absdiff(prev_gray, gray)

    # Detect motion
    motion = cv2.threshold(
        diff, 30, 255, cv2.THRESH_BINARY
    )[1]

    # Display video
    cv2.imshow("Original Video", frame)

    # Display motion
    cv2.imshow("Motion Detection", motion)

    # Current frame becomes previous frame
    prev_gray = gray

    # Press q to stop
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# Close everything
cap.release()
cv2.destroyAllWindows()
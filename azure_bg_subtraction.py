import cv2
import numpy as np

bg_frame = None

def capture_background(cap):
    global bg_frame
    print("Capturing background in 3 seconds. Please leave the frame.")
    for i in range(90):  # approx 3 seconds at 30fps
        ret, frame = cap.read()
        if ret:
            bg_frame = frame.copy()
    print("✅ Background captured.")

def main():
    global bg_frame
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Cannot access webcam")
        return

    print("Press 'b' to capture background (without you in frame).")
    print("Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        key = cv2.waitKey(1) & 0xFF

        if key == ord('b'):
            capture_background(cap)

        if bg_frame is not None:
            # Resize both to same size
            frame_resized = cv2.resize(frame, (640, 480))
            bg_resized = cv2.resize(bg_frame, (640, 480))

            # Compute absolute difference
            diff = cv2.absdiff(frame_resized, bg_resized)
            gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
            _, mask = cv2.threshold(gray, 35, 255, cv2.THRESH_BINARY)

            # Clean mask
            kernel = np.ones((5, 5), np.uint8)
            mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
            mask = cv2.dilate(mask, kernel, iterations=1)

            # Extract person
            person = cv2.bitwise_and(frame_resized, frame_resized, mask=mask)

            # Show combined result
            combined = frame_resized.copy()
            combined[mask == 0] = bg_resized[mask == 0]

            cv2.imshow("Mask", mask)
            cv2.imshow("Person Only", person)
            cv2.imshow("Combined", combined)
        else:
            cv2.imshow("Webcam", frame)

        if key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

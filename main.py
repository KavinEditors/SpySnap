import cv2
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
from datetime import datetime
import time

# Folder to monitor
WATCH_PATH = os.path.expanduser("~/Downloads")

# Folder to save webcam photos
SAVE_PATH = os.path.expanduser("~/Music/SecurityPhotos")

# Ensure save directory exists
os.makedirs(SAVE_PATH, exist_ok=True)


class DownloadEvent(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            try:
                capture_photo()
            except Exception as e:
                # Log errors silently
                with open(os.path.join(SAVE_PATH, "error.log"), "a") as f:
                    f.write(f"{datetime.now()}: {str(e)}\n")


def capture_photo():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise RuntimeError("Webcam not accessible")
    ret, frame = cap.read()
    if ret:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(SAVE_PATH, f"{timestamp}.jpg")
        cv2.imwrite(filename, frame)
    cap.release()
    cv2.destroyAllWindows()


def main():
    event_handler = DownloadEvent()
    observer = Observer()
    observer.schedule(event_handler, WATCH_PATH, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()


if __name__ == "__main__":
    main()

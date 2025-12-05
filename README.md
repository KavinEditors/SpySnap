Automatic Webcam Capture on File Download – Windows

Overview
--------
This program continuously monitors the Downloads folder on a Windows PC and automatically captures a webcam photo whenever any new file is downloaded or created. Captured photos are saved in:
    C:\Users\<YourUsername>\Music\SecurityPhotos

The script runs silently in the background and can be configured to start automatically on system boot.

Features
--------
• Detects ANY file downloaded to the Downloads folder (no restriction by file type)
• Takes a webcam photo instantly upon detection
• Saves all images with timestamps
• Runs silently using pythonw (no Windows console)
• Auto-starts on system boot
• Error logging for webcam issues
• Folder for photos created automatically if missing

Requirements
-----------
• Windows OS
• Python 3.x installed
• Required Python modules:
    pip install opencv-python watchdog

Installation & Setup
--------------------
1. Place main.py somewhere permanent, for example:
    C:\Users\<YourUsername>\Documents\main.py

2. Create a batch file to run the script silently:
   File name: run_main.bat
   Contents:
       @echo off
       pythonw "C:\Users\<YourUsername>\Documents\main.py"
       exit

3. Add run_main.bat to Windows startup:
   • Press Win + R
   • Type: shell:startup
   • Press Enter
   • Copy run_main.bat into this folder

4. Restart your PC to confirm the script auto‑launches.

Folder Structure Created Automatically
--------------------------------------
• Downloads folder is monitored automatically.
• SecurityPhotos folder is created automatically in Music.
• Error logs (if any) are saved in SecurityPhotos/error.log

Saved Files
-----------
Images are stored as:
    YYYYMMDD_HHMMSS.jpg

Troubleshooting
---------------
• If the webcam is unavailable or another program is using it, an error entry is written to:
    error.log inside the SecurityPhotos folder
• To stop the program, end the pythonw process in Task Manager.

Small Description
-----------------
This program monitors the Downloads folder on Windows and automatically takes a webcam photo whenever a new file is detected. Photos are saved in the Music\SecurityPhotos folder with timestamps, and the script runs silently on system startup.

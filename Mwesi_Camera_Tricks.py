#!/usr/bin/env python3
#


import sys
import cv2
import numpy as np

window_title = "Mwesi Camera"

def show_camera():

    # Assigning Camera Address
    camera_id = "/dev/video0"

    # Using V4L2 codec
    video_capture = cv2.VideoCapture(camera_id, cv2.CAP_V4L2)


    # Initial positions and directions
    text_x, text_y = 100, 100
    x_text_direction, y_text_direction = 1, 1
    
    # Define the new dimensions (width, height) for resizing
    new_width = 140
    new_height = 140
    
    logo = cv2.imread('DT_LOGO.jpg')
    logo = cv2.resize(logo, (new_width, new_height))
    logo_height, logo_width = logo.shape[:2]
    logo_x, logo_y = 500, 100
    x_logo_direction, y_logo_direction = -1, 1
    
    if video_capture.isOpened():
        try:
            window_handle = cv2.namedWindow(
                window_title, cv2.WINDOW_AUTOSIZE )
            # Window
            while True:
                ret_val, frame = video_capture.read()
                # Check to see if the user closed the window
                # Because GTK+ , WND_PROP_VISIBLE  (This is the Default for Jetson) does not work here, an alternative method is used.
                # GTK - Substitute=ing in WND_PROP_AUTOSIZE for detection closed window (invoked by user)
                if cv2.getWindowProperty(window_title, cv2.WND_PROP_AUTOSIZE) >= 0:
                    # Draw the text at the current position
                    cv2.putText(frame, "Mwesi is cool", (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    
                    # Draw the logo at the current position
                    frame[logo_y:logo_y+logo_height, logo_x:logo_x+logo_width] = logo
                    
                    cv2.imshow(window_title, frame)
                    
                    # Update the text position for the next frame
                    text_x += x_text_direction
                    text_y += y_text_direction
                    
                    # Update the logo position for the next frame
                    logo_x += x_logo_direction
                    logo_y += y_logo_direction
                    
                    # Check if the text has reached the screen edges, reverse direction if so
                    if text_x <= 0 or text_x >= frame.shape[1]:
                        x_text_direction *= -1
                    if text_y <= 0 or text_y >= frame.shape[0]:
                        y_text_direction *= -1
                        
                    # Check if the logo has reached the screen edges, reverse direction if so
                    if logo_x <= 0 or logo_x + logo_width >= frame.shape[1]:
                        x_logo_direction *= -1
                    if logo_y <= 0 or logo_y + logo_height >= frame.shape[0]:
                        y_logo_direction *= -1
                    
                else:
                    break
                keyCode = cv2.waitKey(10) & 0xFF
                # Stop the program on the ESC key or 'q'
                if keyCode == 27 or keyCode == ord('q'):
                    break

        finally:
            video_capture.release()
            cv2.destroyAllWindows()
    else:
        print("Unable to open camera")


if __name__ == "__main__":
    show_camera()





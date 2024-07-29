import cv2
import tkinter as tk
from PIL import Image, ImageTk



def detect_faces(frame):
    # Converting frame ----> grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detecting faces
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # Drawing Rectangles around faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    return frame



def update_frame():
    ret, frame = cap.read()
    if ret:
        frame = cv2.flip(frame, 1)
        frame = detect_faces(frame)
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        label.imgtk = imgtk
        label.configure(image=imgtk)
    label.after(10, update_frame)



# Initialize Tkinter window
root = tk.Tk()
root.title("Face Detection")


# Create a label and pack it into the window
label = tk.Label(root)
label.pack()


# Initialize video capture
cap = cv2.VideoCapture(0)


update_frame()

root.mainloop()


# Release the video capture object
cap.release()
from tkinter import *
import pyscreenrec
from PIL import Image, ImageTk

# Initialize the ScreenRecorder object
rec = pyscreenrec.ScreenRecorder()

# Tkinter setup
root = Tk()
root.title("SCREEN RECORDER")
root.geometry("500x700+100+50")
root.resizable(False, False)
root.configure(bg="#fff")

# Functions
def start_button():
    file = filename.get()
    rec.start_recording(str(file + ".mp4"), 5)

def pause_button():
    rec.pause_recording()

def play_button():
    rec.resume_recording()

def stop_button():
    rec.stop_recording()

# Icon
image_icon = PhotoImage(file="recoder.png")
root.iconphoto(False, image_icon)

# Background
image = Image.open("back.png")
image = image.resize((495, 695), Image.Resampling.LANCZOS)
background = ImageTk.PhotoImage(image)
Label(root, image=background, bg="white").place(x=0, y=0)

# Heading
lbl = Label(root, text="SCREEN RECORDER", font="arial 18 bold", bg="#0B162B", fg="white")
lbl.pack(pady=20)

# Center Image
image_center = Image.open("app.png")
image_center = image_center.resize((200, 200), Image.Resampling.LANCZOS)
ImageCenter = ImageTk.PhotoImage(image_center)
Label(root, image=ImageCenter, bg="white").place(x=150, y=120)

# Entry
filename = StringVar()
entry = Entry(root, textvariable=filename, width=18, font="arial 15")
entry.place(x=100, y=350)
filename.set("recording1")

# Buttons
start = Button(root, text="Start", font="arial 22 bold", bd=0, fg="white", bg="blue", command=start_button)
start.place(x=195, y=400)

img1 = Image.open("pause.png")
img1 = img1.resize((50, 50), Image.Resampling.LANCZOS)
image1 = ImageTk.PhotoImage(img1)
Button(root, image=image1, background="#C43008", command=pause_button).place(x=120, y=500)

img2 = Image.open("play.png")
img2 = img2.resize((50, 50), Image.Resampling.LANCZOS)
image2 = ImageTk.PhotoImage(img2)
Button(root, image=image2, background="#C21C18", command=play_button).place(x=220, y=500)

img3 = Image.open("stop.png")
img3 = img3.resize((50, 50), Image.Resampling.LANCZOS)
image3 = ImageTk.PhotoImage(img3)
Button(root, image=image3, background="#A8BA20", command=stop_button).place(x=320, y=500)

# Run the application
root.mainloop()

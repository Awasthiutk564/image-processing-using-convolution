import tkinter as tk
from tkinter import filedialog, messagebox
import cv2
import numpy as np
from PIL import Image, ImageTk

# ---------------------------
# Global Variables
# ---------------------------
img_original = None
img_display = None

# ---------------------------
# Function to Show Image
# ---------------------------
def show_image(img):
    global img_display

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_pil = Image.fromarray(img_rgb)
    img_pil = img_pil.resize((500, 350))

    img_tk = ImageTk.PhotoImage(img_pil)
    img_display = img_tk
    panel.config(image=img_tk)

# ---------------------------
# Upload Image
# ---------------------------
def upload_image():
    global img_original

    path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.jpg *.png *.jpeg")]
    )

    if path:
        img_original = cv2.imread(path)
        show_image(img_original)

# ---------------------------
# Blur Function
# ---------------------------
def blur_image():
    global img_original
    if img_original is None:
        messagebox.showerror("Error", "Upload image first")
        return

    kernel = np.ones((3,3), np.float32) / 9
    result = cv2.filter2D(img_original, -1, kernel)
    show_image(result)

# ---------------------------
# Sharpen Function
# ---------------------------
def sharpen_image():
    global img_original
    if img_original is None:
        messagebox.showerror("Error", "Upload image first")
        return

    kernel = np.array([[0,-1,0],
                       [-1,5,-1],
                       [0,-1,0]])

    result = cv2.filter2D(img_original, -1, kernel)
    show_image(result)

# ---------------------------
# Edge Detection
# ---------------------------
def edge_image():
    global img_original
    if img_original is None:
        messagebox.showerror("Error", "Upload image first")
        return

    kernel = np.array([[-1,-1,-1],
                       [-1,8,-1],
                       [-1,-1,-1]])

    result = cv2.filter2D(img_original, -1, kernel)
    show_image(result)

# ---------------------------
# Reset Image
# ---------------------------
def reset_image():
    global img_original
    if img_original is not None:
        show_image(img_original)

# ---------------------------
# GUI Window
# ---------------------------
root = tk.Tk()
root.title("DSP Image Processing using Convolution")
root.geometry("700x550")
root.config(bg="black")

title = tk.Label(root, text="Image Processing using DSP Convolution",
                 font=("Arial", 18, "bold"),
                 bg="black", fg="cyan")
title.pack(pady=10)

panel = tk.Label(root, bg="gray")
panel.pack(pady=10)

# Buttons Frame
frame = tk.Frame(root, bg="black")
frame.pack(pady=10)

btn1 = tk.Button(frame, text="Upload Image", command=upload_image, width=15, bg="cyan")
btn1.grid(row=0, column=0, padx=5, pady=5)

btn2 = tk.Button(frame, text="Blur", command=blur_image, width=15, bg="lightgreen")
btn2.grid(row=0, column=1, padx=5, pady=5)

btn3 = tk.Button(frame, text="Sharpen", command=sharpen_image, width=15, bg="orange")
btn3.grid(row=0, column=2, padx=5, pady=5)

btn4 = tk.Button(frame, text="Edge Detect", command=edge_image, width=15, bg="pink")
btn4.grid(row=1, column=0, padx=5, pady=5)

btn5 = tk.Button(frame, text="Reset", command=reset_image, width=15, bg="yellow")
btn5.grid(row=1, column=1, padx=5, pady=5)

btn6 = tk.Button(frame, text="Exit", command=root.quit, width=15, bg="red")
btn6.grid(row=1, column=2, padx=5, pady=5)

root.mainloop()
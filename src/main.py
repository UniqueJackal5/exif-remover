import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import piexif

def remove_exif(filepath):
    try:
        img = Image.open(filepath)
        data = list(img.getdata())
        new_img = Image.new(img.mode, img.size)
        new_img.putdata(data)
        new_img.save(filepath)  # overwrite original
        return True
    except Exception as e:
        print(f"Error removing EXIF from {filepath}: {e}")
        return False

def process_images(filepaths):
    count = 0
    for path in filepaths:
        if path.lower().endswith((".jpg", ".jpeg")):
            if remove_exif(path):
                count += 1
    messagebox.showinfo("Done", f"EXIF data removed from {count} image(s).")

def select_images():
    filepaths = filedialog.askopenfilenames(
        title="Select Images",
        filetypes=[("JPEG files", "*.jpg *.jpeg")],
    )
    if filepaths:
        process_images(filepaths)

def select_folder():
    folder_path = filedialog.askdirectory(title="Select Folder")
    if folder_path:
        filepaths = [os.path.join(folder_path, f)
                     for f in os.listdir(folder_path)
                     if f.lower().endswith((".jpg", ".jpeg"))]
        process_images(filepaths)

# GUI Setup
root = tk.Tk()
root.title("Image EXIF Remover")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

label = tk.Label(frame, text="Select images or a folder to remove EXIF data")
label.pack(pady=10)

btn1 = tk.Button(frame, text="Select Images", command=select_images, width=20)
btn1.pack(pady=5)

btn2 = tk.Button(frame, text="Select Folder", command=select_folder, width=20)
btn2.pack(pady=5)

root.mainloop()

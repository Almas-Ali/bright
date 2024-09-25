#!usr/bin/python3.12
# -*- coding: utf-8 -*-

'''
A Brightness control GUI application for Linux systems.

Easy to use it. No training needed!! ;)
'''

import subprocess
import tkinter as tk
from tkinter import messagebox, ttk


# Function to set brightness using xrandr
def set_brightness(persent: int) -> None:
    SET_BRIGHTNESS = int(persent) / 100
    cmd = f"xrandr --output LVDS-1 --brightness {SET_BRIGHTNESS}"
    subprocess.run(cmd, shell=True)


# Function to get the current brightness using xrandr
def get_brightness() -> int:
    GET_BRIGHTNESS = "xrandr --verbose | awk '/Brightness/ { print $2; exit }'"

    process = subprocess.Popen(
        [GET_BRIGHTNESS], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    stdout, stderr = process.communicate()

    CURRENT_BRIGHTNESS = int(float(str(stdout, "utf-8")) * 100)
    return CURRENT_BRIGHTNESS


# Function that gets called when the slider is moved
def update_brightness(value):
    brightness_value = int(float(value))

    # Check for minimum brightness threshold
    if brightness_value < 10:
        messagebox.showwarning("Warning", "Brightness cannot be set lower than 10%!")
        brightness_slider.set(10)  # Reset slider to minimum value
        set_brightness(10)  # Set brightness to 10%
    else:
        set_brightness(brightness_value)

    # Update the current brightness label
    current_brightness_label.config(text=f"Current Brightness: {brightness_value}%")


# Functions for menu items
def show_version():
    messagebox.showinfo("Version", "Version: 1.1")


def show_author():
    messagebox.showinfo("Author", "Author: MD. ALMAS ALI")


def show_help():
    messagebox.showinfo(
        "Help",
        "Use the slider to adjust the screen brightness.\n\nMinimum brightness is 10%.",
    )


def exit_app():
    root.quit()


# Create the main application window
root = tk.Tk()
root.title("Brightness Control")
root.geometry("400x300")  # Increased height for the current brightness label
root.resizable(False, False)

# Create a menu bar
menu_bar = tk.Menu(root)

# Create a File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Version", command=show_version)
file_menu.add_command(label="Author", command=show_author)
file_menu.add_command(label="Help", command=show_help)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)
menu_bar.add_cascade(label="File", menu=file_menu)

# Configure the menu bar
root.config(menu=menu_bar)

# Set a modern theme for the app using ttk styles
style = ttk.Style(root)
style.theme_use("clam")  # You can try 'clam', 'alt', 'default', or 'classic'
style.configure("TFrame", background="#f0f0f0")  # Frame background color
style.configure("TLabel", font=("Helvetica", 12), background="#f0f0f0")  # Label styles
style.configure("TScale", background="#f0f0f0")  # Scale (Slider) background
style.configure("TButton", font=("Helvetica", 10))

# Main frame
frame = ttk.Frame(root, padding=(20, 20))
frame.pack(expand=True, fill=tk.BOTH)

# Label for Brightness
brightness_label = ttk.Label(frame, text="Adjust Brightness", anchor="center")
brightness_label.pack(pady=10)

# Slider (Scale) widget
brightness_slider = ttk.Scale(
    frame, from_=0, to=100, orient="horizontal", length=300, command=update_brightness
)
brightness_slider.pack(pady=20)

# Label to display the current brightness percentage
current_brightness_label = ttk.Label(
    frame, text="Current Brightness: 50%", anchor="center"
)
current_brightness_label.pack(pady=10)

# Get the current system brightness and set the slider accordingly
current_brightness = get_brightness()
brightness_slider.set(current_brightness)
current_brightness_label.config(
    text=f"Current Brightness: {current_brightness}%"
)  # Update label on startup

# Start the application
root.mainloop()

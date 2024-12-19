# captain-nemo
# 2024 Dec 19
# Just a little widget to show off the latest XKCD :)

import json
import tkinter
from tkinter import PhotoImage, Frame
import requests as req

comic_details = []

def get_comic_details():
    """Get the json from xkcd.com"""
    global comic_details
    res = req.get("https://xkcd.com/info.0.json")
    details = json.loads(res.text)
    # Put just the parts we need in a list
    comic_details = [details.get("alt"),
                        details.get("img"),
                        details.get("safe_title")]
    # Get the actual image and store it locally
    res = req.get(comic_details[1]).content
    with open("comic_o_the_day.png", 'wb') as handler:
        handler.write(res)

def refresh(image_label, alt_label):
    """Refresh the displayed image and alt text"""
    get_comic_details()
    new_image = PhotoImage(file="comic_o_the_day.png")
    image_label.configure(image=new_image)
    image_label.image = new_image

    alt_label.configure(text=comic_details[0])

def main():
    """Our main function"""
    # Get the json and comic image
    get_comic_details()
    # Create a tkinter window and set its properties
    parent = tkinter.Tk()
    parent.title("XKCD")
    parent.configure(bg='lightblue')
    # A frame to hold the comic with a little bit of padding
    frame = Frame(parent)
    frame.pack(pady=(20,10), padx=20)
    # Load the image into the frame
    image = PhotoImage(file="comic_o_the_day.png")
    image_label = tkinter.Label(frame, image=image)
    image_label.pack()
    # Update idle tasks so that I can access winfo_width
    parent.update_idletasks()
    # Put the alt text in a label beneath the comic
    alt_label = tkinter.Label(parent, text=comic_details[0], bg='lightblue', font=("Lucida Sans", 11), wraplength=parent.winfo_width())
    alt_label.pack(pady=(0,10), padx=(10,10))
    # Create the refresh button
    button = tkinter.Button(parent, text="Refresh", command=lambda: refresh(image_label, alt_label))
    button.pack(pady=(0,10))
    # Start the tkinter mainloop
    parent.mainloop()

if __name__ == "__main__":
    main()

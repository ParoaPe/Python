# Importing necessary packages
import os
import tkinter as tk
from tkinter import * # Import all Tkinter libraries from the module
from unittest import expectedFailure 
from pytube import YouTube # From the installed Pytube module, import the youtube library
from tkinter import messagebox, filedialog 

# Fonction who manage Tkinter 
def Widgets():
    head_label = Label(UI, text="Youtube Downloader", padx=15, pady=15, font="SegoeUI 14", fg="black", bg="gainsboro")
    head_label.grid(row=1, column=1, pady=10, padx=5, columnspan=3)
    link_label = Label(UI, text="YouTube link :", bg="gainsboro", pady=5, padx=5)
    link_label.grid(row=2, column=0, pady=5, padx=5)
    UI.linkText = Entry(UI,width=35, textvariable=video_link, font="Arial 14")
    UI.linkText.grid(row=2, column=1, pady=5, padx=5, columnspan=2)
    destination_label = Label(UI,text="Destination :", bg="gainsboro", pady=5, padx=9)
    destination_label.grid(row=3, column=0, pady=5, padx=5)
    UI.destinationText = Entry(UI, width=27, textvariable=download_Path, font="Arial 14")
    UI.destinationText.grid(row=3, column=1, pady=5, padx=5)
    browse_B = Button(UI, text="Browse", command=Browse, width=10, bg="bisque", relief=GROOVE)
    browse_B.grid(row=3, column=2, pady=1, padx=1)
    Download_B = Button(UI, text="Download Video", command=Download, width=20, bg="coral", pady=10, padx=15, relief=GROOVE, font="Georgia, 13")
    Download_B.grid(row=5, column=1, pady=20, padx=20)
    Download_B_MP3 = Button(UI, text="Download Audio", command=Download_MP3, width=20, bg="coral", pady=10, padx=15, relief=GROOVE, font="Georgia, 13")
    Download_B_MP3.grid(row=6, column=1, pady=20, padx=20)

# Browse button
def Browse():
    download_Directory = filedialog.askdirectory(initialdir="Your directory path", title="Save Video")
    download_Path.set(download_Directory)

# Download Button
def Download():
    # Getting user-input Youtube Link
    Youtube_link = video_link.get()
    # select the optimal location for saving file's
    download_Folder = download_Path.get()
    # Creating object of YouTube()
    getVideo = YouTube(Youtube_link)
    # Getting all the available streams of the youtube video and selecting the first from the
    videoStream = getVideo.streams.get_highest_resolution()
    # Downloading the video
    videoStream.download(download_Folder)
    # Displaying the message
    messagebox.showinfo("SUCCESSFULLY MP4", "DOWNLOADED\n")

def Download_MP3():
    # Getting user-input Youtube Link
    Youtube_link = video_link.get()
    # select the optimal location for saving file's
    download_Folder = download_Path.get()
    # Creating object of YouTube()
    getVideo = YouTube(Youtube_link)
    # Getting all the available streams of the youtube audio
    videoStream = getVideo.streams.filter(only_audio=True).first().download(download_Folder)
    base, ext = os.path.splitext(videoStream)
    new_file = base + '.mp3'
    os.rename(videoStream, new_file)
    # Downloading the video
    # videoStream.download(download_Folder)

    # Displaying the message
    messagebox.showinfo("SUCCESSFULLY MP3", "DOWNLOADED\n")

# Creating object of tk class
UI = tk.Tk()


# Size of the tkinter window
UI.geometry("520x380")
# Disabling the resizing property
UI.resizable(False, False)
# Setting the title
UI.title("YouTubeDL by ParoaPe")
# Setting the background color
UI.config(background="gainsboro")
 
# Creating the tkinter Variables
video_link = StringVar()
download_Path = StringVar()
var = IntVar()
 
# Calling the Widgets() function
Widgets()
 
# Defining infinite loop to run application
UI.mainloop()



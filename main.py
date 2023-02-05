import tkinter
import customtkinter
from pytube import YouTube
import os

def startDownloadVideo():
    finishedLabel.configure(text="", text_color="white") 
    progressBar.set(0)
    pPercent.configure(text= "0%")
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()
        title.configure(text=ytObject.title, text_color="white")
        finishedLabel.configure(text="")
        video.download()
        finishedLabel.configure(text="Youtube download complete", text_color="green") 
    except:
        finishedLabel.configure(text="Youtube link is invalid", text_color="red")

def startDownloadAudio():
    finishedLabel.configure(text="", text_color="white")
    progressBar.set(0)
    pPercent.configure(text= "0%")
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        audio = ytObject.streams.filter(only_audio=True).first()
        characters = "."
        for x in range(len(characters)):
            preTitle = ytObject.title.replace(characters[x],"")
        title.configure(text=preTitle, text_color="white")
        finishedLabel.configure(text="")
        audio.download()
        #rename file from mp4 to mp3
        my_file = preTitle + ".mp4"
        print(my_file)
        base = os.path.splitext(my_file)[0]
        print(base)
        os.rename(my_file, base + ".mp3")
        finishedLabel.configure(text="Youtube download complete", text_color="green") 
    except:
        finishedLabel.configure(text="Youtube link is invalid", text_color="red")

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_completation = bytes_downloaded / total_size * 100
    per = str(int(percentage_completation))
    pPercent.configure(text=per + "%")
    pPercent.update()

    #update progressBar
    progressBar.set(float(percentage_completation)/100)

def delete():
    finishedLabel.configure(text="", text_color="white")
    progressBar.set(0)
    pPercent.configure(text= "0%")
    title.configure(text= "")
    link.delete(0, 'end')

#system settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# our app frame
app = customtkinter.CTk()
app.geometry("720x250")
app.title("YouTube Downloader")

#adding UI elements
title = customtkinter.CTkLabel(app, text="Insert a YouTube link")
title.pack(padx=10, pady=10)

#frame link
frameLink = tkinter.Frame(app)
frameLink.pack(pady=10)

#erase button
erase = customtkinter.CTkButton(frameLink, text="Erase", command = delete)
erase.pack(padx=10, pady=10, side=tkinter.LEFT) #si mette .pack() per farlo apparire sulla schermata

#link input
url_val = tkinter.StringVar()
link = customtkinter.CTkEntry(frameLink, width=350, height=40, textvariable = url_val)
link.pack(padx=10, pady=10, side=tkinter.LEFT)

#frame total
frame = tkinter.Frame(app)
frame.pack(pady=10)

#frame for buttons
frameButton = tkinter.Frame(frame)
frameButton.pack(side = tkinter.LEFT)

#frame for progress
frameProgress = tkinter.Frame(frame)
frameProgress.pack(side = tkinter.LEFT, padx=10)

#frame for progress
frameLink = tkinter.Frame(frameProgress)
frameLink.pack(side = tkinter.TOP)

#progress bar
progressBar = customtkinter.CTkProgressBar(frameProgress, width=400)
progressBar.set(0)
progressBar.pack(side = tkinter.BOTTOM)

#download video button
download = customtkinter.CTkButton(frameButton, text="Download Video", command = startDownloadVideo)
download.pack(padx=10, pady=10, side=tkinter.TOP) #si mette .pack() per farlo apparire sulla schermata

#download audio button
downloadAudio = customtkinter.CTkButton(frameButton, text="Download Audio", command = startDownloadAudio)
downloadAudio.pack(padx=10, pady=10, side=tkinter.BOTTOM) #si mette .pack() per farlo apparire sulla schermata

#finished downloading
finishedLabel = customtkinter.CTkLabel(frameLink, text="")
finishedLabel.pack(padx=10, side = tkinter.LEFT)

#Progress Percentage
pPercent = customtkinter.CTkLabel(frameLink, text="0%")
pPercent.pack(side = tkinter.RIGHT)

#Run app
app.mainloop()

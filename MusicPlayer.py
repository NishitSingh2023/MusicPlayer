from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from pygame import mixer
import os

root = Tk()

#Create Menubar
menubar = Menu(root)
root.config(menu=menubar)

#Create sub menu
subMenu = Menu(menubar, tearoff=0)
def browse_file():
    global filename
    filename = filedialog.askopenfilename()

menubar.add_cascade(label='File', menu=subMenu)
subMenu.add_command(label='Open',command=browse_file)
subMenu.add_command(label='Exit',command=root.destroy)

def About_Us():
    messagebox.showinfo('About Music Player','Developer: Nishit Singh \nContact Me: ns2023@gmail.com')

subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Help', menu=subMenu)
subMenu.add_command(label='About Me', command=About_Us)

mixer.init() #initializing the mixer

root.geometry('300x350+750+300')
root.title("Music Player")
root.iconbitmap(r'pics\music_player.ico')

text = Label(root,text='MUSIC PLAYER',fg = "blue", bg = "yellow", font = "Verdana 20 bold")
text.pack(pady=10)

def play_music():
    try:
        paused
    except NameError:

        try:
            mixer.music.load(filename)
            mixer.music.play()
            statusbar['text']= "Playing Music" + '-' + os.path.basename(filename)
        except:
            #tkinter.messagebox.showerror('File Not Found','File Not Found Please import song')
            browse_file()
    else:
        mixer.music.unpause()
        
def stop_music():
    filename = None
    mixer.music.stop()
    statusbar['text']= "Stopped Music"

def pause_music():
    global paused
    paused = TRUE
    mixer.music.pause()

def set_volume(volume):
    volume=int(volume) / 100
    mixer.music.set_volume(volume)

def rewind_music():
    play_music()
    statusbar['text']= "Playing Music" + '-' + os.path.basename(filename)



middleframe = Frame(root)
middleframe.pack(padx=15, pady=15)

#===============================================================================

playphoto = PhotoImage(file='pics\play.png')
playbtn = Button(middleframe, image=playphoto , command=play_music, width=200, bd=5)
playbtn.pack(pady=10)

#===============================================================================

stopphoto = PhotoImage(file='pics\stop.png')
stopbtn = Button(middleframe, image=stopphoto, command=stop_music ,bd=5)
stopbtn.pack(side='left',padx=20, pady=10)

#===============================================================================

pausephoto = PhotoImage(file='pics\pause.png')
pausebtn = Button(middleframe, image=pausephoto, command=pause_music ,bd=5)
pausebtn.pack(side='left',padx=20, pady=10)

#===============================================================================

rewindphoto = PhotoImage(file='pics\\rewind-button.png')
rewindbtn = Button(middleframe, image=rewindphoto, command=rewind_music ,bd=5)
rewindbtn.pack(side='left',padx=20, pady=10)

#===============================================================================

scale = Scale(root, from_=0,to=100,orient=HORIZONTAL, command=set_volume, length=200, bd=5)
scale.set(0.01)
mixer.music.set_volume(0.01)
scale.pack(pady=15)

#===============================================================================

statusbar = Label(root, text='Welcome To Music Player', relief=SUNKEN)
statusbar.pack(side='bottom', fill=X)


root.mainloop() #this helps countinously show windows

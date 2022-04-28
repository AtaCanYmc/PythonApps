from cProfile import label
from cgitb import text
import time
from tkinter import font, ttk,filedialog,messagebox
import SoundCreater, tkinter, os, browser
from tkinter import * 
from playsound import playsound


OutputPath = (os.getcwd()).replace("PythonCode","")+"/UserAudios"
generalPath = (os.getcwd()).replace("PythonCode","")


def generateSound(fileName, message, language="tr", isSlow=False):
    SoundCreater.generateMP3(OutputPath,fileName,language,isSlow,message)
    messagebox.showinfo("Sound Generator","Sound generated")

def downloadMP3(link):
    time.sleep(0.5)
    SoundCreater.YTdownload(OutputPath, link)
    messagebox.showinfo("Sound Generator","Mp3 downloaded")

def playAudio(path):
    SoundCreater.listenMp3(path)

def removeSound(soundPath):
    os.remove(soundPath)
    messagebox.showinfo("Sound Generator","Sound deleted")

def readFile(txtPath):
    if(len(txtPath)<1):
        return " "
    try:
        with open(txtPath, encoding="utf-8") as f:
            return f.read()
    except IOError:
         tkinter.messagebox.showerror(title="NoFile", message="There is no file like that")

def getTxtFile(ourTitle):
    global txtPath, audioText
    txtPath = filedialog.askopenfilename(initialdir=(generalPath+"/UserTexts"), title=ourTitle, filetypes=(("txt files", "*.txt"),("all files", "*.*")))
    audioText.delete(0, END)
    audioText.insert(0,readFile(txtPath))

def getAudioFile(ourTitle):
    global auPath, audio
    auPath = filedialog.askopenfilename(initialdir=(generalPath+"/UserAudios"), title=ourTitle, filetypes=(("mp3 files", "*.mp3"),("all files", "*.*")))
    audio.delete(0, END)
    audio.insert(0,auPath)

def soundByTextWindow():
    global sbt, txtPath, audioText
    ModeChoice = LabelFrame(sbt,text=" <---| Generate sound from text |---> ")
    ModeChoice.pack(pady = 25, padx = 25)

    audioText = Entry(ModeChoice, width= 60, bg="gray", fg="white", borderwidth=5,font=('Helvetica',11))
    audioText.insert(0, "Write here your message or choose a file")
    audioText.grid(row=0,column=0,columnspan=15,rowspan=1, pady=10,padx=10,ipady=70)
    
    fileName = Entry(ModeChoice, width= 20, bg="gray", fg="yellow", borderwidth=5)
    fileName.insert(0, "Audio file name")
    fileName.grid(row=1,column=0,columnspan=15,rowspan=1, pady=20,padx=10,ipady=10)

    fromTxtfile = Button(ModeChoice, text= "Choose a txt file", bg="gray", pady =25, padx = 25 ,command = lambda:getTxtFile("Choose text"))
    fromTxtfile.grid(row=3,column=0,columnspan=1,rowspan=1, pady=7,padx=5) 

    generate = Button(ModeChoice, text= "Generate sound", bg="green", pady =25, padx = 25 ,command = lambda:generateSound(fileName.get(),audioText.get()))
    generate.grid(row=3,column=1,columnspan=1,rowspan=1, pady=7,padx=5) 

def playWindow():
    global player,audio
    global auPath

    ModeChoice = LabelFrame(player,text=" <---| Player |---> ")
    ModeChoice.pack(pady = 25, padx = 25)

    audio = Entry(ModeChoice, width= 80, bg="gray", fg="white", borderwidth=5)
    audio.insert(0, "File path")
    audio.grid(row=0,column=0,columnspan=15,rowspan=1, pady=10,padx=10,ipady=10)

    fromTxtfile = Button(ModeChoice, text= "Choose audio file", bg="gray", pady =25, padx = 25 ,command = lambda:getAudioFile("Choose audio"))
    fromTxtfile.grid(row=2,column=0,columnspan=1,rowspan=1, pady=7,padx=5) 

    play = Button(ModeChoice, text= "Play sound", bg="green", pady =25, padx = 25 ,command = lambda:playAudio(audio.get()))
    play.grid(row=2,column=1,columnspan=1,rowspan=1, pady=7,padx=5) 

    delete = Button(ModeChoice, text= "Delete sound", bg="red", pady =25, padx = 25 ,command = lambda:removeSound(audio.get()))
    delete.grid(row=2,column=2,columnspan=1,rowspan=1, pady=7,padx=5) 

def soundByLinkWindow():
    global YT 

    ModeChoice = LabelFrame(YT,text=" <---| Youtube MP3 |---> ")
    ModeChoice.pack(pady = 25, padx = 25)

    link = Entry(ModeChoice, width= 80, bg="gray", fg="white", borderwidth=5)
    link.insert(0, "Write here Youtube video link")
    link.grid(row=0,column=0,columnspan=15,rowspan=1, pady=10,padx=10,ipady=10)

    generate = Button(ModeChoice, text= "Download Mp3", bg="green", pady =25, padx = 25 ,command = lambda:downloadMP3(link.get()))
    generate.grid(row=1,column=0,columnspan=1,rowspan=1, pady=7,padx=5) 

    openLink = Button(ModeChoice, text= "Open in browser", bg="purple", pady =25, padx = 25 ,command = lambda:browser.openURL(link.get()))
    openLink.grid(row=1,column=1,columnspan=1,rowspan=1, pady=7,padx=5) 

def homeWindow():
    global home,acy
    
    welcome = Label(home, bg= "gray",text="[Welcome to Sound Generator]",font=('Helvetica',11,"bold"))
    welcome.grid(row=0,column=0,columnspan=5,rowspan=1, pady=2,padx=2) 
    welcome2 = Label(home, bg= "gray",text="-Created by ACY-",font=('Helvetica',8,"bold"))
    welcome2.grid(row=2,column=2,columnspan=1,rowspan=1, pady=2,padx=2) 
    photo = Button(home, bg= "gray",image=acy,borderwidth=0,command=lambda:SoundCreater.listenMp3(generalPath+"ProgramUsage/audios/hihi.mp3"))
    photo.grid(row=1,column=2,columnspan=1,rowspan=1, pady=0,padx=2) 

    Me = LabelFrame(home,text=" <---| Follow Me |---> ",bg="gray")
    Me.grid(row=3,column=0,columnspan=5,rowspan=1, pady=10,padx=5)

    Instagram = Button(Me, text= "My Instagram", bg="purple", pady =25, padx = 25 ,command = lambda:browser.openURL("https://www.instagram.com/atcan_ymc/?hl=en"))
    Instagram.grid(row=0,column=0,columnspan=1,rowspan=1, pady=7,padx=5) 

    LinkedIn = Button(Me, text= "My LinkedIn",fg="white", bg="blue", pady =25, padx = 25 ,command = lambda:browser.openURL("https://tr.linkedin.com/in/ata-can-yaymac%C4%B1"))
    LinkedIn.grid(row=0,column=1,columnspan=1,rowspan=1, pady=7,padx=5) 

    Github = Button(Me, text= " My Github ", fg="white", bg="black", pady =25, padx = 25 ,command = lambda:browser.openURL("github.com"))
    Github.grid(row=0,column=2,columnspan=1,rowspan=1, pady=7,padx=5) 

    email = Button(Me, text= " My Email  ", bg="white", pady =25, padx = 25 ,command = lambda:browser.openURL("mailto:atacanymc@gmail.com"))
    email.grid(row=0,column=3,columnspan=1,rowspan=1, pady=7,padx=5) 

def rootWindow():
    global root,sbt,YT,player,home,acy
    root = Tk()
    root.geometry("600x500")
    root.title("Sound Generator")
    root.iconbitmap(generalPath+"ProgramUsage\images\SD_logo.ico")
    acy = PhotoImage(file= generalPath+"/ProgramUsage\images\Acy.png")
    mainBoard = ttk.Notebook(root)
    mainBoard.pack()

    home = Frame(mainBoard, width=600, height=500, bg= "gray")
    home.pack(fill = "both", expand=1)
    homeWindow()

    sbt = Frame(mainBoard, width=600, height=500, bg= "blue")
    sbt.pack(fill = "both", expand=1)
    soundByTextWindow()

    YT = Frame(mainBoard, width=600, height=500, bg= "red")
    YT.pack(fill = "both", expand=1)
    soundByLinkWindow()

    player = Frame(mainBoard, width=600, height=500, bg= "yellow")
    player.pack(fill = "both", expand=1)
    playWindow()

    mainBoard.add(home, text= "< Home >")
    mainBoard.add(sbt, text= "< Txt to voice >")
    mainBoard.add(YT, text= "< Youtube Mp3 >")
    mainBoard.add(player, text= "< Play audio >")

    root.mainloop()

rootWindow()


from gtts import gTTS
from playsound import playsound
import youtube_dl, os


#language="tr"

def generateMP3(filePath, fileName, language, isSlow, message):
    sound = gTTS(text=message, lang=language, slow=isSlow)
    soundFile = filePath+"/"+fileName+".mp3"
    sound.save(soundFile)
    return soundFile

def YTdownload(filePath, video_url):
    video_info = youtube_dl.YoutubeDL().extract_info(
        url = video_url,download=False
    )
    title = ""
    title = (video_info['title'])
    title = title.replace(" ", "")
    filename =filePath+ f"/{title}.mp3"
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':filename,
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])
    print("Download complete... {}".format(filename))
    return filename

def listenMp3(filePath):
    try:
        playsound(filePath)
    except:
        #filePath = "file:///"+filePath
        os.system("start \"\" "+ filePath)



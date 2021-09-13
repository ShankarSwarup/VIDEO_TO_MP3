from tkinter import * 
import moviepy.editor as mp
from tkinter import filedialog as fd
import datetime

class video:
    def __init__(self, root):
        self.root = root
        self.root.geometry("900x500+200+50")
        self.root.title("Video_to_mp3")
        self.root.resizable(False, False)

        self.download_path = StringVar()

        title = Label(self.root, text="VIDEO TO MP3", font=("times new roman", 40), bg='#053246',
                      fg='white').place(x=0, y=0, relwidth=1)

        lbl_location=Label(self.root,text='Pick a Location',font=("times new roman",15),bg='white').place(x=10,y=100)
        txt_location=Entry(self.root,textvariable=self.download_path,font=("times new roman",13),bg="#d9fcff").place(x=260,y=100,width=340,height=30)


        btn_dir = Button(self.root, text='Choose File', command=self.Browse, font=("times new roman", 13, 'bold'), bg='#607d8b',
                         fg='white').place(x=640, y=100, width=150, height=20)

        btn_convert = Button(self.root, text='Convert', command=self.convert, font=("times new roman", 13, 'bold'), bg='black',
                         fg='white').place(x=300, y=160, width=150, height=20)



    def Browse(self):
        download_Directory = fd.askopenfilename(initialdir="YOUR DIRECTORY PATH")
        self.download_path.set(download_Directory)

    def convert(self):
        video=mp.VideoFileClip(self.download_path.get())
        time_stamp=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        file_name=f'audio-{time_stamp}.mp3'
        video.audio.write_audiofile(file_name)



root=Tk()
obj=video(root)
root.mainloop()

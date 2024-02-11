import customtkinter as ctk
from yt_dlp import YoutubeDL

# Get GUI working for program
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Resolution | Title | Appearance
        self.geometry("400x200")
        self.title("YT-DLP to MP3")
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("dark-blue")

        '''
        URL Input
        '''
        # URL Label
        self.label_url_input = ctk.CTkLabel(self, text="URL", fg_color="transparent")
        self.label_url_input.place(x=40, y=60)
        # URL Input
        self.url_input = ctk.CTkEntry(self,width=250, height=20, placeholder_text="Youtube URL")
        self.url_input.place(x=100, y=63)

        '''
        Download Button
        '''
        self.download_button = ctk.CTkButton(self, text="Download", command=self.output)
        self.download_button.place(x=135, y=100)
    
    def output(self):
        print(self.url_input.get())
        URLS = self.url_input.get()
        ydl_opts = {
            'cookiesfrombrowser:': 'default',
            'outtmpl': '~/Music/%(title)s.%(ext)s',
            'format': 'mp3/bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
            }]
        }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download(URLS)



app = App()
app.mainloop()
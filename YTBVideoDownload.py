from guizero import *
import pytube as ytb
import os
from threading import Thread

class ThreadDownload(Thread):
    def __init__(self, url, mod):
        super(ThreadDownload, self).__init__()
        self.url = url
        self.mod = mod

    def run(self):
        os.makedirs("YTB_downloads/", exist_ok=True)
        self.video = ytb.YouTube(self.url, on_progress_callback=self.update)
        if self.mod == "vidéo (.mp4)":
            self.video.streams.get_highest_resolution().download("YTB_downloads/")
        else:
            self.video.streams.get_audio_only().download("YTB_downloads/")

    def update(self, chunk, file_handle, bytes_remaining):
        global per
        per = str(round((1 - bytes_remaining / self.video.streams.get_highest_resolution().filesize) * 100, 3)) +  "% done..."

class AppCreate(App):
    def __init__(self):
        super().__init__(title="YouTube Downloader", width=350, height=350, layout="grid", bg="#31465d")

        self.create_widgets()

    def create_widgets(self):
        self.text_down = Text(self, text="Entrez lien de la vidéo:", grid=[0, 0])
        self.text_get = TextBox(self, grid=[0, 1], width=50)
        self.combo_ytb = Combo(self, options=["vidéo (.mp4)", "audio (.mp3)"], grid=[0, 2])
        self.button_down = PushButton(self, text="Télécharger", grid=[0, 3], command=self.download)
        self.button_down.bg = "red"
        self.time_remaining = Text(self, text="", grid=[0, 0], visible=False)

    def download(self):
        download = ThreadDownload(self.text_get.value, self.combo_ytb.value)
        download.start()
        self.text_get.clear()
        self.time_remaining.visible = True
        self.text_get.visible = self.combo_ytb.visible = self.button_down.visible = self.text_down.visible = False
        self.repeat(200, self.anim)

    def anim(self):
        global per
        if per == "":
            self.time_remaining.value = "En attente du serveur..."
        elif per[:-9] == "100.0":
            self.time_remaining.visible = False
            self.text_get.visible = self.combo_ytb.visible = self.button_down.visible = self.text_down.visible = True
            self.cancel(self.anim)
        else:
            self.time_remaining.value = per


if __name__ == "__main__":
    per = ""
    app_dow = AppCreate()
    app_dow.display()
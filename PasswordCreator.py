from guizero import *
import random as r

class AppCreate(App):
    def __init__(self):
        super().__init__(title="Password Generator", width=350, height=350, layout="grid")

        self.list_chars = {
            "hex-lower": "abcdefghijklmnopqrstuvwxyz0123456789 ",
            "hex-upper": "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ",
            "numeric": "0123456789 ",
            "symbols": "!@#$%^&*()-_+= ",
            "all-lower": "!@#$%^&*()-_+=abcdefghijklmnopqrstuvwxyz0123456789 ",
            "all-upper": "!@#$%^&*()-_+=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ",
            "all": "!@#$%^&*()-_+=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
        }

        self.create_widgets()

    def create_widgets(self):
        self.label_slider = Text(self, text="Selectionnez le nombre de charactères", grid=[0, 0])
        self.slider_chars = Slider(self, end=30, grid=[0, 1])
        self.buton_gen = PushButton(self, text="Générer", command=self.generate, grid=[0, 4])
        self.combo_affich = Combo(self, options=[k for (k, val) in self.list_chars.items()], grid=[0, 3])
        self.text_show = Text(self, grid=[0, 5])

    def generate(self):
        l = []
        l[:0] = (self.list_chars.get(self.combo_affich.value))
        str_passwd = ""
        for a in range(self.slider_chars.value):
            str_passwd += r.choice(l)

        self.text_show.clear()
        self.text_show.append(str_passwd)


if __name__ == "__main__":

    app_gen = AppCreate()
    app_gen.display()
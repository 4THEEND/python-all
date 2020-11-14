try:
    from tkinter import messagebox
    import tkinter as tk
    import base64 as b64
    import os
except ImportError:
    from Tkinter import messagebox
    import Tkinter as tk
    import base64 as b64
    import os


def save(file_name=None, mod=None, text=""):
    try:
        file = open(file_name + ".ism", mod)
        file.write(text)
        file.close()
    except:
        pass


def read(file_name, mod="r"):
    try:
        file = open(file_name + ".ism", mod)
        buffer = file.read()
        file.close()
    except:
        buffer = ""

    return buffer


class Open_Window_Frame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.filename_entry = tk.Entry(self)
        self.button_submit = tk.Button(self, command=self.save_quit, text="Ouvrir")
        self.write_label = tk.Label(self, anchor="center", text="Entrez nom du fichier:\n")

        self.write_label.pack()
        self.filename_entry.pack()
        self.button_submit.pack()

    def save_quit(self):
        global file_name
        file_name = self.filename_entry.get()
        if file_name != "":
            self.master.destroy()
        else:
            tk.messagebox.showinfo("Erreur", "Nom de fichier invalide")


class Submit_Window_Frame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.filename_entry = tk.Entry(self)
        self.button_submit = tk.Button(self, command=self.save_quit, text="enregistrer")
        self.write_label = tk.Label(self, anchor="center", text="Entrez nom du fichier:\n")

        self.write_label.pack()
        self.filename_entry.pack()
        self.button_submit.pack()

    def save_quit(self):
        global file_name
        file_name = self.filename_entry.get()
        if file_name != "":
            save(file_name, "w", all_text)
            self.master.destroy()
        else:
            tk.messagebox.showinfo("Erreur", "Nom de fichier invalide")

class Help_frame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.CreateMenuBar()
        self.add_listeners()

        self.is_saved = 0

    def create_widgets(self):
        self.text_inside_label = tk.StringVar()
        self.buffer = tk.StringVar()

        self.label_frame_text = tk.LabelFrame(self, text="(Empty)")
        self.preview_save = tk.Text(self.label_frame_text, height=400, width=500)

        self.label_frame_text.pack()
        self.preview_save.pack()

    def add_listeners(self):
        self.master.protocol("WM_DELETE_WINDOW", self.close)

    def close(self):
        if self.is_saved == 0:
            if not tk.messagebox.askyesno("Quitter", "Voulez vous quitter sans enregistrer ?"):
                self.save()
        self.quit()


    def CreateMenuBar(self):
        menuBar = tk.Menu(self.master)
        menuFile = tk.Menu(menuBar, tearoff=0)

        menuFile.add_command(label="New", command=self.new_page)
        menuFile.add_command(label="Open", command=self.open)
        menuFile.add_command(label="Save as", command=self.save_as)
        menuFile.add_separator()
        menuFile.add_command(label="Exit", command=self.quit)

        menuBar.add_cascade(label="File", menu=menuFile)

        menuBar.add_command(label="Save", command=self.save)
        menuBar.add_command(label="Help", command=self.help)

        self.master.config(menu=menuBar)

    def save_as(self):
        global all_text, file_name
        all_text = self.preview_save.get("0.0", "end")
        window_temp_submit = tk.Toplevel()
        window_temp_submit.geometry("150x90")
        window_temp_submit.title("Saver")
        window_temp_submit.maxsize(150, 90)

        app_temp_submit = Submit_Window_Frame(window_temp_submit)

        self.master.wait_window(window_temp_submit)

        self.label_frame_text["text"] = file_name + ".ism"
        self.is_saved = 1

    def save(self):
        global file_name, all_text
        if file_name == "":
            self.save_as()
            self.text_inside_label.set(file_name)
        else:
            all_text = self.preview_save.get("0.0", "end")
            save(file_name, "w", all_text)
        self.is_saved = 1

    def open(self):
        window_temp_open = tk.Toplevel()
        window_temp_open.geometry("150x90")
        window_temp_open.title("Open")
        window_temp_open.maxsize(150, 90)

        app_temp_submit = Open_Window_Frame(window_temp_open)

        self.master.wait_window(window_temp_open)

        self.open_affich()

    def open_affich(self):
        if file_name != "":
            self.preview_save.delete(0.0, tk.END)
            buffer = read(file_name)
            self.preview_save.insert(tk.END, buffer)
            self.label_frame_text["text"] = file_name + ".ism"
            self.is_saved = 1

    def new_page(self):
        self.preview_save.delete(0.0, tk.END)
        self.label_frame_text["text"] = "New Document"

    def help(self):
        help_window = tk.Toplevel()
        help_window.title("Help")

        help_window_frame = Help_frame(help_window)

        self.master.wait_window(help_window)


if __name__ == "__main__":
    all_text = file_name = ""

    window = tk.Tk()
    window.geometry("600x500")
    window.title("Bloc note")
    window.maxsize(600, 500)

    app = App(window)
    app.mainloop()


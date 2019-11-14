"""
Text Editor - Notepad style application that can open, edit, and save text documents.
Python version: 3.x
"""


from tkinter import *
import tkinter.filedialog as tk
import tkinter.messagebox as tk2
import os


class NotepadApp(Frame):

    def __init__(self, master):
        super(NotepadApp, self).__init__(master)
        self.file = None
        self.text = Text(width=20, height=20)
        self.scroll = Scrollbar()
        self.scroll.config(command=self.text.yview)
        self.text.config(yscrollcommand=self.scroll.set)
        self.scroll.pack(side=RIGHT, fill=Y)
        self.text.pack(expand=YES, fill=BOTH)
        self.create_widgets()

    def create_widgets(self):
        menubar = Menu(self)
        root.config(menu=menubar)

        file_menu = Menu(menubar)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_cmd, accelerator="Ctrl+N")
        file_menu.add_command(label="Open", command=self.open_cmd, accelerator="Ctrl+O")
        file_menu.add_command(label="Save", command=self.save_cmd, accelerator="Ctrl+S")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit_cmd, accelerator="Ctrl+Q")

        edit_menu = Menu(menubar)
        menubar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Cut", command=self.cut_cmd, accelerator="Ctrl+X")
        edit_menu.add_command(label="Copy", command=self.copy_cmd, accelerator="Ctrl+C")
        edit_menu.add_command(label="Paste", command=self.paste_cmd, accelerator="Ctrl+V")
        edit_menu.add_separator()
        edit_menu.add_command(label="Clear", command=self.clear_cmd)
        edit_menu.add_command(label="ClearAll", command=self.clearall_cmd)

        help_menu = Menu(menubar)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About...", command=self.about_cmd)

        root.bind_all("<Control-n>", lambda event: self.new_cmd())
        root.bind_all("<Control-o>", lambda event: self.open_cmd())
        root.bind_all("<Control-s>", lambda event: self.save_cmd())
        root.bind_all("<Control-q>", lambda event: self.exit_cmd())
        root.bind_all("<Control-x>", lambda event: self.cut_cmd)
        root.bind_all("<Control-c>", lambda event: self.copy_cmd)
        root.bind_all("<Control-v>", lambda event: self.paste_cmd)

    def new_cmd(self):
        if (tk2.askyesno("Message", "Unsaved work will be lost. Continue?")):
            root.title("Untitled - Notepad")
            self.file = None
            self.text.delete("1.0", END)

    def open_cmd(self):
        self.file = tk.askopenfilename(title="Select a file", defaultextension=".txt",
            filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

        if self.file == "":
            self.file = None
        else:
            root.title(os.path.basename(self.file) + " - Notepad")
            self.text.delete("1.0", END)

            with open(self.file, "r") as read_handle:
                contents = read_handle.read()
            self.text.insert("1.0", contents)

    def save_cmd(self):
        if self.file == None:
            user_text = self.text.get("1.0", END)
            self.file = tk.asksaveasfilename(initialfile='Untitled.txt',
                defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

            if self.file == "":
                self.file = None
            else:
                with open(self.file, "w") as write_handle:
                    write_handle.write(user_text)
                root.title(os.path.basename(self.file) + " - Notepad")
        else:
            with open(self.file, "w") as write_handle:
                write_handle.write(self.text.get(1.0, END))

    def exit_cmd(self):
        if tk2.askokcancel("Quit", "Do you really want to quit?"):
            root.destroy()

    def about_cmd(self):
        _ = tk2.showinfo("About", "This is the text editor made by Megha Bisani")

    def cut_cmd(self):
        self.text.event_generate("<<Cut>>")

    def copy_cmd(self):
        self.text.event_generate("<<Copy>>")

    def paste_cmd(self):
        self.text.event_generate("<<Paste>>")

    def clear_cmd(self):
        self.text.event_generate("<<Clear>>")

    def clearall_cmd(self):
        self.text.delete(1.0, END)


if __name__ == '__main__':
    root = Tk()
    root.title("Megha's Notepad")
    root.geometry('700x600')
    root.call('wm', 'iconphoto', root._w, PhotoImage(file='icon.gif'))
    app = NotepadApp(root)
    app.mainloop()

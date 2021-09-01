import pyshorteners
import tkinter
from tkinter import messagebox


class url_shortner:
    def __init__(self, master):
        # defining the window
        self.master = master
        self.master.title("URL shortner")
        self.master.geometry("500x200")
        self.master.resizable(False, False)

        # window wigets
        self.title = tkinter.Label(self.master, text="URL Shorter", font=('verdana', 16, 'bold'), fg="blue")
        self.title.place(x=180, y=5)

        self.input_bar = tkinter.Entry(self.master, width=34, font="14", bg="lightgrey",
                                       relief="groove", borderwidth=2)
        self.input_bar.place(x=100, y=50)

        self.button_short = tkinter.Button(self.master, text="short", relief="groove", font=(
            'verdana', 10, 'bold'), bg="blue", fg="white", command=self.shortner)
        self.button_short.place(x=180, y=130)
        self.button_expand = tkinter.Button(self.master, text="expand", relief="groove", font=(
            'verdana', 10, 'bold'), bg="blue", fg="white", command=self.expander)
        self.button_expand.place(x=260, y=130)

    def shortner(self):
        if self.input_bar.get() == "":
            messagebox.showerror("Error", "Please Enter an URL")
        else:
            self.url = self.input_bar.get()
            self.s = pyshorteners.Shortener()
            self.shorturl = self.s.tinyurl.short(self.url)

            self.short_output = tkinter.Entry(self.master, width=34, font="14", bg="lightgrey",
                                       relief="groove", borderwidth=2)
            self.short_output.insert(self.shorturl)
            self.short_output.place(x=100, y=90)

    def expander(self):
        if self.input_bar.get() == "":
            messagebox.showerror("Error", "Please Enter an URL")
        else:
            self.url = self.input_bar.get()
            self.abc = pyshorteners.Shortener()
            self.expand = self.abc.tinyurl.expand(self.url)

            self.expand_output = tkinter.Entry(self.master, width=34, font="14", bg="lightgrey",
                                       relief="groove", borderwidth=2)
            self.expand_output.insert(str(self.expand))
            self.expand_output.place(x=100, y=90)

#start of the programm
if __name__ == "__main__":
    master = tkinter.Tk()
    URL = url_shortner(master)
    master.mainloop()

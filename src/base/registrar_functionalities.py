from tkinter import *
import tkinter
from PIL import Image, ImageTk
from src.utils.create_account import Register
from src.utils.delete_account import DeleteAccount
from src.base.case_query import CaseQueries


class Registrar:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1230x590+0+0")
        self.root.title("Registrar")

        img1 = Image.open(r"C:\BI\Projects\judiciary-information-system\src\data\images\TLL.jpg")
        img1 = img1.resize((410, 130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=0, width=410, height=130)

        img2 = Image.open(r"C:\BI\Projects\judiciary-information-system\src\data\images\TC.jpg")
        img2 = img2.resize((410, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=410, y=0, width=410, height=130)

        img3 = Image.open(r"C:\BI\Projects\judiciary-information-system\src\data\images\TR.jpg")
        img3 = img3.resize((410, 130), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        f_lbl = Label(self.root, image=self.photoimg3)
        f_lbl.place(x=820, y=0, width=410, height=130)

        img4 = Image.open(r"C:\BI\Projects\judiciary-information-system\src\data\images\dev.jpg")
        img4 = img4.resize((1230, 590), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=0, relwidth=1, relheight=1)

        # Buttons
        img5 = Image.open(r"C:\BI\Projects\judiciary-information-system\src\data\images\Train.jpg")
        img5 = img5.resize((140, 110), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b1 = Button(bg_img,
                    image=self.photoimg5,
                    command=self.create_account,
                    cursor="hand2")
        b1.place(x=180, y=120, width=140, height=100)
        b1_1 = Button(bg_img,
                      text="Create Account",
                      command=self.create_account,
                      cursor="hand2",
                      font=("lucida handwriting", 10),
                      bg="black",
                      fg="white")
        b1_1.place(x=180, y=220, width=140, height=40)

        img6 = Image.open(r"C:\BI\Projects\judiciary-information-system\src\data\images\Help.jpg")
        img6 = img6.resize((140, 110), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)
        b1 = Button(bg_img,
                    image=self.photoimg6,
                    cursor="hand2",
                    command=self.delete_account)
        b1.place(x=400, y=120, width=140, height=100)
        b1_1 = Button(bg_img,
                      text="Delete Account",
                      cursor="hand2",
                      command=self.delete_account,
                      font=("lucida handwriting", 10),
                      bg="black",
                      fg="white")
        b1_1.place(x=400, y=220, width=140, height=40)

        img7 = Image.open(r"C:\BI\Projects\judiciary-information-system\src\data\images\StudentDetails.jpg")
        img7 = img7.resize((140, 110), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)
        b1 = Button(bg_img,
                    image=self.photoimg7,
                    cursor="hand2",
                    command=self.query_cases)
        b1.place(x=620, y=120, width=140, height=100)
        b1_1 = Button(bg_img,
                      text="Case Queries",
                      cursor="hand2",
                      command=self.query_cases,
                      font=("lucida handwriting", 10),
                      bg="black",
                      fg="white")
        b1_1.place(x=620, y=220, width=140, height=40)

        img8 = Image.open(r"C:\BI\Projects\judiciary-information-system\src\data\images\exit.jpg")
        img8 = img8.resize((140, 110), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)
        b1 = Button(bg_img,
                    image=self.photoimg8,
                    cursor="hand2",
                    command=self.exit)
        b1.place(x=840, y=120, width=140, height=100)
        b1_1 = Button(bg_img,
                      text="Exit",
                      cursor="hand2",
                      command=self.exit,
                      font=("lucida handwriting", 10),
                      bg="black",
                      fg="white")
        b1_1.place(x=840, y=220, width=140, height=40)

    def exit(self):
        self.exit = tkinter.messagebox.askyesno("Exit", "Are you sure you want to exit?", parent=self.root)
        if self.exit > 0:
            self.root.destroy()
        else:
            return

    # Functions

    def create_account(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

    def delete_account(self):
        self.new_window = Toplevel(self.root)
        self.app = DeleteAccount(self.new_window)

    def query_cases(self):
        self.new_window = Toplevel(self.root)
        self.app = CaseQueries(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = Registrar(root)
    root.mainloop()

from tkinter import *
from PIL import Image, ImageTk


class PaymentWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1230x590+0+0")

        self.username = StringVar()
        self.password = StringVar()
        self.combo_securityQ = StringVar()
        self.combo_securityA = StringVar()
        self.new_pass = StringVar()

        img = Image.open(r"C:\BI\Projects\judiciary-information-system\src\data\images\dev.jpg")
        img = img.resize((1230, 590), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0, relwidth=1, relheight=1)

        # self.root2 = Frame(self.root, bd=2, bg="black")
        # self.root2.place(x=484, y=115, width=350, height=380)

        img1 = Image.open(r"C:\BI\Projects\judiciary-information-system\src\data\images\qr.png")
        img1 = img1.resize((279, 279), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root, image=self.photoimg1, bg='black', borderwidth=0)
        f_lbl.place(x=520, y=150, width=279, height=279)


if __name__ == "__main__":
    root = Tk()
    obj = PaymentWindow(root=root)
    root.mainloop()

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import requests


class DeleteAccount:
    def __init__(self, root):
        self.root = root
        self.root.title("Delete Account")
        self.root.geometry("1230x590+0+0")

        # Variables
        self.var_email = StringVar()
        self.var_pass = StringVar()

        img = Image.open(r"C:\BI\Projects\judiciary-information-system\src\data\images\dev.jpg")
        img = img.resize((1230, 590), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0, relwidth=1, relheight=1)

        img1 = Image.open(r"C:\BI\Projects\judiciary-information-system\src\data\images\kobe.jpg")
        img1 = img1.resize((300, 400), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        bg_img1 = Label(self.root, image=self.photoimg1, bg='black')
        bg_img1.place(x=80, y=70, width=350, height=450)

        main_frame = Frame(self.root, bd=2, bg="lightblue")
        main_frame.place(x=430, y=75, width=700, height=450)

        main_label = Label(main_frame,
                           text="DELETE ACCOUNT",
                           font=("times new roman", 20),
                           bd=2,
                           bg="lightblue")
        main_label.place(x=10, y=20)

        username_lbl = Label(main_frame,
                             text="Username",
                             font=("lucida handwriting", 10, "bold"),
                             bg='lightblue')
        username_lbl.place(x=150, y=150)
        self.user_entry = ttk.Entry(main_frame,
                                    textvariable=self.var_email,
                                    width=37,
                                    font=("times new roman", 10,))
        self.user_entry.place(x=150, y=180)

        img2 = Image.open(r"C:\BI\Projects\judiciary-information-system\src\data\images\del.webp")
        img2 = img2.resize((150, 30), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        b1 = Button(main_frame,
                    image=self.photoimg2,
                    command=self.delete,
                    borderwidth=0,
                    cursor="hand2",
                    font=("times new roman", 12),
                    fg='lightblue')
        b1.place(x=200, y=350, width=150)

    # Functions
    def delete(self):
        if self.var_email.get() == "":
            messagebox.showerror("Error", "Please enter a valid username.")
        else:
            url = "https://bigquery-cloudbuild-f7q24pru5q-ey.a.run.app/bigquery_operation_results"
            headers = {"Content-type": "application/json"}
            _dict = {
                "query": f'''
                            DELETE FROM `sandbox-381608.jis.registered_users`
                            WHERE email= "{self.var_email.get()}"
                        ''',
                "gbq_table_id": "sandbox-381608.jis.registered_users",
            }
            _response = requests.post(url, headers=headers, json=_dict)
            _result = _response.json()
            messagebox.showinfo("Success", "User account deletion successful.")


if __name__ == "__main__":
    root = Tk()
    obj = DeleteAccount(root)
    root.mainloop()

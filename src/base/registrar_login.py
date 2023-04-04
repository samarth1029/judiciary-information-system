from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import requests
from src.base.registrar_functionalities import Registrar


class RegistrarLoginWindow:
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

        self.root2 = Frame(self.root, bd=2, bg="black")
        self.root2.place(x=484, y=115, width=270, height=332)

        img1 = Image.open(r"C:\BI\Projects\judiciary-information-system\src\data\images\user-modified.png")
        img1 = img1.resize((79, 74), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root, image=self.photoimg1, bg='black', borderwidth=0)
        f_lbl.place(x=579, y=125, width=79, height=74)

        get_str = Label(self.root2,
                        text="Get Started",
                        font=("lucida handwriting", 12, "bold"),
                        fg='white',
                        bg="black")
        get_str.place(x=80, y=85)

        username_lbl = Label(self.root2,
                             text="Username",
                             font=("lucida handwriting", 10),
                             fg='white',
                             bg="black")
        username_lbl.place(x=20, y=125)

        self.user_entry = ttk.Entry(self.root2,
                                    textvariable=self.username,
                                    width=37,
                                    font=("times new roman", 10))
        self.user_entry.place(x=20, y=145)

        pass_lbl = Label(self.root2,
                         text="Password",
                         font=("lucida handwriting", 10),
                         fg='white',
                         bg="black")
        pass_lbl.place(x=20, y=175)

        self.pass_entry = ttk.Entry(self.root2,
                                    textvariable=self.password,
                                    width=37,
                                    font=("times new roman", 10),
                                    show='*')
        self.pass_entry.place(x=20, y=195)

        login_btn = Button(self.root2,
                           text="Login",
                           command=self.login,
                           width=14,
                           font=("times new roman", 13),
                           bg="red",
                           fg="white",
                           activeforeground='white',
                           activebackground='red')
        login_btn.place(x=70, y=230)

    def login(self):
        if self.user_entry.get == "" or self.pass_entry.get() == "":
            messagebox.showerror("Error", "All fields required.")
        else:
            url = "https://bigquery-cloudbuild-f7q24pru5q-ey.a.run.app/bigquery_operation_results"
            headers = {"Content-type": "application/json"}
            _dict = {
                "query": f'''
                            SELECT * FROM `sandbox-381608.jis.registered_users`
                            WHERE 
                            email="{self.username.get()}" and 
                            password="{self.password.get()}"
                        ''',
                "gbq_table_id": "sandbox-381608.jis.registered_users",
            }
            _response = requests.post(url, headers=headers, json=_dict)
            _result = _response.json()
            if len(_result.get("query_results").get("results")) > 0:
                open_main = messagebox.askyesno("Query", "Access only admin?")
                if open_main > 0:
                    self.new_window = Toplevel(self.root)
                    self.app = Registrar(self.new_window)
                elif not open_main:
                    return
            else:
                messagebox.showerror("Error", "Invalid username and password.")


if __name__ == "__main__":
    root = Tk()
    obj = RegistrarLoginWindow(root=root)
    root.mainloop()

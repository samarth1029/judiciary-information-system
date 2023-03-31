import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox, ttk
import pandas as pd


class DfToTkinterTable:
    def __init__(self, root):
        self.root = root
        self.root.geometry("500x500")
        self.root.pack_propagate(False)
        self.root.resizable(0, 0)

        # Frame for TreeView
        frame1 = tk.LabelFrame(root, text="Excel Data")
        frame1.place(height=250, width=500)

        # Frame for open file dialog
        file_frame = tk.LabelFrame(root, text="Open File")
        file_frame.place(height=100, width=400, rely=0.65, relx=0)

        # Buttons
        button1 = tk.Button(file_frame, text="Browse A File", command=lambda: self.File_dialog())
        button1.place(rely=0.65, relx=0.50)

        button2 = tk.Button(file_frame, text="Load File", command=lambda: self.Load_excel_data())
        button2.place(rely=0.65, relx=0.30)

        # The file/file path text
        self.label_file = ttk.Label(file_frame, text="No File Selected")
        self.label_file.place(rely=0, relx=0)

        self.tv1 = ttk.Treeview(frame1)
        self.tv1.place(relheight=1, relwidth=1)

        treescrolly = tk.Scrollbar(frame1, orient="vertical", command=self.tv1.yview)
        treescrollx = tk.Scrollbar(frame1, orient="horizontal", command=self.tv1.xview)
        self.tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
        treescrollx.pack(side="bottom", fill="x")
        treescrolly.pack(side="right", fill="y")

    def File_dialog(self):
        """This Function will open the file explorer and assign the chosen file path to label_file"""
        filename = filedialog.askopenfilename(initialdir="/",
                                              title="Select A File",
                                              filetype=(("xlsx files", "*.xlsx"), ("All Files", "*.*")))
        self.label_file["text"] = filename
        return None

    def Load_excel_data(self):
        """If the file selected is valid this will load the file into the Treeview"""
        file_path = self.label_file["text"]
        try:
            # excel_filename = r"{}".format(file_path)
            excel_filename=r"C:\BI\Projects\judiciary-information-system\src\data\query_result.xlsx"
            if excel_filename[-4:] == ".csv":
                df = pd.read_csv(excel_filename)
            else:
                df = pd.read_excel(excel_filename)

        except ValueError:
            tk.messagebox.showerror("Information", "The file you have chosen is invalid")
            return None
        except FileNotFoundError:
            tk.messagebox.showerror("Information", f"No such file as {file_path}")
            return None

        self.clear_data()
        self.tv1["column"] = list(df.columns)
        self.tv1["show"] = "headings"
        for column in self.tv1["columns"]:
            self.tv1.heading(column, text=column)

        df_rows = df.to_numpy().tolist()
        for row in df_rows:
            self.tv1.insert("", "end", values=row)
        return None

    def clear_data(self):
        self.tv1.delete(*self.tv1.get_children())
        return None


if __name__ == "__main__":
    root = Tk()
    obj = DfToTkinterTable(root)
    root.mainloop()

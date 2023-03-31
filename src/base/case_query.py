from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from PIL import Image, ImageTk
import requests
import pandas as pd
from src.utils.df_to_tkinter_table import DfToTkinterTable
from src.utils.df_to_excel_resolver import df_to_excel


class CaseQueries:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1230x590+0+0")
        self.root.title("Query Cases")

        # Variables
        self.var_start_date = StringVar()
        self.var_end_date = StringVar()
        self.var_date = StringVar()
        self.var_search = StringVar()

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

        img4 = Image.open(r"C:\BI\Projects\judiciary-information-system\src\data\images\download.jpg")
        img4 = img4.resize((1230, 460), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=130, width=1230, height=460)

        title_lbl = Label(bg_img,
                          text="JUDICIARY INFORMATION SYSTEM",
                          font=("times new roman", 35, "bold"),
                          bg="white",
                          fg="black")
        title_lbl.place(x=0, y=0, width=1230, height=45)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=10, y=55, width=1200, height=390)

        # label frames
        # left
        left_frame = LabelFrame(main_frame,
                                bd=2,
                                relief=RIDGE,
                                text="Case Details",
                                bg="black",
                                fg="white",
                                font=("times new roman", 12, "bold"))
        left_frame.place(x=10, y=10, width=570, height=360)

        start_date_label = Label(left_frame,
                                 text="Start Date",
                                 font=("times new roman", 12),
                                 fg='white',
                                 bg='black')
        start_date_label.grid(row=4, column=0, padx=10, sticky=W)
        self.start_date_entry = DateEntry(left_frame,
                                          textvariable=self.var_start_date,
                                          width=20,
                                          font=("times new roman", 12))
        self.start_date_entry.grid(row=4, column=1, padx=2, pady=10, sticky=W)

        end_date_label = Label(left_frame,
                               text="End Date",
                               font=("times new roman", 12),
                               fg='white',
                               bg='black')
        end_date_label.grid(row=5, column=0, padx=10, sticky=W)
        self.end_date_entry = DateEntry(left_frame,
                                        textvariable=self.var_end_date,
                                        width=20,
                                        font=("times new roman", 12))
        self.end_date_entry.grid(row=5, column=1, padx=2, pady=10, sticky=W)

        date_label = Label(left_frame,
                           text="Date",
                           font=("times new roman", 12),
                           fg='white',
                           bg='black')
        date_label.grid(row=3, column=0, padx=10, sticky=W)
        self.date_entry = DateEntry(left_frame,
                                    textvariable=self.var_date,
                                    width=20,
                                    font=("times new roman", 12))
        self.date_entry.grid(row=3, column=1, padx=2, pady=10, sticky=W)

        search_label = Label(left_frame,
                             text="Enter Keywords",
                             font=("times new roman", 12),
                             fg='white',
                             bg='black')
        search_label.grid(row=6, column=0, padx=10, sticky=W)
        search_entry = ttk.Entry(left_frame,
                                 textvariable=self.var_search,
                                 width=20,
                                 font=("times new roman", 12))
        search_entry.grid(row=6, column=1, padx=2, pady=10, sticky=W)

        pending_btn = Button(left_frame,
                             text="Pending Cases",
                             command=self.query_pending_cases,
                             width=15,
                             font=("times new roman", 13),
                             bg="darkblue",
                             fg="white")
        pending_btn.grid(row=8, column=0, padx=10, pady=100)

        resolved_btn = Button(left_frame,
                              text="Resolved Cases",
                              command=self.query_resolved_cases,
                              width=15,
                              font=("times new roman", 13),
                              bg="darkblue",
                              fg="white")
        resolved_btn.grid(row=5, column=2)

        date_btn = Button(left_frame,
                          text="Cases on Date",
                          command=self.query_cases_on_date,
                          width=15,
                          font=("times new roman", 13),
                          bg="darkblue",
                          fg="white")
        date_btn.grid(row=3, column=2)

        reset_btn = Button(left_frame,
                           text="Reset",
                           command=self.reset_data,
                           width=15,
                           font=("times new roman", 13),
                           bg="darkblue",
                           fg="white")
        reset_btn.grid(row=8, column=2)

        case_status_btn = Button(left_frame,
                                 text="View case Status",
                                 command=self.query_case_status,
                                 width=15,
                                 font=("times new roman", 13),
                                 bg="darkgreen",
                                 fg="white")
        case_status_btn.grid(row=6, column=2, padx=28, pady=4)

        # Right
        right_frame = LabelFrame(main_frame,
                                 bd=2,
                                 relief=RIDGE,
                                 text="Case Details",
                                 font=("times new roman", 12, "bold"),
                                 bg="black",
                                 fg="white")
        right_frame.place(x=600, y=10, width=570, height=360)

        # table frame
        table_frame = LabelFrame(right_frame,
                                 bd=2,
                                 relief=RIDGE,
                                 text="Table Frame",
                                 font=("times new roman", 13, "bold"))
        table_frame.place(x=5, y=5, width=550, height=330)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.student_table = ttk.Treeview(table_frame,
                                          columns=(
                                              "CIN",
                                              "StartDate",
                                              "NextHearing",
                                              "Defendant",
                                              "Address",
                                              "Crime",
                                              "Lawyer",
                                              "Prosecutor",
                                              "Judge",
                                              "EndDate",
                                              "JudgementSummary"
                                          ),
                                          xscrollcommand=scroll_x.set,
                                          yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("CIN", text="CIN")
        self.student_table.heading("StartDate", text="Start Date")
        self.student_table.heading("NextHearing", text="Next Hearing")
        self.student_table.heading("Defendant", text="Defendant")
        self.student_table.heading("Address", text="Address")
        self.student_table.heading("Crime", text="Crime")
        self.student_table.heading("Lawyer", text="Lawyer")
        self.student_table.heading("Prosecutor", text="Prosecutor")
        self.student_table.heading("Judge", text="Judge")
        self.student_table.heading("EndDate", text="End Date")
        self.student_table.heading("JudgementSummary", text="Judgement Summary")

        self.student_table["show"] = "headings"
        self.student_table.pack(fill=BOTH, expand=1)

        self.student_table.column("CIN", width=150)
        self.student_table.column("StartDate", width=150)
        self.student_table.column("NextHearing", width=150)
        self.student_table.column("Defendant", width=150)
        self.student_table.column("Address", width=150)
        self.student_table.column("Crime", width=150)
        self.student_table.column("Lawyer", width=150)
        self.student_table.column("Prosecutor", width=150)
        self.student_table.column("Judge", width=150)
        self.student_table.column("EndDate", width=150)
        self.student_table.column("JudgementSummary", width=150)

        self.student_table.pack(fill=BOTH, expand=1)

    def query_pending_cases(self):
        url = "https://bigquery-cloudbuild-f7q24pru5q-ey.a.run.app/bigquery_operation_results"
        headers = {"Content-type": "application/json"}
        _dict = {
            "query": f'''
                            SELECT
                                CIN,
                                start_date,
                                defendant,
                                address,
                                crime,
                                lawyer,
                                prosecutor,
                                judge
                            FROM    
                             `sandbox-381608.jis.cases_inventory`
                            WHERE end_date IS NULL
                            ORDER BY CIN;
                        ''',
            "gbq_table_id": "sandbox-381608.jis.cases_inventory",
        }
        _response = requests.post(url, headers=headers, json=_dict)
        _result = _response.json()
        df = pd.DataFrame.from_records(_result.get("query_results").get("results"))
        df_to_excel(df)
        self.new_window = Toplevel(self.root)
        self.app = DfToTkinterTable(self.new_window)

    def query_case_status(self):
        url = "https://bigquery-cloudbuild-f7q24pru5q-ey.a.run.app/bigquery_operation_results"
        headers = {"Content-type": "application/json"}
        _dict = {
            "query": f'''
                            SELECT
                                CIN,
                                start_date,
                                defendant,
                                address,
                                crime,
                                lawyer,
                                prosecutor,
                                judge,
                                judgement_summary
                            FROM    
                             `sandbox-381608.jis.cases_inventory`
                            WHERE crime LIKE "%{self.var_search.get()}%"
                            OR CIN LIKE "%{self.var_search.get()}%";
                        ''',
            "gbq_table_id": "sandbox-381608.jis.cases_inventory",
        }
        _response = requests.post(url, headers=headers, json=_dict)
        _result = _response.json()
        df = pd.DataFrame.from_records(_result.get("query_results").get("results"))
        df_to_excel(df)
        self.new_window = Toplevel(self.root)
        self.app = DfToTkinterTable(self.new_window)

    def query_resolved_cases(self):
        url = "https://bigquery-cloudbuild-f7q24pru5q-ey.a.run.app/bigquery_operation_results"
        headers = {"Content-type": "application/json"}
        _dict = {
            "query": f'''
                            SELECT
                                start_date,
                                CIN,
                                end_date,
                                judge,
                                judgement_summary
                            FROM    
                             `sandbox-381608.jis.cases_inventory`
                            WHERE end_date IS NOT NULL
                            AND 
                                start_date>="{self.start_date_entry.get_date()}"
                            AND
                                end_date<="{self.end_date_entry.get_date()}"
                            ORDER BY start_date;
                        ''',
            "gbq_table_id": "sandbox-381608.jis.cases_inventory",
        }
        _response = requests.post(url, headers=headers, json=_dict)
        _result = _response.json()
        df = pd.DataFrame.from_records(_result.get("query_results").get("results"))
        df_to_excel(df)
        self.new_window = Toplevel(self.root)
        self.app = DfToTkinterTable(self.new_window)

    def query_cases_on_date(self):
        url = "https://bigquery-cloudbuild-f7q24pru5q-ey.a.run.app/bigquery_operation_results"
        headers = {"Content-type": "application/json"}
        _dict = {
            "query": f'''
                            SELECT
                                start_date,
                                CIN,
                                end_date,
                                judge,
                                judgement_summary
                            FROM    
                             `sandbox-381608.jis.cases_inventory`
                            WHERE end_date IS NULL
                            AND 
                                next_hearing ="{self.date_entry.get_date()}";
                        ''',
            "gbq_table_id": "sandbox-381608.jis.cases_inventory",
        }
        _response = requests.post(url, headers=headers, json=_dict)
        _result = _response.json()
        df = pd.DataFrame.from_records(_result.get("query_results").get("results"))
        df_to_excel(df)
        self.new_window = Toplevel(self.root)
        self.app = DfToTkinterTable(self.new_window)

    # Reset Function
    def reset_data(self):
        self.var_start_date.set("")
        self.var_end_date.set("")
        self.var_date.set("")
        self.var_search.set("Enter keywords to search...")


if __name__ == "__main__":
    root = Tk()
    obj = CaseQueries(root)
    root.mainloop()

from tkinter import ttk
import tkinter as tk
import mysql.connector
from tkinter import messagebox

def connect_db():
    try: 
        return mysql.connector.connect(
            host='141.209.241.81',
            user='grp3w200',
            passwd='passinit',
            database='bis698_S24_Grp3_w200'
        )
    except mysql.connector.Error as e:
        messagebox.showerror("Database Connection Error", str(e))
        return None
def view_appintments():
    conn= connect_db()
    if conn is not None:
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM Appointment")
            rows = cursor.fetchall()
            for row in rows:
                tree.insert("", tk.END, values=row)
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", str(e))
        finally:
            cursor.close()
            conn.close()
def exist_program():
    root.destroy()

root = tk.Tk()
root.title("Admin Dashboard")

frame= tk.Frame(root)
frame.pack()

#Appointment Report Frame

report_frame = tk.LabelFrame(frame, text="Appointment Report", bg="#728780", fg="#FFFFFF")
report_frame.grid(row=0, column=0, sticky="news", padx=20, pady=10)

tree=ttk.Treeview(report_frame, column=("Appointment_ID", "Service_Type", "Appointment_Date", "User_ID", "Admin_ID"), show='headings')
tree.heading("#1", text="Appointment ID")
tree.heading("#2", text="Service Type")
tree.heading("#3", text="Appointment Date")
tree.heading("#4", text="User ID")
tree.heading("#5", text="Admin ID")

#Button frame

button_frame = tk.LabelFrame(frame, text="", bg="#728780")
button_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

btn_display = tk.Button(button_frame, text="Display Appointments",bg="#728780", fg="#FFFFFF", command=view_appintments())
#btn_exit= tk.Button(button_frame, text="Exit", bg="#728780", fg="#FFFFFF", command=exit_program())

btn_display.grid(row=0, column=0, padx=5)
#btn_exit.grid(row=0, column=1, padx=5)

root.mainloop()


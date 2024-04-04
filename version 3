import tkinter as tk
from tkinter import ttk, Frame, Label, Button, messagebox
import mysql.connector
import datetime as dt

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

def view_appointments(tree):
    conn = connect_db()
    if conn is not None:
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM Appointments")
            rows = cursor.fetchall()
            if len(rows) == 0:
                messagebox.showinfo("No Appointments", "No appointments found.")
            else:
                for row in rows:
                    tree.insert("", tk.END, value=row)
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", str(e))
        finally:
            cursor.close()
            conn.close()
    else:
        messagebox.showerror("Database Error", "Failed to connect to the database.")

def exit_program(window):
    window.destroy()

def create_window():
    window = tk.Tk()
    window.title('Admin Report Dashboard')
    window.geometry('350x250')
    window.state('zoomed')
    window.config(bg="#728780")
    return window

def create_heading(window):
    heading = Label(window, text='Report', bg='#728780', font=("", 20, "bold"), fg='white')
    heading.place(x=320, y=70)
    return heading

def create_body_frame(window):
    body_frame = Frame(window, bg = '#FFFFFF')
    body_frame.place(x=328, y=110, width=1200, height=500)
    return body_frame

def create_sidebar(window):
    sidebar = Frame(window, bg="#C2CEBD")
    sidebar.place(x=0, y=0, width=300, height=900)
    return sidebar

def create_date(window):
    date = dt.datetime.now()
    date_label = tk.Label(window, text=f"{date:%A, %B %d, %Y}", font=("Calibri", 17, "bold"), 
                         bg='#728780',fg="#FFFFFF", anchor='c')
    date_label.place(x=1400, y=20) 
    return date_label

def main():
    window = create_window()
    heading = create_heading(window)
    body_frame = create_body_frame(window)
    brand_name = create_brand_name(window)
    sidebar = create_sidebar(window)
    date_show = create_date(window)
    
    # Treeview
    tree = ttk.Treeview(body_frame, columns=("Appointment_ID", "Service_Type", "Appointment_Date", "User_Name", "Admin_Time"), show='headings')
    tree.tag_configure('gray', background='lightgray')
    tree.tag_configure('normal', background='white')
    tree.column("#1", anchor=tk.CENTER)
    tree.heading("#1", text="Appointment ID")
    tree.column("#2", anchor=tk.CENTER)
    tree.heading("#2", text="Service Type")
    tree.column("#3", anchor=tk.CENTER)
    tree.heading("#3", text="Appointment Date")
    tree.column("#4", anchor=tk.CENTER)
    tree.heading("#4", text="User Name")
    tree.column("#5", anchor=tk.CENTER)
    tree.heading("#5", text="Appointment Time")
    tree.grid()

    # Name of the Screen
    screen_name = Label(window, text='Admin Dashboard', bg="#C2CEBD", fg='#FFFFFF',
                       font=("", 17, "bold", "underline"), anchor=tk.CENTER,)
    screen_name.place(x=25, y=70)
    
    # Display Appointments button
    btn_display = tk.Button(window, text="Display Appointments", bg="#728780", fg="#FFFFFF", 
                            font=("Calibri", 15, "bold"), anchor=tk.CENTER,
                            command=lambda: view_appointments(tree))
    btn_display.place(x=50, y=200)

    # Exit button
    btn_exit = tk.Button(window, text='Exit', bg='#728780', fg="#FFFFFF", 
                         font=("Calibri", 15, "bold"), anchor=tk.CENTER,
                         command=lambda: exit_program(window))
    btn_exit.place(x=100, y=300)

    window.mainloop()

if __name__ == "__main__":
    main()

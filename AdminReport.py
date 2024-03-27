from tkinter import *
import mysql.connector
import datetime as dt
from tkinter import messagebox

class Admin_Report:
    def __init__(self, window):
        self.window = window
        self.window.title('Admin Report Dashboard')     #title of the window
        self.window.geometry('350x250')                 #dimension of the window
        self.window.state('zoomed')                     #auto zoomed
        self.window.config(bg="#728780")                #background color
        
        #dashboard header
        self.header = Frame(self.window, bg="#728780") #, bg='#728780') #if I later decide to add color to the header
        self.header.place(x=300, y=0, width=1300, height=50)
        
        #logout button
        self.logout_text = Button(self.window, text='Logout', bg='#C2CEBD', font= (" ", 13, "bold"), 
                                  bd=0, fg='white', cursor='hand2', activebackground='#728780')
        self.logout_text.place(x=1400, y=15)
        
        #dashboard sidebar
        self.sidebar = Frame(self.window, bg="#C2CEBD")
        self.sidebar.place(x=0, y=0, width=300, height=900)

        #dashboard body
        self.heading = Label(self.window, text='Report', bg='#728780', font= (" ", 20, "bold"), 
                             fg='white')
        self.heading.place(x=320, y=70)

        #dashboard body frame
        self.bodyFrame1 = Frame(self.window, bg='#C2CEBD')
        self.bodyFrame1.place(x=328, y=110, width=1200, height=500)

        #Role Specification on the sidebar
        self.brandName = Label(self.sidebar, text='Admin Dashboard', 
                               bg="#C2CEBD",fg='white', font= (" ", 17, "bold","underline"))
        self.brandName.place(x=25, y=20)

        

    def connect_db(self):
        try:
            conn = mysql.connector.connect(
                host='141.209.241.81',
                user='grp3w200',
                passwd='passinit',
                database='bis698_S24_Grp3_w200')
                
            mycursor = conn.cursor()
            mycursor.execute("SELECT * FROM Appointments")

            #get the results
            result = mycursor.fetchall()

            #close the cursor and the connection
            mycursor.close()
            conn.close()
            
        except mysql.connector.Error as e:
                messagebox.showerror("Database Connection Error", str(e))
                return None


def win():
    window = Tk()
    Admin_Report(window)
    window.mainloop()


if __name__ == '__main__':
    win()

from tkinter import *
import pymysql
import tkinter.messagebox
from tkinter import messagebox

def connection():
    con = pymysql.connect(host="localhost", user="root", password="", database="student_python")
    cur = con.cursor()
    con.commit()
    con.close()

# con = pymysql.connect(host="localhost", user="root", password="", database="student_python")
# cur = con.cursor()
# con.commit()
# con.close()


# ================Function To Add To Database Using Sql===============================
def db_add_student(self):
    if self.rollNoVar.get() == "" or self.nameVar.get() == "" or self.emailVar.get() == "" or self.genderVar.get() == "" or self.contactVar.get() == "" or self.dobVar.get() == "":
        messagebox.showerror("Error", "All Fields are required!!!")
    else:
        con = pymysql.connect(host="localhost", user="root", password="", database="student_python")
        cur = con.cursor()
        cur.execute("insert into students values (%s,%s,%s,%s,%s,%s,%s,%s)", (self.rollNoVar.get(),
                                                                              self.nameVar.get(),
                                                                              self.emailVar.get(),
                                                                              self.genderVar.get(),
                                                                              self.contactVar.get(),
                                                                              self.dobVar.get(),
                                                                              self.regDateVar.get(),
                                                                              self.txtAddress.get('1.0', END)))
    con.commit()
    self.fetch_data()
    self.clear()
    con.close()
    messagebox.showinfo("success", "your information has been added successful")


# ====================== Show data to Table===============================
def db_fetch_data(self):
    con = pymysql.connect(host="localhost", user="root", password="", database="student_python")
    cur = con.cursor()

    cur.execute("select * from students")
    rows = cur.fetchall()
    if len(rows) != 0:
        self.studentTable.delete(*self.studentTable.get_children())
        for row in rows:
            self.studentTable.insert('', END, values=row)

    con.commit()
    con.close()


# ==================== get particular data using cursor pointing at it=======================
def db_get_cursor(self, ev):
    cursor_row = self.studentTable.focus()
    contents = self.studentTable.item(cursor_row)
    row = contents['values']
    self.rollNoVar.set(row[0])
    self.nameVar.set(row[1])
    self.emailVar.set(row[2])
    self.genderVar.set(row[3])
    self.contactVar.set(row[4])
    self.dobVar.set(row[5])
    self.regDateVar.set(row[6])
    self.txtAddress.delete("1.0", END)
    self.txtAddress.insert(END, row[7])


# =================== update data===================================================
def db_update_data(self):
    if self.rollNoVar.get() == "" or self.nameVar.get() == "" or self.emailVar.get() == "" or self.genderVar.get() == "" or self.contactVar.get() == "" or self.dobVar.get() == "":
        messagebox.showerror("Error", "All Fields are required!!!")
    else:
        con = pymysql.connect(host="localhost", user="root", password="", database="student_python")
        cur = con.cursor()
        cur.execute(
            "update students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,reg_date=%s,address=%s where roll_no=%s",
            (
                self.nameVar.get(),
                self.emailVar.get(),
                self.genderVar.get(),
                self.contactVar.get(),
                self.dobVar.get(),
                self.regDateVar.get(),
                self.txtAddress.get('1.0', END),
                self.rollNoVar.get()
            ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
        messagebox.showinfo("success", "your information has been updated successful")


# =======================delete particular data============================
def db_delete_data(self):
    delete_student = tkinter.messagebox.askyesno("Student management system", "confirm if you want to Delete ")
    if delete_student > 0:
        con = pymysql.connect(host="localhost", user="root", password="", database="student_python")
        cur = con.cursor()
        cur.execute("delete  from students where  roll_no=%s", self.rollNoVar.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()
    return


# ======================= search data ==========================================
def db_search_data(self):
    con = pymysql.connect(host="localhost", user="root", password="", database="student_python")
    cur = con.cursor()

    cur.execute(
        "select * from students where " + str(self.searchBy.get()) + " LIKE '%" + str(self.searchTxt.get()) + "%'")
    rows = cur.fetchall()
    if len(rows) != 0:
        self.studentTable.delete(*self.studentTable.get_children())
        for row in rows:
            self.studentTable.insert('', END, values=row)

    con.commit()
    con.close()

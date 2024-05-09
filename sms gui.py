import tkinter as tk

class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, name, rollno, department, major):
        self.students[rollno] = [name, department, major]

    def view_student(self, rollno):
        if rollno in self.students:
            return self.students[rollno]
        else:
            return None

    def update_student(self, rollno, name, department, major):
        if rollno in self.students:
            self.students[rollno] = [name, department, major]
            return True
        else:
            return False

    def delete_student(self, rollno):
        if rollno in self.students:
            del self.students[rollno]
            return True
        else:
            return False

# GUI setup
class StudentManagementGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Student Management System")

        self.sms = StudentManagementSystem()

        self.label = tk.Label(master, text="Student Management System")
        self.label.pack()

        self.frame = tk.Frame(master)
        self.frame.pack()

        self.menu_label = tk.Label(self.frame, text="Select an option:")
        self.menu_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.add_button = tk.Button(self.frame, text="Add Student", command=self.add_student)
        self.add_button.grid(row=1, column=0, padx=10)

        self.view_button = tk.Button(self.frame, text="View Student", command=self.view_student)
        self.view_button.grid(row=1, column=1, padx=10)

        self.update_button = tk.Button(self.frame, text="Update Student", command=self.update_student)
        self.update_button.grid(row=2, column=0, padx=10)

        self.delete_button = tk.Button(self.frame, text="Delete Student", command=self.delete_student)
        self.delete_button.grid(row=2, column=1, padx=10)

        self.exit_button = tk.Button(self.frame, text="Exit", command=self.master.quit)
        self.exit_button.grid(row=3, column=0, columnspan=2, pady=10)

    def add_student(self):
        add_window = tk.Toplevel(self.master)
        add_window.title("Add Student")

        tk.Label(add_window, text="Name:").grid(row=0, column=0)
        tk.Label(add_window, text="Roll No:").grid(row=1, column=0)
        tk.Label(add_window, text="Department:").grid(row=2, column=0)
        tk.Label(add_window, text="Major:").grid(row=3, column=0)

        name_entry = tk.Entry(add_window)
        rollno_entry = tk.Entry(add_window)
        department_entry = tk.Entry(add_window)
        major_entry = tk.Entry(add_window)

        name_entry.grid(row=0, column=1)
        rollno_entry.grid(row=1, column=1)
        department_entry.grid(row=2, column=1)
        major_entry.grid(row=3, column=1)

        def add():
            name = name_entry.get()
            rollno = int(rollno_entry.get())
            department = department_entry.get()
            major = major_entry.get()
            self.sms.add_student(name, rollno, department, major)
            add_window.destroy()

        tk.Button(add_window, text="Add", command=add).grid(row=4, columnspan=2, pady=10)

    def view_student(self):
        view_window = tk.Toplevel(self.master)
        view_window.title("View Student")

        tk.Label(view_window, text="Roll No:").grid(row=0, column=0)
        rollno_entry = tk.Entry(view_window)
        rollno_entry.grid(row=0, column=1)

        def view():
            rollno = int(rollno_entry.get())
            student = self.sms.view_student(rollno)
            if student:
                tk.Label(view_window, text=f"Name: {student[0]}").grid(row=1, column=0)
                tk.Label(view_window, text=f"Roll No: {rollno}").grid(row=2, column=0)
                tk.Label(view_window, text=f"Department: {student[1]}").grid(row=3, column=0)
                tk.Label(view_window, text=f"Major: {student[2]}").grid(row=4, column=0)
            else:
                tk.Label(view_window, text="Student not found!").grid(row=1, column=0)

        tk.Button(view_window, text="View", command=view).grid(row=0, column=2)

    def update_student(self):
        update_window = tk.Toplevel(self.master)
        update_window.title("Update Student")

        tk.Label(update_window, text="Roll No:").grid(row=0, column=0)
        rollno_entry = tk.Entry(update_window)
        rollno_entry.grid(row=0, column=1)

        tk.Label(update_window, text="New Name:").grid(row=1, column=0)
        new_name_entry = tk.Entry(update_window)
        new_name_entry.grid(row=1, column=1)

        tk.Label(update_window, text="New Department:").grid(row=2, column=0)
        new_department_entry = tk.Entry(update_window)
        new_department_entry.grid(row=2, column=1)

        tk.Label(update_window, text="New Major:").grid(row=3, column=0)
        new_major_entry = tk.Entry(update_window)
        new_major_entry.grid(row=3, column=1)

        def update():
            rollno = int(rollno_entry.get())
            new_name = new_name_entry.get()
            new_department = new_department_entry.get()
            new_major = new_major_entry.get()
            success = self.sms.update_student(rollno, new_name, new_department, new_major)
            if success:
                tk.Label(update_window, text="Student details updated successfully!").grid(row=4, columnspan=2)
            else:
                tk.Label(update_window, text="Student not found!").grid(row=4, columnspan=2)

        tk.Button(update_window, text="Update", command=update).grid(row=5, columnspan=2, pady=10)

    def delete_student(self):
        delete_window = tk.Toplevel(self.master)
        delete_window.title("Delete Student")

        tk.Label(delete_window, text="Roll No:").grid(row=0, column=0)
        rollno_entry = tk.Entry(delete_window)
        rollno_entry.grid(row=0, column=1)

        def delete():
            rollno = int(rollno_entry.get())
            success = self.sms.delete_student(rollno)
            if success:
                tk.Label(delete_window, text="Student deleted successfully!").grid(row=1, columnspan=2)
            else:
                tk.Label(delete_window, text="Student not found!").grid(row=1, columnspan=2)

def main():
    root = tk.Tk()
    app = StudentManagementGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
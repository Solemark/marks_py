from tkinter import Tk, StringVar, IntVar, Label, Entry, Button
from Mark import Mark


class MarksGUI:
    def __init__(self) -> None:
        master: Tk = Tk()
        """@param TK - GUI window container"""
        self.__student_name: StringVar = StringVar()
        """@param StringVar - student name"""
        self.__student_mark: IntVar = IntVar()
        """@param IntVar - student mark"""
        self.__output: StringVar = StringVar()
        """@param StringVar - output"""
        self.__students: list[Mark] = []
        """@param list[Mark] - students"""

        master.title("Mark Entry System 3.0")
        Label(master, text="Enter the students details").grid(row=0, columnspan=2)
        Label(master, text="Name:").grid(row=1, column=0)
        Entry(master, textvariable=self.__student_name).grid(row=1, column=1)
        Label(master, text="Mark:").grid(row=2, column=0)
        Entry(master, textvariable=self.__student_mark).grid(row=2, column=1)
        Button(master, text="submit", command=self.__submit).grid(row=3, column=0)
        Button(master, text="display", command=self.__display).grid(row=3, column=1)
        Button(master, text="search", command=self.__search).grid(row=4, column=0)
        Button(master, text="exit", command=self.__exit).grid(row=4, column=1)
        Label(master, textvariable=self.__output).grid(row=5, columnspan=2)

        master.mainloop()

    def __submit(self) -> None:
        """Get and save the input student details"""
        mark: Mark = Mark(self.__student_name.get(), self.__student_mark.get())
        self.__students.append(mark)
        self.__clear()
        self.__output.set(f"Added Student {mark.__str__()}")

    def __display(self) -> None:
        """Display all students"""
        self.__clear()
        self.__output.set("\n".join(student.__str__() for student in self.__students))

    def __search(self) -> None:
        """Search for student record using name"""
        self.__output.set(
            "".join(
                student.__str__()
                for student in self.__students
                if student.get_student_name() == self.__student_name.get()
            )
        )

    def __exit(self) -> None:
        """Close the application"""
        exit(0)

    def __clear(self) -> None:
        """Reset the GUI"""
        self.__student_name.set("")
        self.__student_mark.set(0)
        self.__output.set("")


if __name__ == "__main__":
    MarksGUI()

from Mark import Mark


class MarksCLI:
    __students: list[Mark]
    __INSTR: list[str] = [
        "1 to add new student",
        "2 to search existing booking",
        "3 to list all bookings",
        "Enter any other key to quit",
    ]

    def __init__(self) -> None:
        self.__students = []
        print("Mark Entry System 3.0")
        self.__cli()

    def __cli(self) -> None:
        """run the CLI component recursively"""
        CMD: int = int(input(f"{self.__linebreak()}\n{', '.join(self.__INSTR)}"))
        match CMD:
            case 1:
                self.__students = [*self.__students, self.__new()]
            case 2:
                print(self.__search())
            case 3:
                print(self.__students)
            case _:
                exit(0)
        self.__cli()

    def __linebreak(self) -> str:
        """Function that creates a string linebreak"""
        return "__________"

    def __new(self) -> Mark:
        """Create and return a new Student"""
        print("Enter student details")
        return Mark(input("Name: "), int(input("Mark: ")))

    def __search(self) -> Mark | str:
        """Finds the Student from the student list"""
        out: Mark | str
        inp: str = input("Enter student name to search:")
        for student in self.__students:
            if inp == student.get_student_name():
                out = student
                break
        return out


if __name__ == "__main__":
    MarksCLI()

from src.mark import Mark


class MarksCLI:
    def __init__(self) -> None:
        self.__students: list[Mark] = []
        """list[Mark] - students"""
        self.__INSTR: str = (
            "1 to add new student\n"
            "2 to search existing booking\n"
            "3 to list all bookings\n"
            "Enter any other key to quit\n"
        )
        """str - instructions"""

        print("Mark Entry System 3.0")
        self.__cli()

    def __cli(self) -> None:
        """run the CLI component recursively"""
        while True:
            match input(f"{self.__linebreak()}\n{self.__INSTR}"):
                case "1":
                    self.__students = [*self.__students, self.__new()]
                case "2":
                    print(self.__search().__str__())
                case "3":
                    print(self.__list())
                case _:
                    exit(0)

    def __linebreak(self) -> str:
        """Function that creates a string linebreak"""
        return "__________"

    def __new(self) -> Mark:
        """Create and return a new Student"""
        print("Enter student details")
        return Mark(input("Name: "), int(input("Mark: ")))

    def __search(self) -> Mark | None:
        """Finds the Student from the student list"""
        out: Mark | None = None
        inp: str = input("Enter student name to search:")
        for student in self.__students:
            if inp == student.get_student_name():
                out = student
                break
        return out

    def __list(self) -> str:
        out: str = ""
        for student in self.__students:
            out += f"{student.__str__()}\n"
        return out

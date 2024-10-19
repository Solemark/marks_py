class Mark:
    def __init__(self, student_name: str = "", student_mark: int = 0) -> None:
        self.__student_name = student_name
        """@param str - student name"""
        self.__student_mark = student_mark
        """@param int - student mark"""

    def set_student_name(self, student_name: str) -> None:
        self.__student_name = student_name

    def get_student_name(self) -> str:
        return self.__student_name

    def set_student_mark(self, student_mark: int) -> None:
        self.__student_mark = student_mark

    def get_student_mark(self) -> int:
        return self.__student_mark

    def get_grade(self) -> str:
        if self.__student_mark < 50:
            return "F"
        elif self.__student_mark < 65:
            return "P"
        elif self.__student_mark < 75:
            return "C"
        elif self.__student_mark < 85:
            return "D"
        else:
            return "HD"

    def __str__(self) -> str:
        return f"{self.__student_name}, {self.__student_mark}, {self.get_grade()}"

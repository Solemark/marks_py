from pytest import fixture
from src.mark import Mark


@fixture
def mark() -> Mark:
    return Mark("Obi-Wan Kenobi", 98)


def test_get_mark(mark: Mark) -> None:
    assert "Obi-Wan Kenobi" == mark.get_student_name()
    assert 98 == mark.get_student_mark()
    assert "HD" == mark.get_grade()
    assert "Obi-Wan Kenobi, 98, HD" == mark.__str__()


def test_set_mark(mark: Mark) -> None:
    assert "Obi-Wan Kenobi" == mark.get_student_name()
    assert 98 == mark.get_student_mark()
    assert "HD" == mark.get_grade()
    assert "Obi-Wan Kenobi, 98, HD" == mark.__str__()

    mark.set_student_name("Anakin Skywalker")
    mark.set_student_mark(0)

    assert "Anakin Skywalker" == mark.get_student_name()
    assert 0 == mark.get_student_mark()
    assert "F" == mark.get_grade()
    assert "Anakin Skywalker, 0, F" == mark.__str__()

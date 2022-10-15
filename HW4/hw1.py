"""
Create classes to track homeworks.

1. Homework - accepts howework text and deadline (datetime.timedelta)
Homework has a method, that tells if deadline has passed.

2. Student - can solve homework with `do_homework` method.
Raises DeadlineError with "You are late" message if deadline has passed

3. Teacher - can create homework with `create_homework`; check homework with `check_homework`.
Any teacher can create or check any homework (even if it was created by one of colleagues).

Homework are cached in dict-like structure named `homework_done`. Key is homework, values are
solutions. Each student can only have one homework solution.

Teacher can `reset_results` - with argument it will reset results for specific homework, without - 
it clears the cache.

Homework is solved if solution has more than 5 symbols.

-------------------
Check file with tests to see how all these classes are used. You can create any additional classes 
you want.
"""

from dataclasses import dataclass
from datetime import timedelta


class Homework:
    def __init__(self, homework_text: str, deadline: int, homework_solution=None, author=None):
        self.homework_text = homework_text
        self.deadline = deadline
        self.homework_solution = homework_solution
        self.author = author

    @classmethod
    def is_deadline_passed(cls, deadline_to_check: int) -> bool:
        return timedelta(deadline_to_check) < timedelta(0)


@dataclass
class Teacher:
    lname: str
    fname: str
    homework_done = {}

    @classmethod
    def create_homework(cls, homework_text: str, deadline: int) -> Homework:
        return Homework(homework_text, deadline)

    @classmethod
    def check_homework(cls, homework_to_check: Homework) -> bool:
        if len(homework_to_check.homework_solution) > 5:
            cls.homework_done[homework_to_check] = [homework_to_check]
            return True
        else:
            cls.homework_done[homework_to_check] = [None]
            return False

    @classmethod
    def reset_results(cls, *args):
        if len(args) > 0:
            cls.homework_done.pop(args[0])
        else:
            cls.homework_done.clear()


@dataclass
class Student:
    lname: str
    fname: str

    def do_homework(self, homework: Homework, solution: str) -> Homework:
        if homework.is_deadline_passed(homework.deadline):
            raise DeadlineError("You are late")
        else:
            homework.author = self
            homework.homework_solution = solution
            return homework


class DeadlineError(Exception):
    """Being thrown if a deadline for a homework has passed"""
    def __init__(self, message):
        super().__init__(message)

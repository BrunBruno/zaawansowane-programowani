from zadania_5.classes.Employee import Employee
from zadania_5.classes.Student import Student

class Order:
    def __init__(self, employee:Employee, student:Student, books:list, order_date:str) -> None:
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self) -> str:
        books_str = "\n".join(f"    - {str(book)}" for book in self.books)
        return (
            f"Order:\n"
            f"  {self.employee}\n"
            f"  {self.student}\n"
            f"  Books:\n{books_str}\n"
            f"  Order date: {self.order_date}"
        )
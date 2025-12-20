from classes.Library import Library
from classes.Student import Student
from classes.Order import Order
from classes.Book import Book
from classes.Employee import Employee



lib1 = Library(
    city='Katowice',
    street='Gliwicka',
    zip_code='40-000',
    open_hours='8-16',
    phone="123 123 123"
)
lib2 = Library(
    city='Gliwice',
    street='Katowicka',
    zip_code='50-000',
    open_hours='8-21',
    phone="321 321 321"
)

book1 = Book(
    library=lib1,
    publication_date='2009-09-01',
    author_name='Zdich',
    author_surname='Zadyszka',
    number_of_pages=100,
)
book2 = Book(
    library=lib1,
    publication_date='2012-12-31',
    author_name='Mirek',
    author_surname='Morszczuk',
    number_of_pages=50,
)
book3 = Book(
    library=lib1,
    publication_date='2016-01-30',
    author_name='Kornel',
    author_surname='Kotwica',
    number_of_pages=400,
)
book4 = Book(
    library=lib2,
    publication_date='2013-01-24',
    author_name='Kamila',
    author_surname='Komorowska',
    number_of_pages=150,
)
book5 = Book(
    library=lib2,
    publication_date='2018-05-05',
    author_name='Joanna',
    author_surname='Janicka',
    number_of_pages=80,
)

employee1 = Employee(
    first_name='Jan',
    last_name='Ciasto',
    hire_date='2008-09-01',
    birth_date='1980-01-01',
    city='Kowice',
    street='Ulicowa',
    zip_code='40-000',
    phone='963 963 963'
)
employee2 = Employee(
    first_name='Kamil',
    last_name='Ślimak',
    hire_date='2001-08-01',
    birth_date='1977-06-01',
    city='Mysłowice',
    street='Mickiweicza',
    zip_code='41-000',
    phone='147 147 147'
)
employee3 = Employee(
    first_name='Edmunt',
    last_name='Mazowiecki',
    hire_date='2024-08-08',
    birth_date='1999-09-09',
    city='Jaworzno',
    street='Drogowa',
    zip_code='60-000',
    phone='123 456 789'
)

student1 = Student(
    name='Krzyś',
    marks=[]
)
student2 = Student(
    name='Asia',
    marks=[]
)
student3 = Student(
    name='Basia',
    marks=[]
)

order1 = Order(
    employee=employee1,
    student=student1,
    books=[book1, book2, book3],
    order_date='2025-11-30'
)
order2 = Order(
    employee=employee2,
    student=student2,
    books=[book3, book4],
    order_date='2025-11-30'
)

print(order1)
print(order2)
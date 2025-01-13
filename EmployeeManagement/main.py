class Employee:

    def __init__(self, name, e_id, dept, salary):
        self.name = name
        self.eid = e_id
        self.dept = dept
        self.salary = salary

    def display_info(self):
        print(f'Name: {self.name}\n'
              f'Employee ID: {self.eid}\n'
              f'Department: {self.dept}\n'
              f'Salary: {self.salary}\n\n')


emp1 = Employee('Aryan', 123, 'CSE', 250000)
emp2 = Employee('xyz', 321, 'Mechanical', 1200)
emp1.display_info()
emp2.display_info()
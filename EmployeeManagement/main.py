class Employee:

    def __init__(self, e_name, e_id, dept, salary=0):
        self.name = e_name
        self.eid = e_id
        self.dept = dept
        self.salary = salary

    def display_info(self):
        print(f'Name: {self.name}\n'
              f'Employee ID: {self.eid}\n'
              f'Department: {self.dept}\n'
              f'Salary: {self.salary}\n\n')

    def update_details(self, name=None, dept=None, salary=None):
        if name:
            self.name = name
        if dept:
            self.dept = dept
        if salary:
            self.salary = salary

    def increment_salary(self, per):
        self.salary += round(self.salary * (per/100))


emp1 = Employee('Aryan', 2415800020, 'CSE', 250000)
emp1.display_info()
emp1.increment_salary(20)
emp1.display_info()
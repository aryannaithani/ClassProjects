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


class EmployeeManagement:

    def __init__(self):
        self.employees = []
        self.eid = 1

    def add_employee(self, name, dept, salary):
        new = {self.eid : [name, dept, salary]}
        self.employees.append(new)
        self.eid += 1


    def remove_employee(self, eid):
        self.employees.pop(eid-1)

    def show(self):
        for i in self.employees:
            print(i)



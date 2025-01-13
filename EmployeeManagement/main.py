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

    def update_details(self, name=None, dept=None, salary=None):
        self.name = name
        self.dept = dept
        self.salary = salary


emp1 = Employee('Aryan', 123, 'CSE', 250000)
emp1.display_info()
emp1.update_details('Naithani', 'BioTech', 40000)
emp1.display_info()
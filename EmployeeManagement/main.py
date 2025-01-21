employees = []

class EmployeeManagement:

    def __init__(self):
        self.eid = 1

    def add_employee(self, name, dept, salary):
        new = {self.eid : [name, dept, salary]}
        employees.append(new)

    def remove_employee(self, eid):
        employees.pop(eid-1)

    def show(self):
        for i in employees:
            print(i)

    def increment(self, eid, per):
        employees[eid-1][eid][2] += round(employees[eid-1][eid][2] * (per/100))


class Employee:

    def show_details(self, eid):
        print(employees[eid-1])

    def update_details(self, eid, name=None, dept=None):
        if name:
            employees[eid-1][eid][0] = name
        if dept:
            employees[eid - 1][eid][1] = dept


obj2 = EmployeeManagement()
obj1 = Employee()
print('----------EMPLOYEE MANAGEMENT SYSTEM----------')
while True:
    cmd = int(input('Enter 1 for Employee Menu\n'
                    'Enter 2 for Administrator Menu\n'))
    if cmd == 1:
        ecmd = int(input('Enter 1 to show details\n'
                         'Enter 2 to update details\n'))
        if ecmd == 1:
            x = int(input('Enter Your Employee ID: '))
            obj1.show_details(x)
            print('\n')
        elif ecmd == 2:
            x = int(input('Enter Your Employee ID: '))
            nname = input('Enter new name(leave blank if not needed): ')
            ndept = input('Enter new department(leave blank if not needed): ')
            obj1.update_details(eid=x, name=nname, dept=ndept)
            print('Details Updated Successfully\n\n')
            obj1.show_details(x)
            print('\n')
    elif cmd == 2:
        acmd = int(input('Enter 1 to add employee\n'
                         'Enter 2 to remove employee\n'
                         'Enter 3 to increment salaries\n'
                         'Enter 4 to show all employees\n'))
        if acmd == 1:
            name = input('Enter new employee name: ')
            dept = input(f'Enter {name}\'s department: ')
            salary = int(input(f'Enter {name}\'s salary: '))
            obj2.add_employee(name, dept, salary)
            print(f'{name} added as new Employee\n\n')
        elif acmd == 2:
            x = int(input('Enter employee ID to be removed: '))
            obj2.remove_employee(x)
            print('Employee Removed\n\n')
        elif acmd == 3:
            x = int(input('Enter employee ID for salary increment: '))
            y = int(input('Enter Increment percentage: '))
            obj2.increment(x, y)
            print('Salary Incremented\n\n')
        elif acmd == 4:
            obj2.show()
            print('\n')
    else:
        break
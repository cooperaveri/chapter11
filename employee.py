class employee:
    def __init__(self, name, employee_number):
        # constructor initializes the attributes
        self.name = name
        self.employee_number = employee_number

    def get_name(self):
        # accessor method to retrieve the employee name
        return self.name

    def set_name(self, name):
        # mutator method to set the employee name
        self.name = name

    def get_employee_number(self):
        # accessor method to retrieve the employees number
        return self.employee_number

    def set_employee_number(self, employee_number):
        # mutator method to set the employees number
        self.employee_number = employee_number


class productionworker(employee):
    def __init__(self, name, employee_number, shift, hourly_pay_rate):
        # constructor of the subclass calls the constructor of the superclass
        super().__init__(name, employee_number)
        # additional attributes specific to productionworker
        self.shift = shift
        self.hourly_pay_rate = hourly_pay_rate

    def get_shift(self):
        # accessor method to retrieve the shift
        return self.shift

    def set_shift(self, shift):
        # mutator method to set the shift
        self.shift = shift

    def get_hourly_pay_rate(self):
        # accessor method to retrieve the hourly pay rate
        return self.hourly_pay_rate

    def set_hourly_pay_rate(self, hourly_pay_rate):
        # mutator method to set the hourly pay rate
        self.hourly_pay_rate = hourly_pay_rate


def main():
    # prompt user for data
    name = input("Enter employee name: ")
    employee_number = input("Enter employee number: ")
    shift = int(input("Enter shift number (1 for day, 2 for night): "))
    hourly_pay_rate = float(input("Enter hourly pay rate: "))

    # create productionworker object
    worker = productionworker(name, employee_number, shift, hourly_pay_rate)

    # display the entered data using accessor methods
    print("\nEmployee Information:")
    print("Name:", worker.get_name())
    print("Employee Number:", worker.get_employee_number())
    print("Shift:", "Day" if worker.get_shift() == 1 else "Night")
    print("Hourly Pay Rate: $", worker.get_hourly_pay_rate())


if __name__ == "__main__":
    main()
 
Hierchy Chart:
                        Employee
                       |
            --------------------
           |                    |
 ProductionWorker     (Inherits from Employee)
           |
    -----------------
   |                 |
 (Attributes and     |
 Methods from       (Additional attributes
 Employee class)     and methods specific
                     to ProductionWorker)

    
    
2.
    
    
# employee class definition
class employee:
    def __init__(self, name, employee_number):
        # constructor initializes the attributes
        self.name = name
        self.employee_number = employee_number

    def get_name(self):
        # accessor method to retrieve the employee name
        return self.name

    def set_name(self, name):
        # mutator method to set the employee name
        self.name = name

    def get_employee_number(self):
        # accessor method to retrieve the employee number
        return self.employee_number

    def set_employee_number(self, employee_number):
        # mutator method to set the employee number
        self.employee_number = employee_number


# shiftsupervisor class definition, subclass of employee
class shiftsupervisor(employee):
    def __init__(self, name, employee_number, annual_salary, annual_production_bonus):
        # constructor of the subclass calls the constructor of the superclass
        super().__init__(name, employee_number)
        # additional attributes specific to shiftsupervisor
        self.annual_salary = annual_salary
        self.annual_production_bonus = annual_production_bonus

    def get_annual_salary(self):
        # accessor method to retrieve the annual salary
        return self.annual_salary

    def set_annual_salary(self, annual_salary):
        # mutator method to set the annual salary
        self.annual_salary = annual_salary

    def get_annual_production_bonus(self):
        # accessor method to retrieve the annual production bonus
        return self.annual_production_bonus

    def set_annual_production_bonus(self, annual_production_bonus):
        # mutator method to set the annual production bonus
        self.annual_production_bonus = annual_production_bonus


# main function
def main():
    # create shiftsupervisor object
    supervisor = shiftsupervisor("averi", "123", 50000, 2000)

    # display information using accessor methods
    print("\nshift supervisor information:")
    print("name:", supervisor.get_name())
    print("employee number:", supervisor.get_employee_number())
    print("annual salary: $", supervisor.get_annual_salary())
    print("annual production bonus: $", supervisor.get_annual_production_bonus())


# program entry point
if __name__ == "__main__":
    main()

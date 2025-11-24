# Inheritance
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_info(self):
        return f"Name: {self.name}, Salary: {self.salary}"

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)  # Inherit name & salary setup
        self.department = department

    def get_info(self):
        return f"Name: {self.name}, Salary: {self.salary}, Department: {self.department}"

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def get_info(self):
        return f"Name: {self.name}, Salary: {self.salary}, Language: {self.programming_language}"

emp1 = Manager("Alice", 70000, "HR")
emp2 = Developer("Bob", 60000, "Python")

print(emp1.get_info())
print(emp2.get_info())

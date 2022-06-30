from pyaml import yaml
from typing import List
class Employee(object):

    def __init__(self,eno:int,ename:str,esal:float,eaddr:str):
        self.eno =eno
        self.ename =ename
        self.esal =esal
        self.eaddr =eaddr

    def __str__(self):
        return self.name

    def display(self):
        print(f"Employeee No is {self.eno}")
        print(f"Employeee Name is {self.ename}")
        print(f"EmployeeeSalary is {self.esal}")
        print(f"Employee Address is {self.eaddr}")

emp1:Employee = Employee(eno=101,ename="Abi",esal=50000.0,eaddr="bangalore")
emp2:Employee = Employee(eno=102,ename="Rika",esal=60000.0,eaddr="bangalore")

emp_list:List[Employee] = [emp1,emp2]

with open("emp.yml","w") as f:
    for emp in emp_list:
        yaml.dump(emp, f,sort_keys=False)


with open("emp.yml","r") as f:
        try:
            data=f'"{f.read()}"'
            emp=yaml.safe_load(data)
            print(emp)
        except:
            print("completed")

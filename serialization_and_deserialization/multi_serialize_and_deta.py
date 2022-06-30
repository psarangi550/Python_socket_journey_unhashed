import pickle #importing the pickle module
import random

# names=["pratik","rika","abi","papali","naju","pupuli","puja"]

# address=["Bangalore","Hyderabad","Bhubaneswar","Mumbai","Pune","Dehli"]

# emp_obj_list=[]

class Employee(object):

    def __init__(self,no:int,name:str,esal:float,eaddr:str)->None:

        self.no = no
        self.name = name
        self.esal = esal
        self.eaddr =eaddr
    
    def __str__(self)->str:
        return self.name

    def display(self)->None:
        print(f"Emp No is {self.no}")
        print(f"Emp Name is {self.name}")
        print(f"Emp Esal is {self.esal}")
        print(f"Emp address is {self.eaddr}")

# for i in range(10):
#     emp:Employee = Employee(
#                             no=random.randint(100, 1000),
#                             name=random.choice(names),
#                             esal=random.randint(10000, 50000),
#                             eaddr=random.choice(address)
#                             )
#     emp_obj_list.append(emp)

# with open("Employee.ser","wb") as f:
#     for emp in emp_obj_list:
#         pickle.dump(emp,f)

with open("Employee.ser","rb") as f:
    while True:
        try:
            e1=pickle.load(f)
            e1.display()
        except EOFError as e:
            print("Done")
            break




        

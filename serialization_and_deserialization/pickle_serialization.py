import pickle #importing the pickle module

# emp={
#     "eno":101,
#     "ename":"pratik",
#     "esal":5000,
#     "eaddr":"Bangalore"
# }

#convering an Employee class to the file object using the pickle module as below 

class Employee(object):

    def __init__(self,no:int,name:str,esal:float,eaddr:str)->None:

        self.no = no
        self.name = name
        self.esal = esal
        self.eaddr =eaddr
    
    def __str__(self)->str:
        return self.name

    def display(self)->None:
        print(f"Emp No is{self.no}")
        print(f"Emp Name is{self.name}")
        print(f"Emp Esal is{self.esal}")
        print(f"Emp address is{self.address}")

# emp:Employee=Employee(no=102,name="Abi",esal=50000,eaddr="Bangalore")

#the dump() will conver the python object into byte type steam and write that to the file 
#saving the Employee object into the file object as str then 
# with open("emp.ser","wb") as f:
#     pickle.dump(emp,f)

#here the dumps() will convert the python object to byte type string 
# obj_str=pickle.dumps(emp)
# print(obj_str)


#the dump() will conver the python object into byte type steam and write that to the file 
#saving the python object into a file using the pickle module 
# with open("abc.ser","wb") as f:
#     pickle.dump(emp,f)

#here the dumps() will convert the python object to byte type string 
# obj_str=pickle.dumps(emp)
# print(obj_str)

#deserailizing using the load() function and loads()

# obj_byte_strem_str=b'\x80\x03}q\x00(X\x03\x00\x00\x00enoq\x01KeX\x05\x00\x00\x00enameq\x02X\x06\x00\x00\x00pratikq\x03X\x04\x00\x00\x00esalq\x04M\x88\x13X\x05\x00\x00\x00eaddrq\x05X\t\x00\x00\x00Bangaloreq\x06u.'

#converting the byte strem string to the python object using the loads() as 
# py_dict=pickle.loads(obj_byte_strem_str)

# print(py_dict)


#loading it from the file using the load() on the pickle module as below 
#here it will first convert the file type to byte stream data  from there it will be converted into the 
# python object 

with open("emp.ser","rb") as f:
    emp_obj=pickle.load(f)
    print(emp_obj.name)
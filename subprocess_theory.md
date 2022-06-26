#### **<u>PRIOR TO SUBPROCESS MODULE</u>**

```

os.system():-
-----------------------
#return the exit code of the command once running successfully
#any other exit code apart from 0 which been meant for the success
#in windows ypu will get the output as the result 

os.popen():-
----------------------
#this will open a pipe to execute the command which is the subprocess 
# return a file object in return which being open
#we can read the file object returned by using the read()

os.popen().read() #this will read the file object 
# close() will return None if the execution is successful 
# close() will return the subprocess return value if there is an error 

os.spawnl():-
---------------------
#it takes the mode as the first args which can be P_NOWAIT and P_WAIT 

#P_NOWAIT mode will not wait for the command execution to be completed 
# it will simply return the process id

#P_WAIT wait for the process exit code
# if we want to kill the process then it will return the process code of the kill which we enforced

ex:-os.spawnl(os.P_NOWAIT,<command line path>,<command>)
ex:-os.spawnl(os.P_WAIT,<command line path>,<command>)

command line path:-
-----------------------
#for unix it is :-/usr/sh
#for windows :-system32/cmd.exe

```

### **<u>AFTER SUBPROCESS MODULE</u>**

**subprocess module has below API after 3.5v python**

```

- run() method
#return a CompleteProcess class object with args provided and return           # code which represents the exit code
# for the run() will take string if shell=True
#risky as user can provide subprocess.run('<command1>:<command2>')
#which will execute the additional command along with out command 
#for shell=False(default) we need to provide it as list as                      ['<command>','<args>']

- Popen class

# run() on background uses the Popen class to execute the sub process
# os.popen() also uses the Popen class of the subprocess module to #execute the code

#if we are using the Popen class then while reading the output or error we need to use as below
ex:-
import subprocess #importing the subprocess module 
result=subprocess.Popen(<command>,capture_output=True)
print(result.stdout.read())#here we need to use the read() read output
print(result.stderr.read())# we need to use read() to read error

```

**subprocess module has below api befor 3.5v python which valid now also**

```


- call()->
	
    # runs the command and return exit code once the process completed 
    # if the command failed then it will not raise any error simply                  return the exit code as 1 

- check_call()

	#check the command and return the exit code of the command once                  executed
    # but in case of an error it will raise an CalledProcessError                    exception
 

- check_output()->

	# By default the output will be displayed to the normal console if               we are not executing the check_output function
    # but we are executing the check_output() then it will pipe the                  stdout and stderr to the subprocess PIPE using which we                        can capture the output and error of the process

- getoutput()-

	#wait for the shell to execut the command and return its output                 instead of the exit code 

- getstatusoutput()

	# this will be advance version of the getoutput 
    #return the exit code as well as output in the form of a tuple as 
     (exitcode,output)

```
##### **<u>ARGUMENT THAT CAN PASSED TO RUN FUNCTION</u>**

###### **For after python 3.7**:- 

```
#how to capturte the stdout and stderr in subprocess module 

import subprocess #importing the subprocess module 
result=subprocess.run(capture_output=True) 
#fetching the result from the subprocess module 
#as we are mentioning the capture_output=True
	
   this will create below things:-
    - stdout=subprocess.PIPE
    - stderr=subporcess.PIPE
    #so that we can fetch the value in bytes type 
    #if we want to conver to text then there are 2 ways 
    
    
    ```
    - using the decode()
    
    ex:-result=subprocess.run(capture_output=True)
    	print(result.decode()) #here using the decode method
         
  
    -using the text=True in the run function as an argument
    - or we can also mention as "universal_newline=True"
    ex:-result=subprocess.run(<command>,capture_output=True,text=True)
    	print(result)
        result=subprocess.run(<command>,capture_output=True,universal_newline=True)
        print(result)
    ```  
    
###### **before python 3.7v**

```
#how to capturte the stdout and stderr in subprocess module 

import subprocess #importing the subprocess module 
result=subprocess.run(<command>,stdout-subprocess.PIPE,stdout=subprocess.PIPE) 
#fetching the result from the subprocess module 
#as we are mentioning stdout and stderr as subprocess.PIPE
 
    ```
    - using the decode() method only 
    
    ex:-result=subprocess.run(<command>,stdoutsubprocess.PIPE,stdout=subprocess.PIPE)
    	print(result.decode()) #here using the decode method
        
    ```  

##### **how to handle python to throw exception on command being wrong** 

```
#python by default will not raise any error if the command being wrong
#but if we want python to raise an error while command any is wrong then we have to metion check=True 
#this will create CallProcessError Exception if the command not executed propely i.e the exit value isnot 0

ex:-import subprocess #importing the subprocess module 
	result=subprocess.run(<command>,check=True)

```
##### **How to provide stdin i.e input while running a command using the stdin parameter in the run command**

```
- #the stdin will be used when we are dealing with the file object and getting the data from there 
ex:-
import subprocess #importing the subprocess module 
f=open('test.txt','r') #opening the file in the read mode
result=subprocess.run(['python3','test.py'],capture_output=True,stdin=f) 
#here we need to use the stdin so that all text inside test.txt put into stdin  

```

##### **How to provide input as output of some command then how to do that** 

```
-case:-1
# input will be used when we want to provide the output of some other command inside the command we want to execute
# input will be in the bytes format hence we need to be careful 

ex:-
import subprocess #importing the subprocess module 
result1=subprocess.run(['cat','abc.txt'],capture_output=True)
#here capturing the result of one command and this result 1 will be in the bytes format
result2=subprocess.run(['grep','-n'],capture_output=True,input=result1,universal_newline=True)

#here the input will be result 2 which will be output of result 1
#also we can use as text=True or universal_newline=True so that we can use it inside the result2 will now be in the text format

print(result2.stdout)#this will display the output of the command 2


- we can also use input to provide manual value as well

import subprocess #importing the subprocess module 
f=open('test.txt','r') #opening the file in the read mode
result=subprocess.run(['python3','test.py'],capture_output=True,input='abc\ndef',text=-True) 

#here also while executing the python file it will consider the input value provided 
# here \n will consider as the newline and send the data 

```

###### **How to use shlex to prevent the malicious command to be executed **

- we can use the shlex module to prevent the unwanted shell injection
- shlex module provide the quote() which can split the command provided into multiple part considering it as list 

```
ex:-
import subprocess #importing the subprocess module
import shlex #importing the shlex module 
result=subprocess.run(shlex.quote("cat a.txt:pwd"),shell=True,capture_output=True)
#the quote method devide the command as "cat" and "a.txt:pwd"
#as the command is wrong hence return code of 1 will be provided 

```

- But if we want to provide multiple command using the shlex then we can use the shlex module split()

```
import subprocess #importing the subprocess module
import shlex #importing the shlex module 
result=subprocess.run(shlex.split("cat a.txt:pwd"),shell=True,capture_output=True)
#the split method devide the command as "cat" and "a.txt" and ":" and "pwd"
#as the command is wrong hence return code of 1 will be provided 

```
# Python-Exception-handling
## What is Exception Handling in Python or in General
Exception in general sense means when there is something in the code which is not correct (I am talking about statements wriiten or logic) and python script is unable to cope up with the situation and raises an exception. In technical langauage, it is an object which represents an error.
### How to handle it in Python
I am writing the Read Me file on python because I developed the code in the python. Keep the suspicious code in the try block and throws the exception in the except block. If anything goes wrong user will come to know why code is not running. Further, what ever you want to execute, you can keep in the finally block. If test passed both try and except, finally will be executed.
#### Upper Hand of except Exception over except
There are a few exceptions that it wont catch, most obviously KeyboardInterrupt and SystemExit. With simple except it could make it hard for anyone to exit script.

---

#### List of Some Standard Exception in Python:
* **BaseException**: The base class for all built-in exceptions.
* **Exception**: Base class for all exceptions or one can say that all built-in, non-system-exiting exceptions are derived from this class. All user-defined exceptions should also be derived from this class.
* **SystemExit**: This exception is raised by the sys.exit() function. SystemExit does not inherit from Exception. BaseException class is the base class of SystemExit.
* **StandardError**: Base class for all built-in exceptions except **StopIteration** and **SystemExit**.
* **ArithmeticError**: Base class for exception raised for various ArithmeticError such as **OverflowError**, **ZeroDivisionError**, **FloatingPointError**.  
        1.)  **OverflowError:** Raised when a calculation exceeds maximum limit for a numeric type.  
        2.)  **ZeroDivisionError:** Raised when division or modulo by zero takes place for all numeric types.  
        3.)  **FloatingPointError:** Raised when a floating point calculation fails.  
* **EOFError:** When input() reaches the end of a file unexpectedly. If you look at the hierarchy of the exception handling in the python. At the top most point, it comes *BaseException* and at the second leve *Exception* comes and *EOF* comes under Exception. If terminate the process (Ctrl+D) once the user prompt is shown (Please refer to statement input() in python for opening user prompt).
You will get the exception EOF.
* **ImportError**: Raised when an import statement fails.
* **IndexError**:Raised when an index is not found in a sequence.
* **IOError**: Raised when an I/O operation fails such as file not found. I am referring to function such as open().
There are many other standard exception in python and I am referring some of these here.

---

### Use Case of Exception handling:
There are many types of error which are encountered while writing the code and these are used for throwing such errors. Message will come on the screen telling the reason for error. This makes code more useful and informative.

### How to run this code:
Since this is a python file. So simply download the file Exception_handling.py in an directory and points to same oath in terminal or command prompt and run the following command. Before that Please be ensure that you have python installed in your operating system.
```
python Exception_handling.py
```
Thanks for reading the ReadMe File.







        















import threading
t = threading.currentThread().getName() #main tread is created by Python Virtual Machine (PVM)
print('Hello World!')
print(t)
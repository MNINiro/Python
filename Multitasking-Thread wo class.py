from threading import Thread

#====Ex-1====
# def disp(a):
#     print('Thread Running:',a)
#
# t = Thread(target=disp, args=(10,)) #must put',' in the single argument (tuple)
# t.start()
#
# #====Ex-2====
# def disp(a,b):
#     print('Thread Running:',a,b)
#
# t = Thread(target=disp, args=(10,20))
# t.start()
#
# #====Ex-3====
# def disp(a,b):
#     print('Thread Running:',a+b)
#
# t = Thread(target=disp, args=(10,20))
# t.start()

#====Ex-4==== Will run both threads randomly
def disp():
    for i in range(5):
        print("Child Thread ")

t = Thread(target=disp)

t.start()

for i in range(5):
    print("Main Thread")

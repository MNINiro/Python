def print_msg(msg):
    """This is the outer enclosing function"""
##    print(msg)

    def printer():
        """This is the nested function"""
        print(msg)

    return printer  # this got changed

   
another = print_msg("Hello")


##
##That's unusual. The print_msg() function was called with the string "Hello"
##and the returned function was bound to the name another. On calling another(),
##the message was still remembered although we had already finished executing
##the print_msg() function. This technique by which some data ("Hello") gets
##attached to the code is called closure in Python.
##
##When To Use Closures? 
##So what are closures good for? Closures can avoid the use of global values and
##provides some form of data hiding. It can also provide an object oriented
##solution to the problem. When there are few methods (one method in most cases)
##to be implemented in a class, closures can provide an alternate and more
##elegant solutions.

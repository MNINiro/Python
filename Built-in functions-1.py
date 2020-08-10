# Import built-in module math
##import math
##
##content = dir(math)
##print (content)

########################################
def insert_into_global_namespace(
    new_global_name,
    new_global_value = None,
):
    executable_string = """
global %s
%s = %r
""" % (
        new_global_name,
        new_global_name, new_global_value,
    )
    exec (executable_string)  ## suboptimal!

if __name__ == '__main__':
    ## create global variable foo with value 'bar':
    insert_into_global_namespace(
        'foo',
        'bar',
    )
    print (globals()[ 'foo'])


##def fool(x, y):
##    global a
##    a = 42
##    x,y = y,x
##
##    b = 33
##    b = 17
##    c = 100
##    print (a,b,x,y)
##
##a,b,x,y = 1,15,3,4
##
##fool(17,4)
##
##print (a,b,x,y)

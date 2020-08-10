def foo(x,y):

    def do_this(i,j):
        print(i,j)

    def do_that(a,b):
        print(a,b)

    do_this(x+2,y+2)
    do_that(x+1,y+1)

    foo.do_this = do_this
    foo.do_that = do_that

    return


foo = foo(2, 3)

##foo.do_this(3,4)

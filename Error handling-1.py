##try:
##       f=open('testfile.txt')
##except Exception:
##       print('Sorry. This file does not exist')
##       


##
##try:
##       f=open('sample.txt')
##       var=bad_var
##except FileNotFoundError:
##       print('Sorry. This file does not exist')
##except Exception:
##       print('Sorry. Something went wrong')
##       



try:
       f=open('test.txt')
##       print(f.read())
##       f.close()
except FileNotFoundError as e:
       print(e)
except Exception as e:
       print(e)
else:
       print(f.read())
       f.close()
finally:
       print("Executing Finally....")
       
       

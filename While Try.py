while True:

    try:
        number = int(input("What's your fav number?\n"))
        print(18/number)
        break
    except ValueError:
        print("Make sure and enter a number")
    except ZeroDivisionError:
        print("Don't pick zero")
    except:
        break  # not a good idea
    finally:
        print("loop complete")

import datetime

def find_month_first_monday(tstamp = datetime.today()):
    day_of_month = datetime.date.today().timetuple()[2]
    day_of_week = datetime.weekday(tstamp)
    # now I have the dow, and dom, I can index into a 2D array of
    # dates for the month - IF I knew how to get to that array ...


def find_first_gbd_in_month(tstamp = datetime.today()):
    # naive way would be to find the month and year from the passed in arg,
    # calculate the first day for that month/year and iterate until a non-weekend day
    # is found. Not elegant, there must be a better way
    pass


def find_first_gbd_in_year(tstamp = datetime.today()):
   # Ditto, as above.
    pass


def find_ndow_in_month(tstamp = datetime.today()):
    # again, I can get the month and the year from the passed in argument
    # what I need is a 2D array of dates for the month/year, so I can get
    # the nth dow (similar to reading off a calendar)
    pass

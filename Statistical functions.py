import statistics

print(statistics.mean([12,34,10,24]))

print(statistics.median_high([1,3,5,7,9,11])) #Return the high median of data.
       # If data is empty, StatisticsError is raised.
       # The high median is always a member of the data set.
       # When the number of data points is odd, the middle value is returned.
       # When it is even, the larger of the two middle values is returned.



print(statistics.median_low([1,3,5,7]))
       # When the number of data points is odd, the middle value is returned.
       # When it is even, the smaller of the two middle values is returned.


##print(statistics.median_grouped([51, 52, 53, 54],intervale
                                =10) )
       # Return the median of grouped continuous data,
       # calculated as the 50th percentile

##print(statistics.median_grouped([1, 2, 2, 3, 4, 4, 4, 4, 4, 5]))
       # the data are rounded, so that each value represents the midpoint
       # of data classes, e.g. 1 is the midpoint of the class 0.5–1.5, 2
       # is the midpoint of 1.5–2.5, 3 is the midpoint of 2.5–3.5, etc.
       # With the data given, the middle value falls somewhere in the
       # class 3.5–4.5, and interpolation is used to estimate it

       

def getMean(NUmericValue):
    return sum(numericValue)/len(numericValue)

my_list = [1,2,3]

try:
    result = getMean(my_list2)
except ZeroDivisionError as detail:
    print("(Error): {}".format(float('nan')))
    print("(Error): {}".format(detail))
else:
    print("(the mean is): {}".format(result))\
finally:
        print("(finally): the finally block is executed every time")
    


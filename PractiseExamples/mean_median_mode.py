import statistics
def mean_median_mode(list1):
      return [statistics.mean(list1),statistics.median(list1),statistics.mode(list1)]

meanValue , medianValue , modeValue = mean_median_mode([3,5,23,78,34,90,2])
print(f"the mean is {meanValue} \n the median value is {medianValue} \n mode value is {modeValue}")
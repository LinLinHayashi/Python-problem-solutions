'''Given an array of arrays of integers, this program finds the mean of each array of integers, stores the indexes of arrays of the same mean in an array, and then store these index arrays in an array.'''

def meanArrays(a):
  means = []
  result = []

  # Find the mean of each array and store them in the array "means".
  for array in a:
    mean = sum(array) / len(array)
    means.append(mean)

  print(means)

  # Traverse each mean in means.
  for i in range(len(means)):

    # If the current mean is not none, append it to an new array "indexes".
    if means[i] != None:
      indexes = []
      indexes.append(i)

      # Traverse each mean in means after the current mean, and set it to none and append it to indexes if it equals the current mean.
      for j in range(i + 1, len(means)):
        if means[j] == means[i]:
          means[j] = None
          indexes.append(j)
        
      # Append indexes to result.
      result.append(indexes)

  print(result)

# Test samples.
a = [[3, 3, 4, 2],
     [4, 4],
     [4, 0, 3, 3],
     [2, 3],
     [3, 3, 3]]
b = [[-5, 2, 3],
     [0, 0],
     [0],
     [-100, 100]]

meanArrays(a)
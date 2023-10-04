def factorial(num):
  result = 1
  for x in range(num, 1, -1):
    result *= x
  return result

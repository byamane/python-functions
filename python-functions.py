# Challenge 1

def sum_to(n):
  sum = 0
  for i in range(1, n+1):
    sum += i
  print(sum)

sum_to(6)  # returns 21
sum_to(10) # returns 55

# Challenge 2

def largest(list):
  max_num = max(list)
  print(max_num)

largest([1, 2, 3, 4, 0])  # returns 4
largest([10, 4, 2, 231, 91, 54])  # returns 231

# Challenge 3

def occurrences(str1, str2):
  print(str1.count(str2))

occurrences('fleep floop', 'e')   # returns 2
occurrences('fleep floop', 'p')   # returns 2
occurrences('fleep floop', 'ee')  # returns 1
occurrences('fleep floop', 'fe')  # returns 0

# Challenge 4

def product(*args):
  product = 1
  for x in args:
    product *= x
  return product

print(product(-1, 4)) # returns -4
print(product(2, 5, 5)) # returns 50
print(product(4, 0.5, 5)) # returns 10.0
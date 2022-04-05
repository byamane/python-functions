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
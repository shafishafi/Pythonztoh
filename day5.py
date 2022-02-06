def fun(n):
  return n % 3 == 0 and n % 5 == 0

li = list(range(1, 1001)) # list from range (1, 1000) 
print(list(filter (fun, li)))

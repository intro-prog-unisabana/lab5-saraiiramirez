def find_max(a, b, c):
  max_number = a
  if a > b and a > c:
    max_number = a
  elif b > a and b > c:
    max_number = b
  else:
    max_number = c
  return max_number

#FREEZE CODE BEGIN
x = int(input("Enter a number:\n"))
y = int(input("Enter a number:\n"))
z = int(input("Enter a number:\n"))
#FREEZE CODE END

maximum = find_max(x, y, z)

print("Maximum value:", maximum)




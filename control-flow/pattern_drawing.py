rows = int(input("Enter the size of the pattern: "))
x = 0
while x < rows:
  for i in range(rows):
    print("*",end='')
  x+=1
  print()
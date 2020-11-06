num = int(input("Number please: "))
 
n = 1
 
for i in range(1, num + 1):
	n = n * i
 
print("factorial of ", num, " is ", n)
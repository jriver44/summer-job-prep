n = int(input("Number? "))
if n % 2 == 0:
    print("Even")
elif n % 3 == 0:
    print("Divisible by three")
else:
    print("Odd and not divisible by 3")
    
for i in range(5):
    print(i, end=" ")
for char in "Python":
    print(char)
    
count = 0
while count < 3:
    print("Count:", count)
    count += 1
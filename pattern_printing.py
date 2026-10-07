n = int(input("Enter the number of rows:"))
for i in range(1, n+1):
    if i%2 == 1:
        print(str(i)*(n)+str(i+1))
    else:
        print(str(i+1)+str(i)*(n))

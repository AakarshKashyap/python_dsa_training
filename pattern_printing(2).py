n = int(input())
#upper half
star = 2
space = n-2
for i in range(1, (n//2)+1):
    #pre space
    for j in range(i, (n//2)):
        print(" ", end="")
    #star
    for j in range(1, star+1):
        print("*", end="")
    #mid space
    for j in range(space):
        print(" ",end="")
    #star
    for j in range(1,star+1):
        print("*",end="")
    star += 2
    space -= 2
    print()
    
#lower pattern
star = 2*n-1
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(star):
        print("*",end="")
    star -= 2
    print()
        
    
    
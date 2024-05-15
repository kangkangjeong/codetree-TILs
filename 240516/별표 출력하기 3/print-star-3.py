n=int(input())
for i in range(n): 
    for j in range(2*(i)):
        print(" ", end="")
    
    for j in range(n+4-i*2):
        print("*", end=" ")
    print()
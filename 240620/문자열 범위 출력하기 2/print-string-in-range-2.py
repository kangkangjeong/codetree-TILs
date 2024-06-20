given_str = input()
length = len(given_str)
less=int(input())

if length>=less:
    for i in range(less):
        print(given_str[-i-1],end='')
else:
    a=given_str.reverse()
    print(a)
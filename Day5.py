#CodeChef
#LTIME
Q)Chef has his lunch only between 
1 pm and 4 pm (both inclusive).

Given that the current time is X pm, find out whether it is lunchtime for Chef.

Program
*******
T=int(input())
for i in range(0,T):
    X=int(input())
    if(X>=1):
        if(X<=4):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
Input
*****
3
1
7
3
Output
******
YES
NO
YES

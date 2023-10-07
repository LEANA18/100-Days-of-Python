#CodeChef
Chef is not feeling well today. He measured his body temperature using a thermometer and it came out to be X °F.

A person is said to have fever if his body temperature is strictly greater than 98 °F.


Determine if Chef has fever or not.


  Program
  *******
  T=int(input())
for i in range(0,T):
    X=int(input())
    if(X>98):
        print("YES")
    else:
        print("NO")


Input
****
3
98
100
96

Output
*****
NO
YES
NO

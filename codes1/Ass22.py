import numpy
'''For given three equations :-
2x-3y+5z=11
3x+2y-4z=-5
x+y-2z=-3
Here,
X=([x],
   [y],
   [z])
A=([2,-3,5],
   [3,2,-4],
   [1,1,-2])
B=([11],
   [-5],
   [-3])
The values of x,y and z will satisfy the given equations if and only if
                          AX=B
'''
B = [11,-5,-3]
C=[0,0,0]
A=([2,-3,5],
   [3,2,-4],
   [1,1,-2])

X=[0,0,0]
#Taking three inputs x,y and z respectively from the user
print(" Enter the values of x,y and z")
for i in range(3):
    X[i]=int(input(""))
# Here,C=AX

x = numpy.array(A)
y = numpy.array(X)
C = numpy.dot(x,y)


#Checking whether C=B or not
h_t=True
for i in range(3) :
    if(int(C[i])!=int(B[i])):
        h_t=False

if(h_t==True):
    print("x,y and z are solutions of equations")
else:
    print("x,y and z are not solutions of equations")

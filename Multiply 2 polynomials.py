# Multiply 2 polynomials

def multiply(A, B, m, n):
 
    prod = [0] * (m + n - 1);

    for i in range(m):

        for j in range(n):
            prod[i + j] += A[i] * B[j];
 
    return prod;
 
# A utility function to print a polynomial
"""def printPoly(poly, n):
 
    for i in range(n):
        print(poly[i], end = "");
        if (i != 0):
            print("x^", i, end = "");
        if (i != n - 1):
            print(" + ", end = "");
 """

p1 = [1 , 0, 3, 2]
n1=len(p1)

p2 = [2, 0, 4]
n2=len(p2)            

print(multiply(p1,p2,n1,n2))

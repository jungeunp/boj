def GCD(a, b):
	if(b == 0):
		return a
	else:
		return GCD(b, a%b)
	
A, B = map(int, input().split())
C, D = map(int, input().split())

E = A*D + B*C
F = B*D

tmp = GCD(F, E)
print (E//tmp, F//tmp)

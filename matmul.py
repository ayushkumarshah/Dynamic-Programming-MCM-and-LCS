# Dynamic Programming Python implementation of Matrix Chain Multiplication. 
import sys
from time import time
# Matrix Ai has dimension p[i-1] x p[i] for i = 1..n
def MatrixChainOrder(p, n):
	# For simplicity of the program, one extra row and one
	# extra column are allocated in m[][].  0th row and 0th
	# column of m[][] are not used
	m = [[0 for x in range(n)] for x in range(n)]
	s = [[0 for x in range(n)] for x in range(n)]
	# m[i,j] = Minimum number of scalar multiplications needed
	# to compute the matrix A[i]A[i+1]...A[j] = A[i..j] where
	# dimension of A[i] is p[i-1] x p[i]

	# cost is zero when multiplying one matrix.
	for i in range(1, n):
		m[i][i] = 0
	# L is chain length.
	for L in range(2, n):
		for i in range(1, n-L+1):
			j = i+L-1
			m[i][j] = sys.maxsize
			#print("m[%d][%d]"%(i,j))
			for k in range(i, j):
				# q = cost/scalar multiplications
				q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
				if q < m[i][j]:
					m[i][j] = q
					s[i][j]=k
	return m,s
 
def print_optimal_parens(s, i, j):
	#print("Hello %d %d" %(i,j))
	if i == j:
		print ("A%d" % (i),end="")
	else:
		print ("(",end="")
		print_optimal_parens(s, i, s[i][j])
		print_optimal_parens(s, s[i][j]+1, j)
		print (")",end="")

# Driver program to test above function
n=[]
el_time=[]
arr = [[2,3],[3,4,6],[1,3,6,7],[5,4,6,2,7],[2,4,5,6,7,8],[2,4,5,3,6,7,8],[4,3,2,5,6,4,3,2],
	[3,5,6,4,3,5,6,7,8],[3,4,5,3,6,7,8,9,5,10],[2,4,5,7,8,2,4,10,12,5,6]]
for j in range(10):
	n.insert(j,len(arr[j])-1)
	start_time = time() # record the starting time
	m,s=MatrixChainOrder(arr[j], len(arr[j]))
	print("\nP="+str(arr[j]))
	print ("\nm table\n")     
	for i in range(n[j]):
		for j in range(n[j]):
			print (str(m[i][j])+"\t",end="")
		print("")	
	print ("\ns table\n")
	for i in range(n[j]):
		for j in range(n[j]):
			print (str(s[i][j])+"\t",end="")
		print("")
	print("\nAns:",end="")	
	print_optimal_parens(s, 1,n[j] )
	print("")
	end_time = time() # record the ending time
	el_time.insert(j,end_time-start_time)
print ("\n\nn\tElasped Time")
for i in range(10):
	print (str(n[i])+"\t"+str(el_time[i]))


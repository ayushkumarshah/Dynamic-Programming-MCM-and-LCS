# Dynamic programming implementation of LCS problem
from time import time
# Returns length of LCS for X[0..m-1], Y[0..n-1] 
def lcs(X, Y, m, n):
	L = [[0 for x in range(n+1)] for x in range(m+1)]
	# Following steps build L[m+1][n+1] in bottom up fashion. Note
	# that L[i][j] contains length of LCS of X[0..i-1] and Y[0..j-1] 
	for i in range(m+1):
		for j in range(n+1):
			if i == 0 or j == 0:
				L[i][j] = 0
			elif X[i-1] == Y[j-1]:
				L[i][j] = L[i-1][j-1] + 1
			else:
				L[i][j] = max(L[i-1][j], L[i][j-1])   
	print ("\nL table")
	for i in range(m+1):
		for j in range(n+1):
			print(str(L[i][j])+"\t",end="")
		print("")
	
	# Following code is used to print LCS
	index = L[m][n]
	org_index=index

	# Create a character array to store the lcs string
	lcs = [""] * (index+1)
	lcs[index] = ""

	# Start from the right-most-bottom-most corner and
	# one by one store characters in lcs[]
	i = m
	j = n
	while i > 0 and j > 0:
		# If current character in X[] and Y are same, then
		# current character is part of LCS
		if X[i-1] == Y[j-1]:
			lcs[index-1] = X[i-1]
			i-=1
			j-=1
			index-=1

		# If not same, then find the larger of two and
		# go in the direction of larger value
		elif L[i-1][j] >= L[i][j-1]:
			i-=1
		else:
			j-=1
	print ("\nLength of LCS is "+str(org_index))
	print ("LCS of " + X + " and " + Y + " is " + "".join(lcs) )

el_time=[]
mn=[]
start_time=0
end_time=0
# Driver program
X = ["AGGTAB","ABRAC", "BACDB","AYUSH","KAMLESH","SUNIL","BIBASH","ARAJU","MANASI","DEEPESH"]
Y = ["GXTXAYB","YABBAD","BDCB","SHAHA","MAHES","UNATTI","SHOWIN","ARUNADHA","ANSI","DISH"]
for i in range(10):
	m = len(X[i])
	n = len(Y[i])
	start_time=time()
	lcs(X[i], Y[i], m, n)
	end_time=time()
	mn.insert(i,m*n)
	el_time.insert(i,end_time-start_time)

print ("\nmn\tTime")
for i in range(10):
	print(str(mn[i])+"\t"+str(el_time[i]))




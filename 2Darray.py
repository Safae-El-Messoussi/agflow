
N = input("Enter the value of N : ") 
M = input("Enter the value of M : ")
N = int(N)
M = int(M)

while N <= 0 or M <= 0:
    print("M and N should be greater than 0.")
    N = input("Enter the value of N : ") 
    M = input("Enter the value of M : ")
    N = int(N)
    M = int(M)
    
t = [[0 for x in range(N)] for y in range(M)] 
for i in range(0,N):
    for j in range(0,M):
        if (j>=i):
            t[i][j] = j*j+i+1
        elif(j == 0):
            t[i][j]=(i+1)*(i+1)
        else:
            t[i][j] = t[i][j-1] - 1
        
for i in range(0,N):
    for j in range(0,M):
        print("t[",i,"][",j,"] =",t[i][j])

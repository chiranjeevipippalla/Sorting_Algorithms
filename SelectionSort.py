print("=== SELECTION SORT ====")
print("")
A = [5,4,3,2,1]
n = len(A)

print("Un-Sorted Array: Before Selection Sort")
print(A)
print("")

for i in range(n-2):
    i_min = i
    for j in range (i+1,n):
        if A[j] < A[i_min]:
            i_min = j

    temp = A[i]
    A[i] = A[i_min]
    A[i_min] = temp

print("Sorted Array: After Selection Sort")
print(A)
print("")

#Output:
#=== SELECTION SORT ====

#Un-Sorted Array: Before Selection Sort
#[5, 4, 3, 2, 1]

#Sorted Array: After Selection Sort
#[1, 2, 3, 4, 5]    

                    

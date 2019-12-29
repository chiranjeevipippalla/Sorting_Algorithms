print("=== BUBBLE SORT ====")
print("")
A = [5,4,3,2,1]
n = len(A)

print("Un-Sorted Array: Before Bubble Sort")
print(A)
print("")

for i in range(n): #we reference i for the number of passes
    for j in range(n-i-1): #after every pass, the last element is sorted. so -i
        if A[j]>A[j+1]:
            A[j], A[j+1] = A[j+1], A[j] #swapping the positions of j and j+1
    
print("Sorted Array: After Selection Sort")
print(A)
print("")

#Output:
#=== BUBBLE SORT ====

#Un-Sorted Array: Before Bubble Sort
#[5, 4, 3, 2, 1]

#Sorted Array: After Bubble Sort
#[1, 2, 3, 4, 5]    

                    

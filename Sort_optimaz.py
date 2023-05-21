#bubble sort
def num_optim (a):
    iterations = 0
    for i in range(len(a)):
         for j in range(len(a)-i-1):
            iterations += 1
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1], a[j]

    return (a, iterations)

#insertion sort
def num_optim2 (a):
    for j  in range(1, len(a)):
        key = a[j]
        i = j - 1
        while i >= 0 and a[i] > key:
            a[i+1] = a[i]
            i -= 1
        a[i+1] = key

    return (a)

a = [3,9,15,1,2,45,5,89]

print(num_optim(a))
print(num_optim2(a))


def insert_sort (a) :
    for j in range (1,  len(a)):
        key = a[j]
        i = j - 1

        while i >=0 and a[i] > key:
            a[i+1] = a[i]
            i-=1

        a[i + 1] = key
        
    
    return a

        

if __name__ == "__main__":
    print (insert_sort([3, 2, 1]))
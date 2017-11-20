def odd_evens():
    for i in range(1,2001):
        if i%2 == 0:
            print "Number is",i, "This is an even number"
        else:
            print "Number is",i, "This is an odd number"
odd_evens()


def multiply(arr):
    for i in range(0,len(arr)):
       arr[i] = arr[i] * 5
    print arr

new_array = [3,6,9,10]
multiply(new_array)

#new_array = [3,6,9,10]



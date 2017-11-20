"""for numbers in range(1, 1001, 2):
    print numbers



for numbers in range(5,1000001,5):
    print numbers"""

a = [1, 2, 5, 10, 255, 3]
sum = 0
for i in a:
    sum += i
print sum

average = sum / len(a)
print average

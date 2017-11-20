import random
for x in range(10):
    x = random.randint(40,101)
    if x >=90:
        print "Score:",x,"Your grade is A"
    elif x >=80:
        print "Score:",x,"Your grade is B"
    elif x >=70:
        print "Score:",x,"Your grade is C"
    elif x >=60:
        print "Score:",x,"Your grade is D"
    else:
        print "YOU FAILED"

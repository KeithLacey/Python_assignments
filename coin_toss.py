import random
flips = 0
heads = 0
tails = 0
while flips < 40:
    flips += 1
 #   heads += 1
#    tails += 1
    coin = random.randint(1, 2)
    if coin == 1:
        heads += 1
        print "Attempt #",flips,"Throwing a coin...It's a Heads!..got",heads,"head(s) so far and",tails,"tails so far"
    if coin == 2:
        tails += 1
        print "Attempt #",flips,"Throwing a coin...It's a Tails!..got",tails,"tail(s) so far and",heads,"heads so far"
total = flips
print(total)

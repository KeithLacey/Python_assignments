class bike(object):
    def _init_(price,max_speed,miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):
        print "The price is:$"+ str(self.price)
        print "The Max speed is" + str(self.max_speed) + "MPH"
        print "The total miles are:" + str(self.miles)

    def ride(self):
        print "Riding"
        self.miles += 10

    def reverse(self):
        print "Reversing"
        self.miles -= 5

     
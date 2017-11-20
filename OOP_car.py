class car(object):
    def _init_(price, speed, fuel, mileage)
        self.price = price
            if price > 10000:
                self.tax = .15
            else:
                self.tax = .12
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.display_all()

    def display_all(self):
        print "price:" + str(self.price)
        print "speed:" + str(self.speed)
        print "fuel:" + str(self.fuel)
        print "mileage:" + str(self.mileage)
        print "tax:" + str(self.tax)

car1 = car(2000,35,full,15)
car2 = car(2000,5,full,105)
car3 = car(2000,15,kind of full,95)
car4 = car(2000,25,full,25)
car5 = car(2000,45,empty,25)
car6 = car(20000000,35,empty,15)
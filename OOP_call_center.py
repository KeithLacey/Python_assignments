from datetime import datetime

class Call(object):
    num_call = 0
    def __init__(self, name, phone_number, reason):
        self.id = Call.num_call
        self.name = name
        self.phone_number = phone_number
        self.time = datetime.now()
        self.reason = reason

        Call.num_call += 1

    def display(self):
        print self.id
        print self.name
        print str(self.phone_number)
        print str(self.time)
        print self.reason
    
    
C = Call("john",2222222, "emergency")
C.display()


class Center_Class(Call):
    def __init__()
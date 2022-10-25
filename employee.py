"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    employeeType = 0
    pay = 0
    salary = 0
    wage = 0
    hours = 0
    bonusCommission = 0
    contractCommission = 0
    numContracts = 0
    sentence = ""

    def __init__(self, name, eT, s, w,h, bc, cc,nc):
        self.name = name
        self.employeeType = eT
        if (self.employeeType == 1):
            self.salary = s
        elif (self.employeeType == 2):
            self.wage = w
            self.hours = h
        elif (self.employeeType == 3):
            self.salary = s 
            self.bonusCommission = bc
        elif (self.employeeType == 4):
            self.wage = w
            self.hours = h
            self.bonusCommission = bc
        elif (self.employeeType == 5):
            self.salary = s
            self.contractCommission = cc
            self.numContracts = nc
        else:
            self.wage = w
            self.hours = h
            self.contractCommission = cc
            self.numContracts = nc

    def get_pay(self):
        self.pay = self.salary + (self.hours * self.wage) + self.bonusCommission + (self.contractCommission * self.numContracts)
        print(str(self.pay))
        return self.pay

    def __str__(self):
        self.pay = self.salary + (self.hours*self.wage) + self.bonusCommission + (self.contractCommission*self.numContracts)
        if self.employeeType == 1:
            sentence = self.name + " works on a monthly salary of " + str(self.salary) + ". Their total pay is " + str(self.pay) + "."
            return sentence
        elif self.employeeType == 2:
            sentence = self.name + " works on a contract of " + str(self.hours) + " hours at " + str(self.wage) + "/hour. Their total pay is " + str(self.pay) + "."
            return sentence
        elif self.employeeType == 3:
           sentence = self.name + " works on a monthly salary of " + str(self.salary) + " and receives a bonus commission of " + str(self.bonusCommission) + ". Their total pay is " + str(self.pay) + "."
           return sentence
        elif self.employeeType == 4:
            sentence = self.name + " works on a contract of " + str(self.hours) + " hours at " + str(self.wage) + "/hour and receives a bonus commission of " + str(self.bonusCommission) + ". Their total pay is " + str(self.pay) + "."
            return sentence
        elif self.employeeType == 5:
            sentence = self.name + " works on a monthly salary of " + str(self.salary) + " and receives a commission for " + str(self.numContracts) + " contract(s) at " + str(self.contractCommission) + "/contract. Their total pay is " + str(self.pay) + "."
            return sentence
        else:
            sentence = self.name + " works on a contract of " + str(self.hours) + " hours at " + str(self.wage) + "/hour and receives a commission for " + str(self.numContracts) + " contract(s) at " + str(self.contractCommission) + "/contract. Their total pay is " + str(self.pay) + "."
            return sentence


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie',1,4000,0,0,0,0,0)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie',2,0,25,100,0,0,0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee',5,3000,0,0,0,200,4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan',6,0,25,150,0,220,3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie',3,2000,0,0,1500,0,0)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel',4,0,30,120,600,0,0)

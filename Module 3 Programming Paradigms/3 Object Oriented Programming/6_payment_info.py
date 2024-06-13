class Payslip:
    def __init__(self, name, payment, amount) -> None:
        self.name = name
        self.payment = payment
        self.amount = amount

    def pay(self):
        self.payment = "yes"

    def status(self):
        if self.payment == "yes":
            return self.name + " is paid $"+(str(self.amount))
        else:
            return self.name + " is not paid yet"


nathan = Payslip("Nathan", "no", 1000)
roger = Payslip("Roger", "no", 3000)

print(nathan.status(), "\t", roger.status())

nathan.pay()
print("After payment")
print(nathan.status(), "\t", roger.status())

""" 
Question

Your code has the class meal, along with the method calories() that prints a number value. You also have three instance objects: breakfast, lunch, and dinner. If you call calories() in an instance and change the value, the other instances are not affected. True or false?     

True

Correct
Correct! Changes made in an instance object affect only that instance.
"""

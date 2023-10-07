class Category:

    ledger = []
    categories = []
   
    def __init__(self, description):
        self.description = description

        if description not in self.categories:
            self.categories.append(description)

        print('categories ', self.categories)
    
    def deposit(self, amount, description=""):
        print('ledger: ', self.ledger)
        print('Depositing: ', amount)
        self.ledger = []
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        print('Withdrawing: ', amount)
        balanceCheck = self.check_funds(amount)
        if balanceCheck == True:
            self.ledger.append({"amount": amount*-1, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        total = 0
        for entry in self.ledger:
            total = total + float(entry["amount"])
            
        return (round(total,2))

    def transfer(self, amount, destination):

        balanceCheck = self.check_funds(amount)
        if balanceCheck == True:
        # print(destination.description)
            self.ledger.append({"amount": amount*-1, "description":   "Transfer to " + destination.description})
            destination.ledger = []
            destination.ledger.append({"amount": amount, "description": "Transfer from " + self.description})
            return True
        else:
            return False
                
        #print(self.ledger)
        #print(destination.ledger)
    
    def check_funds(self, amount):
        currentBalance = self.get_balance()
        print('currentBal: ', currentBalance)
        if amount > self.get_balance():
            return False
        else:
            return True
            

def create_spend_chart(categories):

    print('categories for chart', Category.categories)
       

    return
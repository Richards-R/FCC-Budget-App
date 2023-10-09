class Category:
   
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        title = f'{self.name:*^30}\n'
        items = ""
        total = 0
        for item in self.ledger:
           items += f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}" + '\n'

           total += item['amount']
        
        output = title + items + "Total: " + str(total)
        print(output)
        return output 
   
    def deposit(self, amount, description=""):
        print('Depositing: ', amount)
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

    def transfer(self, amount, category):

        balanceCheck = self.check_funds(amount)
        if balanceCheck == True:
            self.ledger.append({"amount": amount*-1, "description":   "Transfer to " + category.name})
            category.ledger.append({"amount": amount, "description": "Transfer from " + self.name})
            return True
        else:
            return False

    def check_funds(self, amount):
        currentBalance = self.get_balance()
        print('currentBal: ', currentBalance)
        if amount > self.get_balance():
            return False
        else:
            return True

        
def create_spend_chart(categories):

    print('categories for chart', Category.categories)
       

